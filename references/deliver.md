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

### Where the tell catalog lives ※

Work through the tell categories and fix what applies. A tell is not "ugly" — it is *the default*, the
choice the model would make for anyone. Each one you keep should be a deliberate decision you can
defend, not an omission.

If the `antislop` skill family is installed, that catalog is already maintained there and this file does
not restate it: load `antislop` (core) with `antislop-ui` (the visual depth) and run them as T7. This
skill's own eight categories are a subset of what they cover, and the sections after this one record the
differences that matter. Antislop is an *optional* source, exactly as it is for the rest of this skill:
when it is not installed, the eight categories below are the whole sweep and the pass still works —
smaller, and missing the traps listed under "What antislop adds" below.

> 中文：把中招的地方按类别逐条改掉。「AI 味」不等于「丑」，它指的是**默认值**，是模型对任何人都会做的那个选择；凡是保留下来的，都要能说清是刻意的决定，而不是漏掉的。本机若装了 `antislop` 系列，这份清单不必由本文件重复维护：调 `antislop`（核心）+ `antislop-ui`（视觉细则）来跑 T7；本 skill 的八个类别是它们的子集，差异记在后面几节。antislop 与全篇一样是**可选**依赖：没装时下面八类就是全部扫描，流程照样能走，只是更小，也少了后面「antislop 补了什么」里那些坑。

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

> 中文：八类覆盖 surface（首屏渐变、辉光色块、满屏玻璃拟态、网格纹理当唯一质感）、color（单一强调色滥用、随机上色、灰阶缺失、超过约三种色相且无系统）、layout（居中双按钮、三张一样的卡片、满屏对称、间距一刀切、只靠装饰分隔线分节）、type（通篇单一字体与字重、默认字距、没有排版想法的大标题、emoji 当图标）、components（统一圆角描边阴影、无理由胶囊徽章、图标堆砌、自研控件不如原生）、imagery（抽象 3D 色块、AI 素材人像、没有主体的纹理、只为占位）、motion（只有滚动淡入、每个元素都在动、没有编排与主次、不响应用户）、structure（为凑页面而存在的功能清单、硬塞的 FAQ／推荐语轮播／logo 条、无意义的「New」与「AI powered」徽章）。

### The purpose test ※

Antislop's mechanism turns on one question, asked before any technique is allowed to stay, and it is the
question this stage should be run with:

> What does this serve? If the only answer is "it looks AI" or "it looks safe", the technique goes or
> gets reworked. If the answer names a hierarchy, identity, or readability goal, it stays — and the
> reason is written down.

The same filter, as a single check on the finished design:

> If the logo and product name were swapped out, would this design still feel unique and have its own
> character?

If the answer is no, the design is still generic. Do not fix that by deleting more; go back to the
direction.

> 中文：判断任何技法留不留，先问一句：**它服务于什么？** 若答案只有「这样看起来像 AI」或「这样比较安全」，就改掉或删掉；若答案指向层级、身份或可读性，就保留，并把理由写下来。整份设计还可以用一个问题收口：**把 logo 与产品名换掉，它是否依然独特、有自己的性格？** 答否则仍然是通用设计。此时不要靠继续删来解决，回到方向上重做。

### What antislop adds ※

> The bullets below summarize the installed `antislop` 3.2.20 and its `antislop-ui`, checked against
> this file's eight categories. Rule numbers are cited so the gap can be re-checked; the loaded skill
> stays authoritative if it and this summary ever disagree.

1. **A purpose test instead of a tell list.** Our table answers "does this look like the default?".
   Antislop answers "what does this serve, and is the reason written down?" (R-31). That turns a list of
   recognised tells into a rule you can apply to patterns nobody has catalogued yet.
2. **A tier that has no exception.** Most tells are defaults that are fine when they serve something.
   Some do not work that way, and antislop keeps them apart: an em dash anywhere in the product's own
   text (R-02), and the accessibility floor — contrast, keyboard reach, visible focus (R-25, R-32).
   Confirmed on the real page rather than asserted, under T3's usual rule.
3. **Dose caps, not bans.** Glass on at most 1-2 elements (R-10), glow as a focus accent on 1-2 (R-13),
   shadow as an elevation marker rather than a default (R-12), the active palette at 2-3 cores plus one
   accent (R-29). "How much before it reads as slop" is the half our table never states.
4. **Tells shaped like an app, not a landing page.** T7 grew out of landing-page before/afters, and the
   defaults an agent reaches for on a signed-in screen are not the same: the sidebar + top bar + four
   stat cards + chart + table shell, chosen before anyone asked what the screen is for; stat cards with
   invented numbers and green deltas; a filler activity feed of invented people; a chart with no
   question to answer; table columns copied from the component instead of the data; empty fields filled
   with `John Doe` / `johndoe@example.com`; empty, loading, and error states that say "No data
   available" and nothing else. Same failure mode as a three-card feature grid, absent from our eight
   categories.

> 中文：上述条目对照的是本机安装的 antislop 3.2.20 与其 antislop-ui，逐条与本文八类比对过。① **用「目的测试」替代清单**：我们的表回答「像不像默认值」，antislop 回答「它服务于什么、理由写下来了吗」（R-31）——于是没被收录进清单的新招式也能判。② **区分「没有例外」的一层**：多数 AI 味是「有目的就可以留」的默认值，但产品自身文案里出现破折号（R-02）、以及无障碍底线（对比度 R-25、键盘可达与可见焦点 R-32）不属于此列；按 T3 的老规矩，要在真实页面上确认，而不是嘴上声称。③ **剂量上限而非禁令**：玻璃拟态最多 1–2 处（R-10），辉光作为焦点强调最多 1–2 处（R-13），阴影只作层级标记而非默认（R-12），色板 2–3 个主色 + 1 个强调色（R-29）——「到多少才算过界」正是我们表里没有的那一半。④ **补齐「应用界面」形态的 AI 味**：T7 源自落地页的前后对比，但登录后页面上模型爱用的默认形状并不相同——没人问过这个页面要干什么就已经摆好的侧栏＋顶栏＋四张统计卡＋图表＋表格；数字与绿色涨跌都在编的统计卡；编造人名与事件的动态流；没有问题要回答的图表；从组件而不是数据长出来的表格列；用 `John Doe`／`johndoe@example.com` 填满的空字段；只会说「No data available」的空／加载／错误态。同一个失败模式，只是换了个形状，我们的八类里没有。

### Removing slop is not the same as designing ※

The purpose test alone leaves a hole. Deleting every default produces the sterile result — flat white,
thin grey borders, one generic font — which is not slop and is not design either. Antislop treats that
outcome as a failure and answers it with positive requirements: declare a Design Read, hold three dials
(ENERGY / RHYTHM / MOTION at 1-3, derived from the direction rather than the mood of the moment), and
keep one focal point per screen, structural whitespace, one deliberate accent, and one repeated identity
motif. When direction is missing entirely, the honest output is labelled *draft without direction* at
ENERGY 1 / RHYTHM 1 / MOTION 1 (R-37): a draft, not a deliverable.

This is the pass's largest gap today. The direction Stage 2 settles on is exactly what those dials derive
from, and nothing here used to say to carry it forward. Read that direction as the dial setting, and
re-read it before the sweep, not after.

> 中文：只做「目的测试」会留下一个洞。把默认值删干净就得到**无菌默认**——平白底、细灰边、一个通用字体——它不算 AI 味，但也不算设计。antislop 把这个结果当作失败，并用正向要求来补：先声明 Design Read，明确三个刻度（ENERGY／RHYTHM／MOTION 取 1–3，由方向推导而不是当下一时的心情），并且每屏一个焦点、留白承担结构、只有一个刻意的强调点、有一个反复出现的身份母题。完全没有方向时，诚实的做法是标注 *draft without direction* 并用 ENERGY 1／RHYTHM 1／MOTION 1（R-37）：那是草稿，不是可交付物。这正是本技法目前最大的缺口：第二阶段「深挖一个方向」产出的正是这些刻度要依据的方向，而本文此前没有说要把它带到这里；请把那个方向读成刻度值，并在扫描**之前**重读一次。

### How to fix, not just flag ※

1. **Name the tell, then make the opposite decision explicit.** "Remove the glow" is weaker than
   "hierarchy comes from spacing and type scale; no glow anywhere".
2. **Replace rather than delete where the element had a real job** — an image whose job was "subject
   matter" becomes a generated image, not nothing.
3. **Collapse the system.** Fewer colors, fewer sizes, fewer radii. A tight scale reads as intent.
4. **Borrow from a real reference.** Pick a design you admire and ask what *it* would do here — that is
   the same move as the critic's "how would a top studio execute this aesthetic".
5. **Write the reason for every surviving decision, one line each.** For each color, layout, type, and
   spacing choice that stays, say why it is there (R-31). A decision whose reason cannot be written in
   one line is not a decision; it is the default wearing a justification.
6. **Ask the critic again.** Tells are exactly what the critic is instructed to penalize, so re-run the
   T3 loop after the sweep and let the score confirm the result. Then run antislop's Delivery Gate and
   report it as that gate requires: one line per item, every PASS backed by concrete evidence. A report
   containing a FAIL is not delivered.

> 中文：① 说清「不做这个」，再给出替代的明确决策（「层级由间距与字阶承担，全站不用发光」强于「去掉发光」）。② 有实际职责的元素换掉而不是删掉。③ 收窄色板与尺寸阶梯，紧的尺度读起来就是刻意。④ 找一个真实参照，问它在这里会怎么做（与评审那句「顶级工作室会怎么做」同一动作）。⑤ 为每个留下的颜色、布局、字体、间距决定各写一行理由（R-31）：写不出一行理由的决定不是决定，只是穿了理由外衣的默认值。⑥ 重跑 T3 评审——AI 味正是评审被要求扣分的对象——并让分数确认结果；然后跑 antislop 的 Delivery Gate，按其要求逐条报出：每项一行，每个 PASS 都要有具体证据。报告里出现 FAIL 就不算交付。

### Copy tells are the user's call ※

Copy tells — the em dash, a buzzword, a number nobody supplied — are reported, never silently
rewritten. T8 below makes the copy the user's property, and that rule outranks convenience here: take
the tell to the user with the specific line named, and let them decide. Silently "improving" a supplied
string is the same failure as inventing one. The em-dash rule applies to the product's copy; this file's
own prose is documentation, not shipped text.

> 中文：文案上的 AI 味——破折号、空泛营销词、没人给过的数字——只**报告**，绝不悄悄改写。下面 T8 把文案的所有权判给用户，这条在这里优先于省事：指出具体是哪一行，交给用户决定。擅自「优化」用户给的字符串，与凭空编造是同一个错误。破折号那条管的是**产品文案**，本文件自己的正文是文档，不是要交付的文字。

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
- [ ] ※ Every surviving color, layout, type, and spacing decision has its one-line reason written down.
- [ ] ※ Not sterile: the dials are explicit, there is one focal point per screen, one deliberate accent,
      and one repeated identity motif — not just an absence of tells.
- [ ] ※ If `antislop` is installed, its Delivery Gate was run and reported item by item, with evidence
      behind every PASS and no FAIL left in the report.
- [ ] The copy on the page came from the user's copy deck, unchanged, not generated. ※ Copy tells found
      in that deck were reported to the user, not silently rewritten.
- [ ] No gradients, glows, or containers that exist only to make the design feel fuller.
- [ ] Native/platform components are used wherever they are better than a custom build.
- [ ] The design has been verified in the browser. ※ At real viewport sizes, with the states — hover,
      open, empty, error — checked too.
- [ ] ※ A fresh critic, shown only a screenshot, still scores it ≥ 9/10 after the cuts.

> 中文：出口条件——屏上每个元素都有一行职责说明；AI 味清单已按类别扫过，留下的每一条都是可辩护的刻意决策；每个留下的颜色／布局／字体／间距决定都写了单行理由；结果**不是无菌默认**（刻度明确、每屏一个焦点、一个刻意的强调点、一个反复出现的身份母题，而不只是「没有 AI 味」）；装了 antislop 的话，其 Delivery Gate 已逐条跑过并报出，每个 PASS 都有证据、报告里没有 FAIL；页面文案来自人写的文案清单且已明确禁止 agent 改写，清单里发现的 AI 味是**报告**给用户而不是悄悄改掉；没有只为「填满」而存在的渐变、辉光与容器；平台原生控件优于自研的地方就用原生；真实视口、全部状态已在浏览器验证；删减之后再让独立评审只看截图评一次，仍 ≥9/10。
