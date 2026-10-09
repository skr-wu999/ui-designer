# Discover — explore the space of possibilities

Stage 1 of 3. Goal: a wide set of **bold, genuinely different** directions, plus a written brief and a
rendered first pass for each one. Depth comes later; this stage is about breadth.

> 中文：第一阶段。目标是拿到一组**大胆且真正不同**的方向，每个方向配一段设计简报和第一版渲染。这个阶段只管广度，深度留到 Define。

## Why the model needs help here / 为什么这一步要外部帮忙

Told to design the same thing, a model returns the same thing: purplish gradient, text on the left,
graphic on the right, nav bar on top. Told to be random, it returns tokens that *sound* random and
are not — the same palette, the same structure, even the same metaphors. A model can only predict the
most likely next token; it cannot act randomly. Variety has to come from outside it.

> 中文：同一个提示词，模型给出的永远是同一套东西：紫渐变、左文右图、顶部导航。让它「完全随机」也没用——它生成的是听起来随机、其实不随机的词，配色、结构甚至比喻都一样。模型只能预测最可能的 token，随机性必须从外部注入。

## Technique 1 — Use seed strings to inject variety

**Mechanism.** Generate a random alphanumeric string, hand it to the model, and ask it to derive the
creative direction — colors, layout, typography — from patterns it finds in that string. The model is
not making a random choice; it is *interpreting* an input that happens to be random. The string is
inspiration only and must not appear in the design.

The technique is based on **String Seed of Thought (SSOT)**, published by Sakana AI
(<https://pub.sakana.ai/ssot/>).

Run the generator (from the skill directory, or with the absolute path to the script — it has no
dependency on the current working directory):

```bash
python scripts/seed_string.py            # 40 characters
python scripts/seed_string.py --length 64
```

**Verbatim prompt from the article:**

> I want you to build me a landing page for my productivity app.
>
> Follow this procedure:
> – Generate a long, random alphanumeric string using a shell script.
> – Define the creative direction (color scheme, layout, typography, etc.) based on the string. Look beyond the surface for subpatterns, special numbers, anything that inspires you.
> – Use your judgment to bring this direction to life and make it look great.
> – Don't reveal the string in the design. It's only for your inspiration.

**How to run it ※**

- One seed = one direction. Run several seeds (three to five) in parallel, each in its own context, to
  get several directions to choose from.
- Log the seed next to the direction it produced. If you later want that direction back, the log lets
  you reproduce it instead of re-rolling and hoping.
- Strip the seed out of the final artifact — the brief should read as a design direction, not as
  "here is what my random string said".
- Do not let the model see a *previous* direction's seed; each run must be blind to the others.
- The seed governs the look, not the content. Facts, product copy, and structure stay the human's.

> 中文：一个种子＝一个方向。并行跑 3–5 个种子（各自独立上下文）拿到多个候选；把种子号和它产出的方向记在一起，方便复现；最终产物里不能出现种子字符串，简报要读起来像设计方向而不是「我的随机串说了什么」；每个方向互相盲跑；种子只管「长相」，内容、文案和结构仍归人。

## Technique 2 — Be much more ambitious with your prompts

The second injection method is your own taste. Instead of asking the model to invent a direction,
name a specific, vivid inspiration — a video game, an interior design trend, an art installation — and
describe how it should shape the output. This gives the model a clear vision to base decisions on
rather than letting it pick the safe default at each step.

**Examples from the article:**

> "Build me a landing page for my productivity app, with a bold pixel art theme and stunning graphics.
> Each section should feel like a still from a video game, yet somehow it should all function as a
> landing page."

> "Build me a landing page for my productivity app, set in an isometric living 3D city, where
> different features are somehow represented by neighborhoods or buildings."

> "Build me a landing page for my productivity app, with a radically asymmetric layout, dissonant
> colors and typography, and uncomfortable negative space. Break all the rules but still make it look
> good."

Note the shape of these: a specific world, plus an explicit constraint that it still has to work as
the thing you asked for. Ambition without the constraint produces art, not a page.

> 中文：第二种注入方式是你自己的品味：说出一个具体、有画面的灵感来源（电子游戏、室内设计潮流、装置艺术），并说明它该怎么影响产出。注意上面三条提示词的共同结构——一个具体的世界＋一条「但仍然要能当落地页用」的约束；只有野心没有约束，出来的就是艺术品而不是页面。

### The three-step system for finding unique directions

**Step 1 — Ask for many ideas, intentionally lacking detail.** The goal is to spark your imagination,
not to get a usable specification.

> I want to come up with a bold, unique design language for my product. Can you list as many ideas as
> you can, with short, high-level descriptions? Go broad, not deep.

**Step 2 — Visualize your favorites and report your reactions, then ask for refinement.** Say what you
picture, what feels wrong, and what would be boring. The article's example:

> Industrial Control Panel:
> I'm imagining something tactile. Clicky, satisfying buttons, nice sounds.
> Initially I pictured something cartoony or skeuomorphic, but this feels tacky to me. Avoid that.
> Instead, want consistent components and little touches that land this look without going overboard.
> Gray gradients would look boring. Need more texture. Maybe we can incorporate some color, while
> retaining the control panel feel?
> Can you sharpen this one based on my tastes?

This is the part most people skip: the model cannot guess your taste, so state it as reactions —
*this is what I picture · this is what it must not become · this is what would be boring · this is
what to add*. Those four moves are what turn an average idea into one only you would have asked for.

**Step 3 — Iterate until satisfied, then have the model write the build prompt.**

> Can you write a concise prompt that an AI agent could use to build an initial POC page with this?

Keep the written prompt — it is the brief you carry into Define, and it is reusable across projects.

> 中文：三步法——① 让它列大量「只有高层描述、故意不细」的想法，目的是启发你自己；② 挑出你最有感觉的几个，说出你脑中的画面、你排斥什么、什么会很无聊、想补什么，再让它据此锐化；③ 满意后让它把方向写成一条可直接执行的建造提示词，这条提示词就是进入 Define 的简报。

## Rules that keep this stage honest / 让这一步有效的规则

- **Don't be afraid to try ideas that sound terrible.** If you catch yourself thinking "there's no way
  this will work", you are on the right track — that is the edge of the model's comfort zone. If it
  fails, throw the result away and try something else.
- **Save the prompts that don't work** and retest them when a newer model ships. That is how you learn
  what the current models can actually do.
- **Pasting model-generated ideas back into the model gets you nothing unique** — anyone else could do
  the same. Value comes from actively steering the direction.
- ※ **Judge only after rendering.** A direction that reads dull in a paragraph can be striking on
  screen, and vice versa.

> 中文：不要怕试「听起来很糟」的想法——「这不可能成」往往说明你正踩在模型的舒适区边界上；失败就丢掉重来。不成功的提示词要存下来，等新模型发布再试。把模型生成的点子再喂回模型，得不到独特结果，因为别人也能这么做；独特性来自你主动掌舵。方向一定要渲染出来再判断。

## Exit checklist / 阶段出口自检

- [ ] ※ At least three directions survived, each with a written brief: aesthetic, three feeling words,
      what to avoid, one reference.
- [ ] Each surviving direction has been rendered, not just described.
- [ ] The directions differ in structure and idea — not just in color.
- [ ] Each brief can be handed to a fresh agent and produce approximately that direction again.
- [ ] Failed directions and their prompts are logged for a later model generation.

> 中文：出口条件——至少三个方向存活且各有简报（美学／三个关键词／禁忌／一个参照）；每个都渲染过；差异在结构与点子层面而非配色；简报交给新 agent 能大致复现该方向；失败方向与提示词已归档待新模型重试。

Next: `references/define.md` — take one direction and give it an identity.
