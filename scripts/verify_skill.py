"""Check this skill package: frontmatter, internal links, per-section Chinese explanations.

Two extra groups run only when their inputs are present locally, and are skipped with a note otherwise:
  * quote traceability — needs the article text at _build/article.md (or ARTICLE_PATH)
  * figure index       — needs the saved page's asset folder under _source/

A check that silently matches nothing is worse than no check, so every skipped group is reported.

    python scripts/verify_skill.py
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLE = Path(os.environ.get("ARTICLE_PATH", ROOT / "_build" / "article.md"))

# (phrase, files that must contain it) — every phrase must also appear in the article text.
QUOTES = [
    ("generate a long, random alphanumeric string using a shell script", ["references/discover.md", "references/prompt-library.md"]),
    ("don't reveal the string in the design", ["references/discover.md", "references/prompt-library.md"]),
    ("bold pixel art theme", ["references/discover.md", "references/prompt-library.md"]),
    ("isometric living 3d city", ["references/discover.md", "references/prompt-library.md"]),
    ("uncomfortable negative space", ["references/discover.md", "references/prompt-library.md"]),
    ("go broad, not deep", ["references/discover.md", "references/prompt-library.md"]),
    ("clicky, satisfying buttons, nice sounds", ["references/discover.md"]),
    ("can you sharpen this one based on my tastes", ["references/discover.md", "references/prompt-library.md"]),
    ("write a concise prompt that an ai agent could use", ["references/discover.md", "references/prompt-library.md"]),
    ("invoke the critic in a fresh context, with just the screenshot", ["references/define.md", "references/prompt-library.md"]),
    ("imagine how a top design studio would execute this aesthetic", ["references/define.md", "references/prompt-library.md"]),
    ("penalize", ["references/define.md", "references/prompt-library.md"]),
    ("your work is only complete when the critic independently deems it 9/10 or higher", ["references/define.md", "references/prompt-library.md"]),
    ("do not put that criterion in the critic prompt", ["references/define.md", "references/prompt-library.md"]),
    ("use the same critic prompt each time", ["references/define.md", "references/prompt-library.md"]),
    ("4 professional examples and 1 screenshot of our product", ["references/define.md", "references/prompt-library.md"]),
    ("treat these as a baseline or a moodboard", ["references/define.md"]),
    ("don't go too small", ["references/define.md"]),
    ("less than 10% of output tokens", ["references/define.md"]),
    ("verify that your work looks right frame-by-frame in the browser", ["references/define.md", "references/prompt-library.md"]),
    ("create a gitignored file called .env.agents", ["references/define.md", "references/prompt-library.md"]),
    ("remove the background with a video matting model", ["references/define.md", "references/prompt-library.md"]),
    ("use the final frame of that video to seed the next transition", ["references/define.md", "references/prompt-library.md"]),
    ("simplify the layout into an image-centric grid", ["references/deliver.md", "references/prompt-library.md"]),
    ("get rid of gradients, glows, and unnecessary containers", ["references/deliver.md", "references/prompt-library.md"]),
    ("aim for a truly minimalist aesthetic that feels apple-native", ["references/deliver.md", "references/prompt-library.md"]),
]

REQUIRED = ["SKILL.md", "README.md", "LICENSE", "NOTICE.md", "references/discover.md",
            "references/define.md", "references/deliver.md", "references/prompt-library.md",
            "references/sources.md", "scripts/seed_string.py"]

EXPECTED_FRONTMATTER = ["name", "description", "allowed-tools"]
LINK_RE = re.compile(r"`((?:references|scripts|_build)/[\w./-]+)`")
FIGURE_RE = re.compile(r"`([\w-]+\.(?:jpg|jpeg|png|gif|webp))`")


def norm(text: str) -> str:
    text = text.replace("\u2019", "'").replace("–", "-")
    text = re.sub(r"(?m)^\s*>\s?", " ", text)
    text = re.sub(r"[`*_]", "", text)
    return re.sub(r"\s+", " ", text).lower()


def main() -> int:
    failures: list[str] = []
    skipped: list[str] = []
    notes: list[str] = []
    checks = 0

    skill_path = ROOT / "SKILL.md"
    skill = skill_path.read_text(encoding="utf-8")
    raw_bytes = skill_path.read_bytes()

    # 1. frontmatter
    m = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
    if not m:
        failures.append("SKILL.md: no YAML frontmatter block")
    else:
        fm = m.group(1)
        for key in EXPECTED_FRONTMATTER:
            checks += 1
            if not re.search(r"^%s:" % re.escape(key), fm, re.M):
                failures.append("SKILL.md: frontmatter missing '%s'" % key)
        name = re.search(r'^name:\s*"?([\w-]+)"?', fm, re.M)
        checks += 1
        if not name:
            failures.append("SKILL.md: frontmatter has no name")
        elif name.group(1) != ROOT.name:
            # Not a failure: people clone into arbitrary folder names. It only matters on install.
            notes.append("folder is '%s' but the skill name is '%s' — rename the folder on install"
                         % (ROOT.name, name.group(1)))
        if "中文" not in fm:
            failures.append("SKILL.md: description has no Chinese trigger text")

        # No YAML library required: assert the frontmatter shapes that break loaders.
        lines = fm.splitlines()
        checks += 1
        if b"\t" in raw_bytes:
            failures.append("SKILL.md: tab character inside the frontmatter block")
        checks += 1
        if raw_bytes.startswith(b"\xef\xbb\xbf"):
            failures.append("SKILL.md: file starts with a UTF-8 BOM")
        checks += 1
        if len(lines) != len(EXPECTED_FRONTMATTER):
            failures.append("SKILL.md: frontmatter has %d lines, expected %d one-line keys"
                            % (len(lines), len(EXPECTED_FRONTMATTER)))
        checks += 1
        desc_lines = [ln for ln in lines if ln.startswith("description:")]
        if len(desc_lines) != 1 or not desc_lines[0].endswith('"'):
            failures.append("SKILL.md: description must be a single double-quoted line")
        else:
            inner = desc_lines[0][len("description: "):]
            checks += 1
            if inner[0] != '"' or inner[1:-1].count('"'):
                failures.append("SKILL.md: description contains an unescaped double quote")

    # 2. links resolve, across every markdown file
    md_files = sorted(ROOT.glob("*.md")) + sorted((ROOT / "references").glob("*.md"))
    for path in md_files:
        rel = path.relative_to(ROOT).as_posix()
        for target in sorted(set(LINK_RE.findall(path.read_text(encoding="utf-8")))):
            checks += 1
            if not (ROOT / target).exists():
                failures.append("%s: broken link -> %s" % (rel, target))

    # 3. language convention: every section of the skill itself carries a Chinese explanation.
    #    README.md and NOTICE.md are repository docs, not skill instructions, so they are exempt.
    skill_md = [ROOT / "SKILL.md"] + sorted((ROOT / "references").glob("*.md"))
    for path in skill_md:
        rel = path.relative_to(ROOT).as_posix()
        parts = re.split(r"(?m)^(#{2,3}) (.+)$", path.read_text(encoding="utf-8"))
        for i in range(1, len(parts), 3):
            checks += 1
            if "中文" not in parts[i + 2]:
                failures.append("%s: section '%s' has no Chinese explanation"
                                % (rel, parts[i + 1].strip()))

    # 4. required files
    for rel in REQUIRED:
        checks += 1
        if not (ROOT / rel).exists():
            failures.append("missing required file: %s" % rel)

    # 5. quote traceability (needs the article text)
    if ARTICLE.exists():
        article = norm(ARTICLE.read_text(encoding="utf-8"))
        for phrase, files in QUOTES:
            checks += 1
            if norm(phrase) not in article:
                failures.append("article text: phrase not found -> %r" % phrase)
                continue
            for rel in files:
                path = ROOT / rel
                checks += 1
                if not path.exists():
                    failures.append("%s: missing file" % rel)
                elif norm(phrase) not in norm(path.read_text(encoding="utf-8")):
                    failures.append("%s: missing quoted phrase -> %r" % (rel, phrase))
    else:
        skipped.append("quote traceability (no article text at %s)" % ARTICLE)

    # 6. figure index (needs the saved page's assets)
    assets = [p for p in (ROOT / "_source").glob("*_files") if p.is_dir()]
    sources_md = (ROOT / "references" / "sources.md").read_text(encoding="utf-8")
    names = sorted(set(FIGURE_RE.findall(sources_md)))
    if assets and names:
        for name in names:
            checks += 1
            if not any((a / name).exists() for a in assets):
                failures.append("sources.md: figure not on disk -> %s" % name)
    else:
        skipped.append("figure index (%d filenames named, no _source asset folder)"
                       % len(names))

    print("checks: %d" % checks)
    print("failures: %d" % len(failures))
    for f in failures:
        print("  FAIL", f)
    for n in notes:
        print("  note:", n)
    for s in skipped:
        print("  skipped:", s)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
