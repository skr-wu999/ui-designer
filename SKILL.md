---
name: ui-designer
description: "Run the Discover → Define → Deliver process that gets distinctive, world-class design out of an AI agent instead of generic slop. Use when building or redesigning any interface, landing page, app screen, deck, poster, or prototype and visual quality matters; when an AI-generated design looks bland, repetitive, or obviously AI-made; when the user asks for a bold, unique, or ambitious direction; or when they ask to make something 'look designed'. 中文：用 Discover → Define → Deliver 三阶段流程，把 AI 默认产出的平庸设计变成有辨识度的好设计。任何界面／落地页／应用页面／幻灯片／海报／原型的制作或改版，只要视觉质量重要，或 AI 生成的结果显得平庸、雷同、有「AI 味」，或用户要求更大胆、更独特的方向时使用。"
allowed-tools: Read Write Edit Glob Grep Bash(python *) Bash(node *) Bash(npx *)
---

# UI Designer — Discover → Define → Deliver

> **Language convention.** English lines are the instructions you follow. Each `中文：` blockquote
> explains the same content in Chinese. Prompts, code, and tool names stay in their original form —
> never translate a prompt you are about to run.
>
> **中文：** 本文件英文部分是执行指令，紧跟的 `中文：` 引用块是同一内容的中文对照。提示词、代码、工具名保持原样，不要翻译要执行的提示词。
>
> **`※` marker.** `※` marks the text that follows it, up to the end of that sentence or table cell, as
> something this skill adds to make the process runnable — not the source article's text. Anything with
> no `※` in front of it comes from the article. The same applies to `※` items in `references/`.
> See `references/sources.md`.
>
> **中文：** `※` 标记的是它之后、到该句（或该表格单元）结束为止的内容，表示这是本 skill 为了流程可执行而补充的，不是原文；没有 `※` 的内容来自原文，`references/` 里的 `※` 同理。来源与缺口见 `references/sources.md`。

## When to use this / 何时使用

Use it when a design decision has to be *made*, not just implemented:

- Building an interface, page, screen, deck, poster, or prototype from scratch.
- Redesigning something that "works but looks like every AI-built site".
- A first AI draft exists and it needs to become distinctive.
- The user asks for bold, unusual, high-craft, "not obviously AI" output.

Don't use it for pure implementation work — wiring an existing, already-designed component,
fixing a bug, or writing a spec with no visual surface.

> 中文：当需要「做设计决策」时用它——从零做界面／页面／幻灯片／海报／原型；把「能用但一看就是 AI 做的」东西改版；已经有第一版 AI 稿要变成有辨识度的作品；用户要求大胆、独特、高完成度或「不要 AI 味」。纯粹的实现类工作（照已有设计接线、修 bug、写没有视觉产出的规格）不用它。

## The failure this process fixes / 它解决的问题

LLMs predict the most likely next token. At every design decision — which color, where the element
goes — the model picks the choice it thinks will please the most people. The result is
design-by-committee: purple gradients, text left, graphic right, the same structure every time.

Great design is the opposite: it starts with feeling, aims at an emotional response, bends the rules,
and delights with memorable, unexpected choices. The model cannot reach that on its own, because
reaching it means *not* making the predictable choice.

So the gap is not model capability — it is **process**. The process below pushes a team of AI agents
past its defaults, then polishes the result to a studio level of quality.

> 中文：大模型逐 token 预测最可能的下一个词。每到设计决策点（用什么颜色、元素放哪），它都选「最能讨好所有人」的那个，于是产出设计委员会式的平均结果：紫色渐变、左文右图、结构雷同。好设计恰恰相反——从感受出发、追求情绪反应、打破规则、用出人意料的选择打动人。模型自己到不了那里，因为那意味着「不做最可能的那个选择」。所以差距不在模型能力，而在**流程**。下面的流程把 AI 智能体推离默认值，再把结果打磨到工作室级完成度。

## The three stages / 三阶段

| Stage | Goal | Exit criteria | Techniques |
|---|---|---|---|
| **Discover** | Explore the space of possibilities | ※ at least 3 genuinely different directions, each with a written design brief and a rendered first pass | T1 seed strings, T2 ambitious prompts |
| **Define** | Give one direction an individual identity | the design critic, in a fresh context seeing only a screenshot, independently scores it ≥ 9/10 — ※ twice in a row, with the same critic prompt | T3 critic loop, T4 image generation, T5 video generation |
| **Deliver** | Make it production-ready and loved | subtraction pass done; ※ AI tells gone (T7 is a reader's summary of a paywalled section); ※ copy supplied by the user, never generated; verified in the browser | T6 subtract, T7 remove AI tells, T8 write the copy yourself |

Run them in order, and do not skip a stage because the first draft "looks fine": initial AI designs
usually still feel generic.

> 中文：顺序执行，不要因为第一版「看着还行」就跳过阶段——AI 的第一版设计通常仍然是通用的。Discover 探索可能性，Define 给一个方向立起个性，Deliver 打磨到可交付。

## Operating rules / 铁律

1. **Never accept the first output.** The first render is the model's average. Treat it as raw material.
   中文：第一版只是原料，不是成品。
2. **Vary from outside the model.** The model cannot act randomly or break its own patterns, so inject
   variety through a seed string or through your own taste (T1, T2).
   中文：变化必须从模型外部注入。
3. **Judge the picture, not the code.** Screenshot the result and look at it. Never call a design good
   because the code looks clean.
   中文：看截图判断，不靠读代码。
4. **The critic is separate, blind, and consistent.** A fresh context, a screenshot only — no code, no
   implementation notes, no earlier critiques — and the *same* critic prompt every iteration (T3).
   中文：评审必须另起上下文、只看截图、每次用同一份提示词。
5. **The ≥ 9/10 bar belongs to the implementer, never to the critic.** Say "your work is complete when
   the critic independently deems it 9/10 or higher" in the worker's prompt, and keep the critic's own
   scoring objective. 中文：门槛写在执行者那边，不能污染评审的评分标准。
6. **Spend taste, not tokens.** The critic can be a big, expensive model because it makes only
   executive decisions — in the article's runs it used under 10% of output tokens — while a cheaper,
   faster model does the labor. 中文：大模型管品味，小模型干苦力。
7. **Subtract before you add.** Most polishing effort goes into removing things. A design that shows
   restraint reads premium (T6). 中文：打磨的主要动作是删。
8. **The user writes the words; the agent asks for them.** The human writes the copy that ships and the
   agent designs around it. ※ Ask for the copy deck and use it verbatim; never invent, paraphrase or
   "improve" strings, and if no copy exists yet, stop and ask rather than writing it yourself.
   (T8 comes from a reader's summary of the paywalled section, not from text this skill could read.)
   中文：上线文案由人写、agent 围着它做设计；agent 要做的是**向用户索要**文案清单并逐字使用，绝不自己编、改写或「润色」，拿不到文案就停下来问。※ T8 来自读者对付费墙章节的口述摘要，不是本 skill 能读到的原文。
9. **Keep the prompts that failed.** Retest them when a newer model lands — that is how you find out
   what the current models can actually do. 中文：失败提示词留着，等新模型再试。

## Stage 1 — Discover: explore the space of possibilities

Goal: wide, bold, varied directions — not one tasteful safe one.

Do this:

1. Pick an injection method: a seed string (T1) or a specific, vivid inspiration from your own taste (T2).
2. Produce several directions. ※ Run them in parallel if you can — the source example ran four
   instances of the same agent with the same prompt to expose the default.
3. ※ For each direction, write a one-paragraph brief: the aesthetic in plain words, the three words it
   should feel like, what it must avoid, and one reference.
4. Render each direction before judging it — a first pass, not a finished page.
5. ※ Kill the ones that merely differ in color. Variety means different structure, typography, and
   idea, not a different palette.

Never settle for "make it unique" as a prompt: told to be random, models produce tokens that *sound*
random and are not. Inject real randomness or real taste instead.

Full procedures, exact prompts, and the three-step ideation system: `references/discover.md`.

> 中文：目标是大胆、多样的方向，而不是一个安全好看的方案。做法：选一种注入方式（种子字符串或你自带的具体灵感）→ 同时产出多个方向（能并行就并行，原文就是同一个提示词跑四个实例来暴露默认值）→ 每个方向写一段设计简报（审美、三个关键词、必须避免什么、一个参照）→ 每个方向都渲染出第一版再评判 → 淘汰只换了配色的那些。「给我个独特的」这种提示词无效：模型会生成「听起来随机」但并不随机的选择。

## Stage 2 — Define: deepen the design direction

Goal: the surviving direction stops looking generic and gains its own identity.

The loop (T3):

1. The implementer screenshots the current design.
2. It invokes a **design critic** in a fresh context with *only* the screenshot.
3. The critic names the aesthetic being attempted, imagines how a top studio would execute that
   aesthetic, outlines the biggest gaps, and scores the design out of 10.
4. The implementer fixes the gaps, then repeats.
5. Stop when the critic independently scores ≥ 9/10. ※ Require the score twice in a row so a lucky
   single pass does not end the loop. Cap the loop — the article's advice is one or two iterations
   first, then check convergence before allowing more.

Make the critic's criteria as objective as you can — "rank these 5 designs by polish and taste level,
4 of them professional" beats "judge whether it looks beautiful". Give it example images as a baseline
or moodboard, never as a target to copy.

Then push the visual material beyond code: generate real images for texture, depth, and subject matter
(T4), and use video generation when the design needs motion — looping graphics keyed off their
background, or keyframe-interpolated transitions the user can scroll through (T5).

Critic prompt templates, the criteria ladder, stopping rules, and the image/video wiring options:
`references/define.md`.

> 中文：让存活下来的方向脱离通用感、长出个性。循环：执行者截图 → 在新的上下文里调起「设计评审」，只给它截图（不给代码、实现细节、历史评审）→ 评审说出当前追求的美学、想象顶级工作室会怎么做、指最大差距、打 0–10 分 → 执行者按差距修改再评 → 评审独立给出 ≥9/10 才算完成。评分标准尽量客观（「把这 5 个设计按完成度与品味排序，其中 4 个是专业作品」好过「看它美不美」），参考图当基线／情绪板，而不是照抄目标。视觉素材也要超出代码：用图像生成补质感与主体（T4）；需要动效时用视频生成——抠掉背景的循环动画，或可随滚动拖动的关键帧过渡（T5）。

## Stage 3 — Deliver: polish it into something users will love

Goal: it holds up as a real product, not a demo.

1. **Subtract.** List every element on screen and ask what it is doing. Remove glows, gradients,
   decorative containers, redundant labels, and anything that overexplains. Ask: what really needs
   to be there? (T6)
2. **Hunt AI tells.** ※ Sweep for the signals that read as machine-made — default palette and spacing,
   three identical cards, emoji section bullets, centered hero with two buttons, symmetry everywhere,
   stock-looking imagery, borders and radii applied uniformly, motion that only fades things in.
   `references/deliver.md` has the checklist. **If the antislop family is installed, that pass is T7**:
   load `antislop` with `antislop-ui` and run them as the sweep, which adds the purpose test, the
   rules that allow no exception, the dose caps, the app-shaped tells, and the liveliness dials that
   keep the result from turning sterile — and it ends with antislop's Delivery Gate. Without antislop,
   the eight categories in `references/deliver.md` are the whole pass. Either way: removal is not the
   goal, so re-check the direction before the sweep and report copy tells to the user instead of
   rewriting their strings.
3. **Get the copy from the user.** ※ Ask for the copy deck — headlines, subheads, button labels,
   microcopy, empty and error strings — and use those strings exactly. Never invent, paraphrase,
   shorten, or "improve" copy. If the user has no copy yet, stop and ask for it: writing the words is
   not the agent's job. (T8 is a reader's summary of the paywalled section.)
4. **Verify in the browser, frame by frame.** Click the states, scroll the transitions, check the empty
   and error states, and look at it at real viewport sizes. ※ If you have no way to capture a
   screenshot, use "Getting a screenshot" below — and never claim a visual check you did not perform.
5. **Re-run the blind critic once.** ※ After the cuts, a fresh critic seeing only a screenshot should
   still score ≥ 9/10. Cutting exposes new problems, so this pass is what confirms the deletions helped.
6. **Then stop.** ※ One more round of "adding polish" is usually where restraint gets lost.

> 中文：让它站得住。① 做减法：逐个数屏幕上每个元素在干什么，去掉发光、渐变、装饰性容器、重复标签和一切「解释过度」的东西（T6）。② 清 AI 味：按清单扫一遍默认配色与间距、三张一模一样的卡片、emoji 当小标题、居中大标题加两个按钮、满屏对称、素材图感、统一圆角与描边、只会淡入的动效（T7）；**装了 antislop 系列就用它来跑这一步**——`antislop` + `antislop-ui` 在此之上补了目的测试、没有例外的那一层、剂量上限、应用界面形态的 AI 味，以及防止删成「无菌默认」的活力刻度，并以它的 Delivery Gate 收口；没装则 `references/deliver.md` 的八类就是全部。两种情况都一样：**删不是目的**，扫之前先复核方向，文案里的 AI 味报告给用户而不是替用户改写。③ 向用户索取文案：标题、副标题、按钮、微文案、空态与错误态文案都要用户给，逐字使用，缺了就停下来问，绝不自己编（T8）。④ 在浏览器里逐帧验证：点状态、滚过渡、看空态与错误态、按真实视口看；拿不到截图就用下面的办法，且不要声称做过没做的检查。⑤ 删减之后再让独立评审只看截图评一次：删除会暴露新问题，这一轮用来确认删对了。⑥ 该停就停：再加一轮「精致化」往往正是克制失守的地方。

## Technique index / 技法索引

| # | Technique | Where |
|---|---|---|
| T1 | Seed strings — inject real randomness from outside the model | `references/discover.md` |
| T2 | Be much more ambitious — bring your own taste into the prompt | `references/discover.md` |
| T3 | Positive feedback loops with a critic subagent | `references/define.md` |
| T4 | Image generation to enrich the design | `references/define.md` |
| T5 | Video generation for motion and transitions | `references/define.md` |
| T6 | Cut out elements that don't add value | `references/deliver.md` |
| T7 | Remove AI tells | `references/deliver.md`; the `antislop` + `antislop-ui` skills when installed |
| T8 | Write the copy on the site yourself | `references/deliver.md` |

Ready-to-adapt prompts, including the verbatim ones from the source article: `references/prompt-library.md`.
The `antislop` family is optional: this skill is the process, antislop is the taste filter. It is worth
loading for T7 (remove AI tells) and whenever the design decisions themselves need defending, because it
supplies the purpose test, the rules that allow no exception, the dose caps, and the liveliness dials that
keep a swept design from becoming sterile. `references/deliver.md` says exactly what it adds and how to
run it as part of T7.

> 中文：技法索引与出处见上表；可直接改用的提示词（含原文逐字提示词）在 `references/prompt-library.md`。antislop 系列是**可选**依赖：本 skill 管流程，antislop 管品味过滤。建议在 T7（清 AI 味）以及任何需要为设计决策辩护的时候加载它——它提供目的测试、没有例外的那一层、剂量上限，以及防止清理之后变成「无菌默认」的活力刻度；它到底补了什么、如何在 T7 里配合使用，`references/deliver.md` 写得很具体。

## Getting a screenshot / 怎么拿到截图

Stages 2 and 3 are judged from pictures, so the first task is always to obtain one. Try, in order:

1. The project's own browser test setup (Playwright, Puppeteer, Cypress) if it has one.
2. A one-off headless capture with tooling already on the machine — `npx playwright screenshot <url>
   <file>`, or a small Node/Python script driving an installed browser.
3. Ask the user for a screenshot. This is the fastest and always accurate option, and the only one
   available when the design lives on their machine or behind a login.
4. If none of these works, say so explicitly: report that the design could not be judged visually and
   what is missing. Do not skip the critic silently and do not describe a visual check you did not run.

> 中文：第二、三阶段靠图判断，所以第一件事永远是拿到截图。按顺序试：① 项目自带的浏览器测试（Playwright／Puppeteer／Cypress）；② 用机器上已有的工具做一次性无头截图（`npx playwright screenshot <url> <file>` 或一个小 Node／Python 脚本驱动已装浏览器）；③ 直接向用户要截图——最快也最准，设计在用户机器上或需要登录时这是唯一办法；④ 都不行就明确说出来：报告「无法做视觉判断」以及缺什么，不要偷偷跳过评审，也不要描述你没做过的视觉检查。

## Before you call it done / 交付前自检

- [ ] ※ The direction is identifiable from a screenshot alone — it does not look like the default
      output of the model you used.
- [ ] A critic in a fresh context, seeing only the screenshot, scored it ≥ 9/10 with the same prompt
      used every iteration. ※ Twice.
- [ ] Every element on screen has a job. Anything that only decorates or explains was cut or justified.
- [ ] ※ No remaining AI tells from the checklist in `references/deliver.md`. ※ If `antislop` is
      installed, its Delivery Gate was run on the visual result and reported item by item, and the
      design was checked for the opposite failure too: it is not sterile.
- [ ] ※ The copy on the page came from the user's copy deck, unchanged, not generated.
- [ ] Verified in a browser: real viewport, real interactions, transitions scrubbed. ※ States checked,
      and if no capture was possible, that limitation is reported rather than glossed over.
- [ ] ※ The user can say what it is for, and the design serves that.

> 中文：完成前逐条核对——只看截图就能辨认出这个方向（不是模型默认输出）；新上下文的评审只用截图、每次同一提示词、独立给出 ≥9/10（连两次）；屏上每个元素都有职责；AI 味清单已清（装了 antislop 的话，其 Delivery Gate 已对视觉结果逐条跑过并报出，同时也检查了相反方向的失败——结果不是「无菌默认」）；页面上文案来自用户提供的清单、逐字未改；在浏览器按真实视口与真实交互验证过（含各种状态；若无法截图，如实说明限制而不是含糊过去）；它能说清「这是给谁、为什么」，且设计服务于这个目的。

## Source / 来源

The methodology, techniques, and verbatim prompts in this skill come from **“How to turn your AI into
a world-class designer”** by **Anshu Chimala** (Apple design and engineering lead, 12 years), published
in [Lenny's Newsletter](https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world). The stages
are loosely inspired by the [Double Diamond](https://en.wikipedia.org/wiki/Double_Diamond_(design_process_model))
adapted for a team of AI agents.

Coverage and gaps — which parts are verbatim, which came from a reader's summary, and which are this
skill's additions — are documented in `references/sources.md`, which also indexes the article's figures
and says what each one shows. Read it before attributing anything here to the original author.

> 中文：本 skill 的方法论、技法与逐字提示词出自 **Anshu Chimala**（在 Apple 负责设计与研发团队 12 年）的文章《How to turn your AI into a world-class designer》，发表于 Lenny's Newsletter；三阶段框架受 Double Diamond 启发并改造为面向 AI 智能体团队。哪些是原文、哪些来自读者口述摘要、哪些是本 skill 的补充，以及原文图片的索引与说明，都记在 `references/sources.md` 里。
