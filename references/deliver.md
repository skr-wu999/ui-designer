# Deliver — polish your design into something users will love

Stage 3 of 3. Goal: the design survives contact with real use. AI can build amazing, striking visuals;
your judgment is what makes sure the design makes sense, flows well, and serves its practical purpose.

> 中文：第三阶段。目标是让设计经得起真实使用。AI 能做出惊艳的画面，但「讲得通、用得顺、真正解决问题」靠的是你的判断。

## Technique 6 — Cut out elements that don't add value

**The asymmetry.** AI loves to add more and rarely takes away. One of the biggest signs that a design is
AI-generated is that it overexplains everything or contains elements that serve no practical purpose. By
contrast, a design that exercises restraint immediately looks premium and tasteful.

**In practice.** When polishing AI designs, most of the effort goes into removing things.

**Worked example from the article — a calorie-tracking app.**

The author described the app's functionality and explicitly asked for a "clean, minimalist design". The
result was impressive for being fully AI-generated, but a lot in it was not adding value:

- Pink glowy effects in the background and on the progress bar
- Random colors and highlights on text
- Extra labels and empty space when displaying all the foods for a day, when the images already
  communicate this
- Custom buttons and text fields that look worse than built-in iOS components

**The instruction that fixed it (verbatim):**

> – Simplify the layout into an image-centric grid
> – Get rid of gradients, glows, and unnecessary containers
> – Aim for a truly minimalist aesthetic that feels Apple-native

**Why it worked.** It is opinionated, lets the visuals speak for themselves, uses native iOS components,
and drops the excess color and gradients; the text is smaller, simpler, tighter.

**The lesson.** Today's models would not make these choices on their own: AI does not like to take
risks, and it is risky to strip down a design and delete code. The model needs a push from you. Look
over the design and ask what really needs to be there. Putting less on the screen often communicates
more, because you hold attention without drowning it in clutter.

**How to run the pass ※**

1. List every element and its job in one line. "Looks nice" is not a job.
2. Delete or merge anything whose job is decoration, reassurance, or explanation of something already
   visible.
3. Prefer the platform's native components over custom ones unless the custom one is a deliberate,
   defensible design decision.
4. Count your colors, type sizes, radii, shadows, and spacings. If any category has a value that exists
   in exactly one place, ask whether it earns the exception.
5. Re-render and look again. Deletion usually exposes hierarchy problems that were hidden by noise.

> 中文：AI 只爱加不爱减，「解释过度」和「没用的元素」是最强的 AI 味信号；克制的设计一看起来就贵。原文案例：作者明确要了「clean, minimalist」，结果里仍有粉色辉光（背景与进度条）、文字上的随机颜色与高亮、图片已经说明问题却还加的标签与空白、比 iOS 原生控件更丑的自定义按钮与输入框；他用上面三条指令把布局简化成以图为主的网格、去掉渐变辉光与多余容器、追求 Apple 原生的极简感，结果明显更好。要点：模型不会主动做「删除」这种有风险的选择，必须由你推它。补充的可执行做法：逐个元素写出它的一条职责（「好看」不算职责）→ 删掉或合并纯装饰／纯安慰／重复解释的元素 → 除非是刻意的设计决策，否则优先用平台原生控件 → 数一数颜色、字号、圆角、阴影、间距的取值，只出现一次的那个值要能说出理由 → 重新渲染再看，删除通常会暴露出被噪音掩盖的层级问题。

## Technique 7 — Remove AI tells

> **Coverage note.** The body of this technique sits behind the publication's paywall and was not in the
> saved page. The reader's summary: *the section is about removing the signs that a design was made by
> AI.* Everything below the line is **this skill's operationalization** of that idea — not the original
> author's text. Treat it as a checklist to apply, and prefer the actual section if you can read it.

> 中文：本节正文在付费墙之后，保存的页面里没有。读者的口述摘要是：这一段讲**消除 AI 味**。下面清单是本 skill 对这条思路的具体化，不是原文。

### The sweep ※

Work through the tell categories and fix what applies. A tell is not "ugly" — it is *the default*, the
choice the model would make for anyone. Each one you keep should be a deliberate decision you can
defend, not an omission.

> 中文：按下面的类别逐条扫，把中招的地方改掉。「AI 味」不等于「丑」——它指的是**默认值**，是模型对任何人都会做的那个选择；凡是保留下来的，都要能说清是刻意的决定，而不是漏掉的。

| Category | Tells |
|---|---|
| Surface | Purple/indigo gradient hero · glow blobs behind content · glassmorphism on everything · mesh gradients as the only texture |
| Color | A single accent used for every emphasis · accent-colored random words · near-black on near-white with no middle · more than ~3 hues with no system |
| Layout | Centered hero with two buttons · three identical feature cards · everything symmetric · uniform padding everywhere so nothing leads · sections separated by decorative dividers only |
| Type | One typeface for the whole page · uniform weights · default letter-spacing · a huge heading with no typographic idea · emoji standing in for icons |
| Components | One radius, one border, one shadow applied to everything · pill badges for no reason · icon soup · inputs and buttons worse than the platform's native ones |
| Imagery | Abstract 3D blobs · generic AI "stock" people · texture with no subject · images that only fill space |
| Motion | Only fade/slide-in on scroll · every element animated · no choreography or hierarchy · motion that does not respond to the user |
| Structure | Feature lists that exist to fill a page · bolted-on FAQ, testimonial carousel, logo strip · badges like "New" and "AI-powered" with no meaning |

### How to fix, not just flag ※

1. **Name the tell, then make the opposite decision explicit.** "Remove the glow" is weaker than
   "hierarchy comes from spacing and type scale; no glow anywhere".
2. **Replace rather than delete where the element had a real job** — an image whose job was "subject
   matter" becomes a generated image, not nothing.
3. **Collapse the system.** Fewer colors, fewer sizes, fewer radii. A tight scale reads as intent.
4. **Borrow from a real reference.** Pick a design you admire and ask what *it* would do here — that is
   the same move as the critic's "how would a top studio execute this aesthetic".
5. **Ask the critic again.** Tells are exactly what the critic is instructed to penalize, so re-run the
   T3 loop after the sweep and let the score confirm the result.

> 中文：清单按类别列了常见 AI 味信号（紫蓝渐变首屏、辉光色块、满屏玻璃拟态、单一强调色滥用、居中双按钮、三张一样的卡片、通篇同一字体与字重、统一圆角描边、抽象 3D 素材、只会淡入的动效、为凑页面而存在的功能清单等）。修法：先说清「不做这个」，再给出替代的明确决策（例如「层级由间距与字阶承担，全站不用发光」）；有实际职责的元素换掉而不是删掉；收窄色板与尺寸阶梯；找一个真实参照问它在这里会怎么做；最后重跑 T3 评审，因为「AI 味」正是评审被要求扣分的对象。

## Technique 8 — Write the copy on the site yourself

> **Coverage note.** Also behind the paywall. The reader's summary: *the section says you should write
> the text that appears on the site yourself.* Everything below is **this skill's operationalization**.

> 中文：同样在付费墙之后。读者口述摘要：**网站上的文案要自己写**。下面是本 skill 的具体化。

**Why.** The same token-prediction problem that flattens layout also flattens language. Asking the
model for copy yields the average of every landing page it has read: superlatives, abstractions, and
the same three verbs. Layout can carry a design a long way, but the words are what the user actually
reads — and they are the cheapest place to sound like everyone else.

**How to run it ※**

The agent's job here is to *obtain* the copy, never to author it. If you are the agent:

1. **Ask the user for a copy deck** — a plain file with the headline, subhead, value proposition, each
   feature name and its one-line description, every button label, and the empty, loading and error
   strings.
2. **If the user has no copy yet, stop and ask for it.** Do not write it yourself, do not paraphrase a
   draft into something "better", and do not fill gaps with plausible marketing text.
3. **Hand the deck to the implementer as fixed text:** "Use exactly these strings. Do not invent,
   rewrite, shorten, or add copy. If a string is missing, ask me."
4. **Design against the real strings.** No lorem ipsum, no placeholder marketing text. Lay out with the
   longest real string and check the shortest.
5. **Offer mechanical help only** — terminology consistency, character counts, capitalisation, alt text,
   translation drafts, typo scans — and flag every touch for the user to approve.
6. **Ask the user to read it out loud.** Where the reading stumbles, the sentence needs rewriting, not
   the layout.

If you are the human: those six points are your checklist — concrete nouns, contractions, one idea per
sentence, no invented metrics, no superlatives you cannot defend.

> 中文：让模型写文案，得到的就是它读过所有落地页的平均值——最高级、最抽象、同样的几个动词。做法：先写一份纯文本文案清单（标题、副标题、价值主张、每个功能名＋一句话、所有按钮文案、空态／加载／错误态文案），用「严格使用这些字符串，不许自创、改写、压缩或增补，缺了就来问我」的方式交给 agent；用真实文案排版（禁止 lorem ipsum，用最长字符串试版式），不写没人能兑现的最高级；把页面从头读一遍，卡住的地方改句子而不是改版式；agent 只做机械活（术语一致性、字数、大小写、alt 文本、翻译初稿）且必须复核。

## Exit checklist / 阶段出口自检

- [ ] Every element on screen has a one-line job. Anything that only decorates or explains was cut.
- [ ] ※ The AI-tell sweep has been run category by category, and each surviving tell is a deliberate,
      defensible decision.
- [ ] The copy on the page came from the user's copy deck, unchanged, not generated.
- [ ] No gradients, glows, or containers that exist only to make the design feel fuller.
- [ ] Native/platform components are used wherever they are better than a custom build.
- [ ] The design has been verified in the browser. ※ At real viewport sizes, with the states — hover,
      open, empty, error — checked too.
- [ ] ※ A fresh critic, shown only a screenshot, still scores it ≥ 9/10 after the cuts.

> 中文：出口条件——屏上每个元素都有一行职责说明；AI 味清单已按类别扫过，留下的每一条都是可辩护的刻意决策；页面文案来自人写的文案清单且已明确禁止 agent 改写；没有只为「填满」而存在的渐变、辉光与容器；平台原生控件优于自研的地方就用原生；真实视口、全部状态已在浏览器验证；删减之后再让独立评审只看截图评一次，仍 ≥9/10。
