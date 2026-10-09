# Prompt library

Copy, adapt, run. Prompts from the source article are quoted verbatim and marked **source**; the rest are
templates this skill adds so the process runs without re-inventing wording. ※ Anything a `※` introduces
is this skill's addition, not the article's text. Replace `{PLACEHOLDERS}` and substitute your own
strongest model where a model name appears — the role matters, the product name does not. Never translate
a prompt you are about to run: the models were tuned on English prompts.

> 中文：提示词库。标 **source** 的是原文逐字引用，其余是本 skill 为让流程可跑通而补的模板；凡 `※` 引出的内容都是本 skill 补的，不是原文。替换占位符，模型名换成你当下最强／最合适的那一个。要执行的提示词不要翻译。

## 1. Direction injection — seed string (Discover, T1) — **source**

```
I want you to build me a landing page for {PRODUCT}.
Follow this procedure:
- Generate a long, random alphanumeric string using a shell script.
- Define the creative direction (color scheme, layout, typography, etc.) based on the string.
  Look beyond the surface for subpatterns, special numbers, anything that inspires you.
- Use your judgment to bring this direction to life and make it look great.
- Don't reveal the string in the design. It's only for your inspiration.
```

※ Give the agent a seed from `scripts/seed_string.py` instead of letting it roll its own when you want to
log and reproduce directions, and run several seeds in parallel for several candidates.

> 中文：※ 想记录并复现方向时，用 `scripts/seed_string.py` 先生成种子交给它；并行跑多个种子＝多个候选方向。

## 2. Direction injection — ambition and taste (Discover, T2) — **source**

```
Build me a landing page for {PRODUCT}, with a bold pixel art theme and stunning graphics.
Each section should feel like a still from a video game, yet somehow it should all function as a
landing page.

Build me a landing page for {PRODUCT}, set in an isometric living 3D city, where different features
are somehow represented by neighborhoods or buildings.

Build me a landing page for {PRODUCT}, with a radically asymmetric layout, dissonant colors and
typography, and uncomfortable negative space. Break all the rules but still make it look good.
```

> 中文：三种「更具体、更大胆」的提示词写法，注意共同结构——一个具体世界＋一条「但仍要能当落地页用」的约束；野心没有约束，出来的就是艺术品而不是页面。

## 3. The three-step ideation system (Discover, T2) — **source** (steps 1 and 3 verbatim; step 2 is a template)

**Step 1 — go broad, not deep**

```
I want to come up with a bold, unique design language for my product. Can you list as many ideas as
you can, with short, high-level descriptions? Go broad, not deep.
```

**Step 2 — react with your taste, then ask it to sharpen**

```
{DIRECTION NAME}:
I'm imagining something {WHAT YOU PICTURE}.
Initially I pictured {WHAT YOU REJECTED}, but this feels {WHY}. Avoid that.
Instead, I want {WHAT TO DO INSTEAD}.
{WHAT WOULD BE BORING} would look boring. {WHAT TO ADD INSTEAD}.
Can you sharpen this one based on my tastes?
```

**Step 3 — turn the direction into a build prompt**

```
Can you write a concise prompt that an AI agent could use to build an initial POC page with this?
```

> 中文：三步选题法——① 让它列大量「只有高层描述、故意不细」的想法，目的是启发你自己；② 用上面的模板说出你脑中的画面、你排斥什么、什么会很无聊、想补什么，再让它据此锐化（② 是模板，① 和 ③ 是原文逐字）；③ 让它把方向写成一条可直接执行的建造提示词。

## 4. The design critic loop (Define, T3) — **source**

```
I want you to improve this design. To figure out what to focus on, use a {CRITIC MODEL} subagent as a
design critic.

Follow this procedure at each iteration:
- Capture a screenshot of the current design.
- Invoke the critic in a fresh context, with just the screenshot, not the code, implementation
  details, or earlier iterations/critiques.
- Ask it to evaluate the aesthetic that the design is going for, imagine how a top design studio
  would execute this aesthetic, then outline the biggest gaps.
- Lastly, it should provide a score out of 10 indicating how close the current design is to that
  studio-level quality bar.

Provide this guidance to the critic in its prompt:
- It should think high-level about the overall structure and composition as well as look at the fine
  details.
- It should watch out for patterns that feel overdone, excessive, or otherwise obviously
  AI-generated, and penalize them.
- It should provide tight, specific feedback, not vague prose.
- It should be bold and opinionated, not rely on what's safe or easy.

Your work is only complete when the critic independently deems it 9/10 or higher. Do not put that
criterion in the critic prompt; keep it objective in its scoring. Use the same critic prompt each time.
```

※ Run it as written: the critic prompt stays identical across iterations, and the 9/10 completion bar
lives only in the implementer's instructions. ※ Accept the result after two consecutive ≥ 9/10 scores.

> 中文：这段就是原文的评审闭环提示词，注意最后三句是核心：门槛只写在执行者这边、评分保持客观、每次迭代用同一份评审提示词。※ 本 skill 补充：要连续两次 ≥9/10 才收工。

## 5. A ready-to-paste critic prompt (Define, T3) — template

Use this as the critic's system/user message. Keep it identical across iterations. Do not mention the
9/10 completion bar here — that belongs in the implementer's instructions.

```
You are a design critic at a top-tier studio. You will receive screenshots of one design in progress.
You do not see its code, its history, or anyone's reasoning, and you do not need to.

1. Name the aesthetic this design is reaching for, in one sentence.
2. Describe how a top design studio would execute that same aesthetic — structure and composition
   first, then the fine details.
3. List the biggest gaps between the two, most important first, specific enough to act on.
4. Penalize anything overdone, excessive, or obviously AI-generated.
5. Score the design out of 10 for how close it is to that studio-level bar.
   Judge against the bar, not against how much effort went into it.

Be bold and opinionated. Tight, specific feedback, not vague prose.
{OPTIONAL: The attached images are references — treat them as a baseline or moodboard, not a target to copy.}
```

**Objective-scoring variant (best per the article):**

```
Here are 5 designs: 4 professional examples and 1 screenshot of our product. Rank them by polish and
taste level.
```

> 中文：这是本 skill 按原文要求写好的评审提示词模板，直接当评审的系统消息用，每轮不要改。※ 模板里刻意不出现 9/10 门槛；附参考图时明确「当基线／情绪板，不是照抄目标」。最后一个变体是原文认为最客观的评分方式。

## 6. Enrich the design with generated images (Define, T4) — **source**

```
The design is pretty plain. Add more personality using image generation. Consider shaders or 3D
effects in combination with images to create more interesting visuals.

For image generation, use this {PROVIDER} API key (only use it locally, do not store it in the code or
product): {KEY}

Verify that your work looks right frame-by-frame in the browser.
```

**Key handling (source, quoted):**

```
Create a gitignored file called .env.agents, store this API key in it, and note to yourself in
AGENTS.md/CLAUDE.md that these keys are for you to use during development (but must not ship with the
product).
```

※ Use a separate key with a tight spend limit, and rotate any key that has been pasted into a chat or a
file that could be shared.

> 中文：让 agent 用图像生成给设计加个性（可与 shader、3D 效果组合），并在浏览器里逐帧核对。密钥放 gitignore 的 `.env.agents`，并在 AGENTS.md/CLAUDE.md 里声明「仅供开发、不得随产品发布」。※ 本 skill 补充：用单独限额的 key，凡粘贴过聊天或可能被分享的文件里的 key 都要轮换。

## 7. Motion from video models (Define, T5) — **source**

**Looping animated graphic, background removed:**

```
Can you replace the image on this page with a looping video clip that does something more interesting?
{WHAT MOVES}.
To get convincing {EFFECT} effects, render the video over the page background colors first (so it bakes
in the refraction effects), then remove the background with a video matting model.
Use this fal.ai API key: {KEY}
Find appropriate recent models for video generation and background removal.
```

**Scroll-scrubbed transition between states:**

```
Build a demo page for {SUBJECT} that uses a video model to create interactive transitions between a
couple of screens. Each screen should show {SUBJECT} in a different state, with vertical motion that
feels appropriate for scrolling:
- Initially, {STATE 1}
- Then {STATE 2}
- Finally {STATE 3}
Generate the initial frame using your image generation skill. Then, generate a video clip that starts
from that frame and animates to the next state. Use the final frame of that video to seed the next
transition so that it continues seamlessly. Scrub through the transitions one by one as the user
scrolls.
Use this fal.ai API key: {KEY}
Use a video model with strong physics and consistency, like {MODEL}.
```

> 中文：两段原文提示词。要点：抠背景前先把动效渲染在页面背景色上（把折射烤进去）；多段过渡必须用上一段的末帧作为下一段起始帧，拼接才无缝。模型用 fal.ai 这类聚合平台让 agent 自己挑。

## 8. Subtraction pass (Deliver, T6) — **source**

```
Simplify the layout into an image-centric grid
Get rid of gradients, glows, and unnecessary containers
Aim for a truly minimalist aesthetic that feels Apple-native
```

※ Same prompt, parameterized for another product:

```
Simplify the layout into {TARGET STRUCTURE}
Get rid of {WHAT TO REMOVE}
Aim for a truly minimalist aesthetic that feels {PLATFORM}-native
```

Precede it with the question that makes the model act: *what really needs to be there?*

> 中文：原文的减法指令（逐字）。※ 下面是同一指令的参数化版本，换产品时用。发这条之前先把那个问句丢给它——「到底哪些东西真的需要存在」。

## 9. AI-tell sweep (Deliver, T7) — template

※ The paywalled section this technique comes from is summarized by the reader as being about removing
AI tells; this prompt is this skill's operationalization of that idea.

```
Review this design as a hostile critic looking only for signs that it was generated by AI. Go category
by category: surface, color, layout, typography, components, imagery, motion, structure.
For each tell you find: name it, say why it reads as machine-made, and state the concrete opposite
decision. Then apply those decisions and re-render.
Keep deliberate exceptions: if a choice is intentional and defensible, say so and leave it.
```

> 中文：※ T7 正文在付费墙后，本提示词是本 skill 对该思路的具体化：让 agent 只挑「像 AI 生成」的证据，逐类别过一遍，每条都要给出「相反的具体决策」再重渲染，并保留能说清理由的刻意例外。

### 9b. Same pass, with antislop installed — template

※ Use this instead of 9 when the `antislop` family is available. It widens the categories to antislop's
catalog, keeps the two questions that make its filter work, names the direction the pass is judged
against, and closes with the gate rather than an impression.

```
Load the antislop core and antislop-ui and run them as the AI-tell sweep on this design.
Judge against this direction: {DESIGN DIRECTION / the Stage 2 brief}. Its dials are ENERGY {1-3} /
RHYTHM {1-3} / MOTION {1-3}; flag anything that contradicts them.
For each tell: name it, cite the rule, say what it serves (or that nothing is served), and state the
concrete opposite decision you are applying. Write one line of reason for every decision that survives.
Report copy tells (em dash, buzzwords, numbers nobody supplied) to me instead of rewriting my strings.
Then answer: if the logo and product name were swapped, would this still feel unique?
Finish with the Delivery Gate as a PASS/FAIL list, one line per item, every PASS backed by evidence.
```

> 中文：※ 装了 antislop 时改用本条替代第 9 条：类别改用 antislop 的完整目录，保留让它的过滤器真正起作用的两个问题（「它服务于什么」「换掉 logo 还独特吗」），把本阶段的方向与三个刻度作为评判基准写进提示词（方向与刻度对抗的内容要标出来），每条 AI 味都要引用规则号并给出相反的明确决策，留下的决定各写一行理由；文案上的 AI 味（破折号、空泛词、没人给过的数字）报告给用户而不是替其改写；最后按 Delivery Gate 逐条给出 PASS／FAIL，每个 PASS 附证据。

## 10. Copy ownership (Deliver, T8) — template

※ T8 is a reader's summary of a paywalled section; this is how an agent should act on it: obtain the
strings, never author them.

```
Here is the copy deck: {FILE}. Use exactly these strings, character for character.
Do not invent, rewrite, shorten, expand, or "improve" any copy. If a string is missing, ask me.
Lay out against the longest real string, not placeholder text.
```

> 中文：※ T8 来自读者口述摘要，本 skill 把它落成 agent 的动作：**向用户要**文案清单，逐字使用，缺了就问，绝不自己写；按最长真实字符串排版。
