# ui-designer

A skill that runs the **Discover → Define → Deliver** process so an AI agent produces distinctive,
world-class design instead of the model's average.

The process comes from **“How to turn your AI into a world-class designer”** by **Anshu Chimala**
(Apple design and engineering lead for 12 years), published in
[Lenny's Newsletter](https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world). Read
[NOTICE.md](NOTICE.md) before reusing anything here.

> 中文：把「Discover → Define → Deliver」这套设计方法论做成可执行的 skill，让 AI agent 产出有辨识度的设计而不是平均值。方法论出自 Anshu Chimala 的文章，署名与边界见 NOTICE.md。

## What it does

It treats design as a process problem, not a capability problem: models pick the most likely next token
at every decision, so they converge on the same average output. The skill pushes them off that default,
then judges the result from pictures rather than code.

| Stage | What it produces |
|---|---|
| **Discover** | Several genuinely different directions, each with a written brief and a rendered first pass |
| **Define** | One direction with its own identity, confirmed by a blind design critic scoring ≥ 9/10 twice |
| **Deliver** | Subtraction, AI-tell sweep, copy supplied by the user, verified in a browser |

## Contents

| Path | What it is |
|---|---|
| [SKILL.md](SKILL.md) | The skill itself — triggers, three stages, operating rules, screenshot workflow, checklists |
| [references/discover.md](references/discover.md) | Stage 1: seed strings, ambitious prompts, the three-step ideation system |
| [references/define.md](references/define.md) | Stage 2: the design-critic loop, image generation, video generation |
| [references/deliver.md](references/deliver.md) | Stage 3: subtraction, AI-tell sweep (antislop-backed when that family is installed), obtaining the copy |
| [references/prompt-library.md](references/prompt-library.md) | Every prompt, ready to copy — quoted ones marked **source** |
| [references/sources.md](references/sources.md) | Provenance: what is verbatim, what is a reader's summary, what this skill added |
| [scripts/seed_string.py](scripts/seed_string.py) | Generates seed strings for Technique 1 |
| [scripts/verify_skill.py](scripts/verify_skill.py) | Checks the package: frontmatter, links, per-section Chinese |

## Optional companion: antislop

Technique 7 (remove AI tells) defers to the third-party
[`antislop`](https://github.com/miqdadbadjuber/anti-slop) family when it is installed: load `antislop`
with `antislop-ui` and run them as the sweep. What they add is recorded in
[references/deliver.md](references/deliver.md), checked against `antislop` 3.2.20 — the purpose test,
the rules that allow no exception (the em-dash and accessibility tier), the dose caps, the app-shaped
tells, and the liveliness dials that stop over-filtering from producing a sterile result.

Nothing here requires it. With no antislop installed, the eight tell categories in
[references/deliver.md](references/deliver.md) are the whole pass. The two sets also do not fight over
the copy: whenever the copy carries a tell, both say to report it to the user rather than silently
rewrite a string the user owns (Technique 8).

> 中文：T7（清 AI 味）在本机装有第三方 [`antislop`](https://github.com/miqdadbadjuber/anti-slop) 系列时以它为准：调 `antislop` + `antislop-ui` 来跑这一步。它补了什么记在 `references/deliver.md` 里（对照的是 antislop 3.2.20）——目的测试、没有例外的那一层（破折号与无障碍）、剂量上限、应用界面形态的 AI 味，以及防止「过滤过头变成无菌默认」的活力刻度。没有它也能跑：不装时 `references/deliver.md` 的八类就是全部。两者在文案上也不冲突——凡是用户提供的文案里发现 AI 味，两边都要求**报告**而不是擅自改写（T8）。

## Install

A skill is discovered from a skills root, not from wherever you cloned it. Copy `SKILL.md`,
`references/` and `scripts/` into `<skills-root>/ui-designer/`, where `<skills-root>` is one of:

```text
User-level (every project)
  Windows        %USERPROFILE%\.agents\skills
  macOS / Linux  ~/.agents/skills
  Claude Code    ~/.claude/skills

Project-level (that project only)
  any project    <project-root>/.agents/skills     # shared by tools that read .agents
  DeepSeek DSH   <project-root>/.dsh/skills        # DSH's own project root
```

`<project-root>` is **the nearest ancestor directory containing `.git`** — not the directory you
happen to be in. DSH and similar harnesses fall back to the starting directory when there is no
`.git` anywhere above it. The `.agents` or `.dsh` folder must sit in that root, so
`<project-root>/.agents/skills/ui-designer` works and `<project-root>/ui-designer` does not.

The folder name must match the `name:` in the frontmatter (`ui-designer`). Anything that reads a
`SKILL.md` can follow it — no build step, no dependencies beyond Python 3 for the seed script.
Skills are discovered when a session resolves its working directory, so start a new session in that
project after installing.

```powershell
$dest = "$env:USERPROFILE\.agents\skills\ui-designer"     # or <project-root>\.agents\skills\ui-designer
$src  = "$env:TEMP\ui-designer-src"

New-Item -ItemType Directory -Force -Path $dest | Out-Null
git clone --depth 1 https://github.com/skr-wu999/ui-designer.git $src

# copy the skill only: a skills root should not carry the clone's .git, .gitignore or repo docs
Copy-Item "$src\SKILL.md" $dest -Force
Copy-Item "$src\references", "$src\scripts" $dest -Recurse -Force
Remove-Item $src -Recurse -Force
```

That leaves `<skills-root>/ui-designer/` holding just `SKILL.md`, `references/` and `scripts/` —
about 85 KB, and exactly what `scripts/verify_skill.py` calls the core package. `README.md`,
`LICENSE` and `NOTICE.md` are repository docs and are not needed inside a skills root; copy them too
if you want them to travel with the skill. The verifier notes their absence instead of failing on it.

> 中文：skill 必须放进 skills 根目录下的 `ui-designer\` 里。用户级位置是 `~\.agents\skills`（所有项目可用）；项目级位置是 **项目根**（含 `.git` 的最近祖先目录，没有 `.git` 时用会话启动目录）下的 `.agents\skills` 或 DSH 的 `.dsh\skills`。只复制 `SKILL.md`、`references\`、`scripts\` 三项即可（约 85 KB），不要把 clone 出来的 `.git`、`.gitignore` 和仓库文档一起塞进 skills 根。目录名要与 frontmatter 里的 `name` 一致。装好后在该项目新开会话即可生效——skill 在会话解析工作目录时被发现。`README.md`／`LICENSE`／`NOTICE.md` 属于仓库文档，校验器对它们的缺失只提示不报错。除种子脚本需要 Python 3 之外没有依赖，也没有构建步骤。

## Verify

```bash
python scripts/verify_skill.py     # frontmatter, links, per-section Chinese
python scripts/seed_string.py --count 3
```

`verify_skill.py` exits non-zero if the skill package is incomplete. Three groups are reported as
skipped rather than passed silently when their inputs are absent: the repository docs (normal for a
skills-root install, which holds only the core package), quote traceability against the article text,
and the figure index. The latter two need local material this repository does not ship (see below).

> 中文：`verify_skill.py` 在 skill 本体不完整时以非零退出。有三组检查在缺少输入时**报「跳过」而不是静默通过**：仓库文档（skills 根安装的正常情况，因为那里只放核心包）、引文可溯源、图片存在性；后两组需要本仓库不提供的本地素材（见下）。

## What this repository does not include

- **The article's text.** The method notes are summaries and short quotes; the full post is paywalled
  and is not redistributed here.
- **The article's images.** Its screenshots and animated demos belong to the author and are not
  included. [references/sources.md](references/sources.md) describes what each figure shows, so you can
  follow along while reading the original.
- **Techniques 7 and 8 in the author's own words.** Those sections sit behind the paywall; what is here
  is built from a reader's one-line summary and is labelled as such throughout.

> 中文：本仓库不包含原文全文、不包含作者的原图，付费墙后的 Technique 7／8 也标明「据读者摘要补写」。想读原始论证与前后对比图，请看原文。

## License

MIT for this skill's own text and code — see [LICENSE](LICENSE). The methodology, the technique names
and the quoted prompts belong to their author; see [NOTICE.md](NOTICE.md).

> 中文：本 skill 自身的文字与代码用 MIT；方法论、技法名称与引用的提示词归原作者，详见 NOTICE.md。
