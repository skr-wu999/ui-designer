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
| [references/deliver.md](references/deliver.md) | Stage 3: subtraction, AI-tell sweep, obtaining the copy |
| [references/prompt-library.md](references/prompt-library.md) | Every prompt, ready to copy — quoted ones marked **source** |
| [references/sources.md](references/sources.md) | Provenance: what is verbatim, what is a reader's summary, what this skill added |
| [scripts/seed_string.py](scripts/seed_string.py) | Generates seed strings for Technique 1 |
| [scripts/verify_skill.py](scripts/verify_skill.py) | Checks the package: frontmatter, links, per-section Chinese |

## Install

A skill is discovered from a skills root, not from wherever you cloned it. Copy `SKILL.md`,
`references/` and `scripts/` into one of:

```text
Windows   %USERPROFILE%\.agents\skills\ui-designer
macOS     ~/.agents/skills/ui-designer
Claude    ~/.claude/skills/ui-designer
```

The folder name must match the `name:` in the frontmatter (`ui-designer`). Anything that reads a
`SKILL.md` can follow it — no build step, no dependencies beyond Python 3 for the seed script.

> 中文：skill 需要放进 agent 的 skills 根目录才会被加载；目录名要与 frontmatter 里的 `name` 一致。除种子脚本需要 Python 3 之外没有依赖，也没有构建步骤。

## Verify

```bash
python scripts/verify_skill.py     # frontmatter, links, per-section Chinese
python scripts/seed_string.py --count 3
```

`verify_skill.py` also checks that quoted text really appears in the source article and that the figure
index resolves — those two groups are skipped automatically when the article text is not present, which
is the case in this repository (see below).

> 中文：`verify_skill.py` 会检查 frontmatter、内部链接与「每个小节都有中文对照」；引文可溯源与图片存在性两组检查在缺少原文时自动跳过（本仓库正是这种情况）。

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
