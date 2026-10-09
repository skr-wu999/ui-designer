# Define — deepen your design direction

Stage 2 of 3. Goal: the direction you picked in Discover stops looking generic and gains an individual
identity — its own layout logic, typography, material, and motion.

> 中文：第二阶段。目标是让 Discover 里选中的方向脱离通用感，长出个性：自己的版式逻辑、字体、材质与动效。

## Why the first pass still looks generic / 为什么第一版还是通用

However you prompted it, the first AI pass usually falls back on stale patterns: text on the left with
a CTA below, a nav bar on top, a graphic on the right. Technique 1 and 2 got you a *direction*; this
stage is where the direction becomes a *design*.

> 中文：不管前面怎么提示，第一版通常还是会退回老套路：左文＋下方按钮、顶部导航、右侧配图。T1/T2 给的是**方向**，这一阶段才把方向变成**设计**。

## Technique 3 — Create positive feedback loops with subagents

**The problem.** An agent cannot objectively review its own work: it is looking at its own code, its
own earlier decisions, and its own rationale. It cannot zoom out and think differently about what it
already built.

**The fix.** Let a *separate* agent decide whether the design is good enough. The critic looks at
screenshots of the current design and cares nothing about how it was implemented or how much effort it
took — only whether it actually hits the quality bar.

**The bonus.** A big, expensive model can serve as the critic without breaking the bank, because the
critic only makes executive decisions. A cheap, fast model does the grunt work. In the article's runs,
the critic model accounted for **less than 10% of output tokens**; asking that model to redesign the
page directly would have cost twice as much and taken much longer.

**Verbatim prompt from the article:**

> I want you to improve this design. To figure out what to focus on, use a Fable 5 subagent as a design critic.
>
> Follow this procedure at each iteration:
> – Capture a screenshot of the current design.
> – Invoke the critic in a fresh context, with just the screenshot, not the code, implementation details, or earlier iterations/critiques.
> – Ask it to evaluate the aesthetic that the design is going for, imagine how a top design studio would execute this aesthetic, then outline the biggest gaps.
> – Lastly, it should provide a score out of 10 indicating how close the current design is to that studio-level quality bar.
>
> Provide this guidance to the critic in its prompt:
> – It should think high-level about the overall structure and composition as well as look at the fine details.
> – It should watch out for patterns that feel overdone, excessive, or otherwise obviously AI-generated, and penalize them.
> – It should provide tight, specific feedback, not vague prose.
> – It should be bold and opinionated, not rely on what's safe or easy.
>
> Your work is only complete when the critic independently deems it 9/10 or higher. Do not put that criterion in the critic prompt; keep it objective in its scoring. Use the same critic prompt each time.

Adapt the model name (`Fable 5`) to whatever your strongest, most tasteful model is today — the role
matters, the product name does not.

> 中文：核心是「让另一个 agent 来裁决好不好」。执行者把自己的作品拿给评审看，评审只看截图，不关心实现与投入，只关心是否达标。评审用大模型（它只做决策，原文实测占输出 token 不到 10%），执行用便宜快的模型。注意最后那句：**9/10 的门槛写在执行者的提示词里，不能写进评审的评分标准**，且每次迭代用同一份评审提示词。

### Make the loop behave / 让循环可控

- **Make the criteria as clear and objective as possible.**
  - *Bad:* "Judge if our design looks beautiful, not AI-generated." Subjective; results vary wildly.
  - *OK:* "Review the aesthetic we're going for, visualize how a top design studio would execute it,
    then judge our design's quality against that bar." Still mushy, but consistent.
  - *Great:* "Here are 5 designs: 4 professional examples and 1 screenshot of our product. Rank them by
    polish and taste level." Concrete, objective, and gives a visual baseline.
- **Provide example images** — comparable screenshots, designs you like, or AI-generated concept art.
  Instruct the critic to treat these as a baseline or a moodboard, **not a target**; you don't want it
  copying other designs outright.
- **Set the stopping criteria carefully.** Otherwise the critic may never be satisfied and the agent
  burns tokens trying to please it. Ask for one or two iterations first and see whether it is
  converging before allowing more.
- **Choose the right model for each job.** Bigger models for the critic (more parameters generally mean
  better design sense and a wider distribution of ideas). Small models can implement, but don't go too
  small — the implementer still has to execute a direction well.

**Running the loop reliably**

- The critic must be a **separate context** that receives only the image. If your harness has a
  subagent call, use it; never "ask yourself to critique".
- Use **the same critic prompt** for every iteration, and keep the scoring rubric in the critic prompt
  only — the worker's instructions carry the completion bar.
- ※ Require **two consecutive ≥ 9/10 scores** before you accept the result, so one lucky pass does not
  end the loop.
- ※ **Budget check:** in the article's runs the critic used **under 10% of output tokens**. If yours is
  spending far more than that, the rubric is too subjective or the loop has no stop condition. Fix the
  rubric, not the model.
- ※ Record each iteration's score and the gaps it named. The list of repeated gaps is the fastest way to
  see what the direction is still failing to be.

> 中文：执行要点——评审必须是独立上下文且只拿到图、每次迭代用同一份评审提示词、评分标准只存在于评审提示词里（以上为原文要求）；※ 要连续两次 ≥9/10 才算通过；※ 评审吃掉大量 token 说明标准太主观或没有停止条件，改标准而不是换模型；※ 记录每轮分数与它指出的差距，重复出现的差距就是这个方向还没立住的地方。

### Capturing the screenshot ※

The critic is only as good as the picture it sees.

- Screenshot the **rendered page**, at a real viewport, after fonts and images have loaded.
- Capture the **full page** for composition feedback and **a viewport crop** for detail feedback.
- For states — hover, open menu, empty, error — capture each one; a critic cannot judge states it
  cannot see.
- If the design has motion, capture a short sequence or key frames rather than a single still.
- ※ If no browser or screenshot tooling is available, ask the user for the image (see "Getting a
  screenshot" in `SKILL.md`). Without a picture there is no critic step — say so instead of skipping it.

> 中文：截图为王——等字体和图片加载完、按真实视口截全页（看构图）＋视口裁切（看细节）；hover、展开态、空态、错误态都要单独截；有动效就截关键帧序列。※ 拿不到截图工具就找用户要图；没有图就没有评审这一步，要如实说明而不是跳过。

## Technique 4 — Use image generation to enrich designs

Coding agents love writing code and rarely reach for images. Left alone they substitute gradients,
shapes, and basic patterns — all strong giveaways of an AI-generated design. Push the agent to use
image generation (including shaders and 3D effects combined with images) and to verify the result
frame by frame in the browser.

**Verbatim prompt from the article:**

> The design is pretty plain. Add more personality using image generation. Consider shaders or 3D
> effects in combination with images to create more interesting visuals.
>
> For image generation, use this OpenAI API key (only use it locally, do not store it in the code or
> product): sk-…
>
> Verify that your work looks right frame-by-frame in the browser.

**Wiring options from the article:**

- **Codex, Antigravity, or Grok Build:** tell the agent to use its built-in image generation. It
  already knows how; it just rarely does so until instructed.
- **Claude Code or another agent plus a ChatGPT subscription:** tell the agent, "Use the Codex CLI to
  generate images. Help me install it if it isn't already present. Make sure it's billing my
  subscription, not an API key." This uses the subscription instead of paying per image.
- **Any other setup:** give the agent an OpenAI or Gemini API key. Create a **separate key with a tight
  spend limit** just for the agent, so a leaked or misused key stays cheap and can be revoked without
  disrupting other work.

**Key hygiene from the article:**

> Create a gitignored file called `.env.agents`, store this API key in it, and note to yourself in
> AGENTS.md/CLAUDE.md that these keys are for you to use during development (but must not ship with the
> product).

Never paste a key into a design artifact, commit it, or ship it. ※ Rotate any key that has been pasted
into a chat or a file that could be shared.

> 中文：agent 默认不会用图片，只会用渐变、形状、基础图案——这些都是最强的 AI 味信号。要明确要求它用图像生成（可与 shader、3D 效果组合），并要求在浏览器里逐帧核对结果。接入方式：Codex／Antigravity／Grok Build 用它自带的；Claude Code + ChatGPT 订阅就让 agent 通过 Codex CLI 生成并确认走订阅计费；其余情况给 OpenAI 或 Gemini 的 API key，且单独建一个限额 key。密钥放 gitignore 的 `.env.agents`，并在 AGENTS.md/CLAUDE.md 里声明「仅供开发、不得随产品发布」。

## Technique 5 — For more advanced motion, use video generation

Video models are not only for ads and clips. Two uses in real design work:

**A. Stunning animated graphics.** Generate a looping clip on a solid background, then remove the
background — chroma key it out (green screen) or, in harder cases, run a video matting model. The
result is an animation you can layer anywhere in the UI without it looking like a video.

> Verbatim prompt:
> "Can you replace the image on this page with a looping video clip that does something more
> interesting? Have the crystal splinter apart and slowly spin around. It should have awesome glassy
> effects that refract the page background and cast shadows and light around it.
> To get convincing glass refraction effects, render the video of the glass over the page background
> colors first (so it bakes in the refraction effects), then remove the background with a video matting
> model.
> Use this fal.ai API key: sk-…
> Find appropriate recent models for video generation and background removal."

**B. Fluid transitions between states.** Many video models interpolate between keyframe images, so two
product stills can become a transition clip. Play it when the user acts (screen change) or scrub it
frame by frame in response to a gesture (scroll or swipe).

> Verbatim prompt:
> "Build a demo page for a suitcase that uses a video model to create interactive transitions between a
> couple of screens. Each screen should show the suitcase in a different state, with vertical motion
> that feels appropriate for scrolling:
> – Initially, have the suitcase floating high up in the air
> – Then have it land on the floor and pop open
> – Finally, have its contents neatly land into it from the top
> Generate the initial frame using your image generation skill. Then, generate a video clip that starts
> from that frame and animates to the next state. Use the final frame of that video to seed the next
> transition so that it continues seamlessly. Scrub through the transitions one by one as the user
> scrolls.
> Use this fal.ai API key: sk-…
> Use a video model with strong physics and consistency, like Seedance 2.5."

**Model aggregation.** The best video models change frequently, so point the agent at an aggregator
platform such as [fal.ai](https://fal.ai/): one API key, and the agent can evaluate several options and
pick the strongest without you wiring up multiple integrations.

**Chaining frames is the trick for B:** each clip's final frame seeds the next clip, so separate
generations join seamlessly.

**Caveats ※**

- Video and image assets are heavy. Compress, use poster frames, lazy-load, and preload only what the
  first screen needs.
- Provide a **reduced-motion fallback** (a still, or a short CSS transition) and respect
  `prefers-reduced-motion`. A scroll-scrubbed video that ignores this is an accessibility defect.
- Keep the generated asset and the prompt that produced it in the repo, so the asset can be
  regenerated when the model behind it changes.

> 中文：视频模型不只是做广告。用法 A：先生成纯色背景的循环片段，再用 chroma key 或视频抠像模型去掉背景，得到可以叠在界面任何位置的动效（做玻璃折射时要先渲染在页面背景色上，把折射「烤」进去再抠）。用法 B：让视频模型在两帧产品图之间插值，得到过渡片段，在用户操作时播放或随滚动/滑动逐帧拖动；关键技巧是**用上一段视频的末帧作为下一段的起始帧**，多段拼接天然无缝。模型迭代快，用 fal.ai 这类聚合平台给一个 key 让 agent 自己挑。补充注意：视频资源重，要压缩、用海报帧、懒加载；必须提供 reduced-motion 降级；把生成的素材和提示词一起留在仓库里以便重生成。

## Exit checklist / 阶段出口自检

- [ ] A critic in a fresh context, given only screenshots, scored the design ≥ 9/10 with the same
      prompt used every iteration. ※ Twice in a row.
- [ ] The score was produced without the ≥ 9/10 bar appearing in the critic's prompt.
- [ ] The design's identity is visible in structure, type, and material — not only in color.
- [ ] Image and (if used) video assets are generated, in the repo, and compressed.
- [ ] ※ Reduced-motion and heavy-asset loading behaviour are handled.
- [ ] Iteration log exists: score per round plus the gaps the critic named.

> 中文：出口条件——独立评审在各轮同一提示词下独立给出 ≥9/10（连两次）；评审提示词里没有出现那条门槛；设计个性体现在结构、字体与材质而不只是颜色；图像与视频素材已生成、入库并压缩；处理了 reduced-motion 与重资源加载；保留了每轮分数与差距记录。

Next: `references/deliver.md` — subtract, remove AI tells, own the copy.
