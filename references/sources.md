# Sources, coverage, and what this skill added

> 中文：来源、覆盖范围、以及哪些内容是本 skill 自己补的。引用或转述前请先看这张表。

## The article

| | |
|---|---|
| Title | How to turn your AI into a world-class designer |
| Author | **Anshu Chimala** — led software engineering and design teams at Apple for 12 years, focused on research and prototyping for future AI products ([X](https://x.com/anshuc), [Substack](https://substack.com/@anshuc), [LinkedIn](https://www.linkedin.com/in/achimala/)) |
| Published in | [Lenny's Newsletter](https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world) (guest post), page metadata says 2026-09-01 |
| Subtitle | An end-to-end process for tapping into AI's hidden creativity |
| Framework | Loosely inspired by the [Double Diamond](https://en.wikipedia.org/wiki/Double_Diamond_(design_process_model)), reimagined for a team of AI agents instead of human designers |
| Techniques cited | [String Seed of Thought](https://pub.sakana.ai/ssot/) (Sakana AI); model and tool names as of the author's writing (Claude Opus 5, Claude Fable 5, GPT-5.6 Sol, Codex CLI, fal.ai, Seedance 2.5) |

> 中文：文章为 Lenny's Newsletter 的客座文章，作者 Anshu Chimala（Apple 设计与研发团队 12 年，做未来 AI 产品的研究与原型）；框架受 Double Diamond 启发。文中提到的模型与工具名是作者写作时的版本。

## How this skill was built / 本 skill 是怎么来的

The article is paywalled. This skill was built from the free preview — the intro, the three-stage
framework, and Techniques 1 through 6 in full, including their prompts — plus a reader's one-line
summary of the two sections that sit behind the paywall.

The free preview ends mid-article, at the heading **“Technique 7: Remove AI tells”**. Nothing after that
heading was available while writing this skill.

> 中文：文章有付费墙。本 skill 依据免费预览部分（引言、三阶段框架、Technique 1–6 全含提示词）加上读者对付费墙后两节的一句话摘要写成。预览在「Technique 7: Remove AI tells」这个标题处结束，之后的内容在写作时拿不到。

## Coverage / 覆盖范围

| Part of the article | Status in this skill |
|---|---|
| Intro: why models produce generic design; the three-stage framework; the process comes from managing human designers | Verbatim from the free preview |
| Technique 1 — seed strings | Verbatim, including the prompt |
| Technique 2 — ambitious prompts + the three-step ideation system | Verbatim, including all example prompts |
| Technique 3 — critic subagent loop | Verbatim, including the prompt, the criteria ladder, example images, stopping rules, model choice |
| Technique 4 — image generation | Verbatim, including the prompt and the key-handling instruction |
| Technique 5 — video generation | Verbatim, including both prompts and the fal.ai aggregation point |
| Technique 6 — cut elements that don't add value | Verbatim, including the calorie-tracker case and the three fix instructions |
| Technique 7 — remove AI tells | **Heading only.** The reader's summary: the section is about removing the signs that a design was made by AI. The checklist in `references/deliver.md` is this skill's operationalization, not the author's text |
| Technique 8 — write the copy yourself | **Not in the preview.** The reader's summary: you should write the text that appears on the site yourself. The workflow in `references/deliver.md` is this skill's operationalization |
| The `antislop` skill family (third-party, optional) | **Not from the article.** Where the tell catalog is concerned, Technique 7 defers to the `antislop` core plus `antislop-ui` when they are installed: the purpose test, the rules that allow no exception, the dose caps, the app-shaped tells, and the liveliness dials are theirs, summarized against `antislop` 3.2.20 in `references/deliver.md`. Antislop is a separate project with its own provenance; nothing here is quoted from it at length, and the loaded skill wins if the summary drifts |
| The article's images | **Not redistributed.** The post is image-heavy: before/after pairs for Techniques 3, 4, 5 and 6, three animated demos for Technique 2, and the framework diagram. The index below says what each one shows so you can follow along while reading the original |
| Anything preceded by `※` | Added by this skill to make the process runnable: exit criteria and thresholds, the screenshot workflow, the AI-tell sweep and its antislop integration, the copy-deck workflow, accessibility and asset-weight caveats, seed logging, the loop budget check. `※` marks the text that follows it to the end of that sentence or cell; unmarked text comes from the article |

> 中文：Technique 1–6 与三阶段框架均为原文（免费预览部分）；Technique 7 只有标题、Technique 8 连标题都不在预览里，两者按读者口述摘要补写并已在 `references/deliver.md` 顶部标注。**antislop 系列是第三方可选项，不来自本文**：涉及 AI 味清单时，T7 在本机装有它的情况下以 `antislop` 核心 + `antislop-ui` 为准——目的测试、没有例外的那一层、剂量上限、应用界面形态的 AI 味、活力刻度都出自它，`references/deliver.md` 里针对 3.2.20 做了比对摘要；antislop 有自己的出处，此处不整段引用，摘要若与已加载的 skill 不一致，以 skill 为准。原文的图**未随本仓库分发**（见下方图片索引，了解每张图讲什么）；凡 `※` 之后到该句／该单元结束的内容都是本 skill 补的，其余来自原文。

## Figure index / 图片索引

What the original's figures show, so this skill's text makes sense next to it. All of them live in the
article, not here.

| Where | Shows |
|---|---|
| Intro | Three demos built in a few prompts each: a conversational calorie tracker, a space exploration game, a dynamic landing page |
| Intro | The three-stage framework diagram (Discover → Define → Deliver) |
| T1 | The same landing-page prompt run four ways: the default, "make every decision completely at random", and the seed-string version — the seed-string one is visibly the most varied |
| T2 | The three ambitious directions in motion: pixel-art, isometric 3D city, radically asymmetric |
| T2, steps 1–3 | The ideation system: a list of high-level ideas, then the industrial-control-panel direction, then the build prompt the model wrote |
| Define | Seed-string results that still lean on stale patterns — text left, CTA below, nav bar top, graphic right |
| T3 | The critic loop's before/after: what self-review produced versus what a blind critic pushed it to |
| T4 | Before/after pairs showing what image generation adds over gradients and shapes |
| T5 | The glassy looping animation, and the scroll-scrubbed suitcase transition between states |
| T6 | The calorie app before and after the subtraction pass — the article's clearest example of removal as polish |

> 中文：上表说明原文每张图讲什么，便于对照阅读——图本身在原文里，不在本仓库。T6 的「减法前／后」对比最值得亲眼看一次。

## Attribution and limits / 署名与边界

- This skill is an independent derivative work. It is not endorsed by the author or by Lenny's
  Newsletter.
- Quoted prompts are short excerpts, attributed, and included because the skill is unusable without
  them. The full article is paywalled: read it, don't substitute this for it.
- Model and tool names in the prompts are the author's at the time of writing. Substitute your current
  strongest "taste" model for the critic role and a fast, cheap model for the implementer; the roles are
  what matter.
- If you obtain the missing sections, extend `references/deliver.md`: replace the coverage note at the
  top of Technique 7 and Technique 8 with the original text and update this table.

> 中文：本 skill 是独立衍生物，未经作者或 Lenny's Newsletter 背书；引用的提示词是带署名的短摘录，没有它们这个 skill 无法使用；原文有付费墙，请去读原文而不是用本 skill 替代它；提示词里的模型名请替换为你当下最合适的那一个；如果拿到缺失章节，请补进 `references/deliver.md` 并更新本表。
