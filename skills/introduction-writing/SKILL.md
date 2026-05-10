---
name: introduction-writing
description: Use when drafting, revising, or planning an academic paper Introduction, especially when the user needs a general-to-specific logic chain, research gap framing, high-level literature ladder, or Chinese discussion before English writing. Prioritizes Nature/Science/Cell main journal and major sub-journal references before lower-tier supporting papers.
metadata:
  skill-author: local WTY research workflow
---

# Introduction Writing

Use this skill when the user asks to write, revise, or discuss a paper Introduction, including:

- “帮我写 introduction”
- “这个引言逻辑怎么搭”
- “怎么从大问题收束到我的工作”
- “总结 introduction 写作框架”
- “这几篇文章怎么串成 ABC 逻辑”

## Core Principle

An Introduction is not a literature list. It is a narrowing argument:

```text
general problem -> known progress -> unresolved boundary -> precise research gap -> this work
```

The first paragraph should define a broad, high-level scientific or engineering problem, then gradually narrow toward the paper's specific problem. Do not start from the user's device, material, algorithm, or demo unless the field itself is already extremely narrow.

## Default Workflow

1. **Define the general problem**
   - State the broad natural, engineering, biomedical, robotic, computational, or physical context.
   - Make it bigger than the user's immediate device.
   - Then add one narrowing sentence showing where the user's system sits inside the broad problem.

2. **Build the literature ladder**
   - Select 3-5 anchor papers.
   - Prioritize in this order:
     1. Nature / Science / Cell main journals
     2. Nature Physics / Nature Chemistry / Nature Nanotechnology / Nature Electronics / Nature Machine Intelligence / Science Robotics / Science Advances and equivalent major sub-journals
     3. Nature Communications
     4. Advanced Materials / Advanced Functional Materials / ACS Nano and other strong specialist journals
     5. Lower-tier papers only as supporting or technical references
   - If no high-level paper directly matches the exact topic, use high-level papers for the upstream mechanism and explicitly state the boundary.

3. **Write each literature step as A/B/C**
   - A did what?
   - What did A not answer?
   - B moved the field how?
   - What boundary remains?
   - C adds what missing dimension?
   - What still remains unresolved for this paper?

4. **Add bridge sentences**
   - Between every two paragraphs, explain why the argument moves from one domain to the next.
   - Typical bridges:
     - from liquid-liquid interface to liquid-solid interface
     - from static interface to dynamic interface
     - from normal pressure to high pressure
     - from mechanism to device
     - from material response to system-level behavior

5. **State the research gap directly**
   - The gap should be a missing mechanism, missing condition, missing coupling, missing system regime, or missing generalizable model.
   - Avoid vague gaps such as “few studies have explored this”.
   - Prefer: “It remains unclear how X changes Y under Z.”

6. **Introduce this work**
   - State the model system or method.
   - State what it controls, observes, or decouples.
   - State the central question.
   - State the broader implication, but do not overclaim.

## Paragraph Template

```text
Paragraph 1: General problem and narrowing
Many natural and engineered systems involve [broad phenomenon]. In [important contexts], [key process] is not static but [dynamic features]. However, under [critical condition], how [condition] changes [mechanism] remains unclear, limiting [broader system or design consequence].

Paragraph 2: First anchor field
Researchers first showed that [interface/system A] is not [old assumption]. [Top paper 1] revealed [finding]. [Top paper 2] further showed [finding]. These studies establish [core principle], but they mainly address [boundary].

Paragraph 3: Migration step
In practical systems, [A] rarely exists alone; it is constrained by or coupled with [B]. Therefore, the problem moves from [old scope] to [new scope]. [Anchor paper 3] demonstrated [progress]. However, it still does not resolve [remaining boundary].

Paragraph 4: Research gap and this work
The central gap is therefore [precise gap]. Here, this work uses [model/platform/method] to [controlled action], enabling [what can be observed/decoupled]. This paper asks how [core variable] regulates [mechanism] and provides [scientific insight/application outlet].
```

## Quality Checklist

Before finalizing, check:

- Does paragraph 1 define a big enough problem?
- Does every paragraph narrow the scope instead of merely adding references?
- Is there a bridge sentence between A, B, C, and this work?
- Are high-level references used as the main ladder, with lower-tier papers demoted to support?
- Is the research gap written as a mechanism question, not a vague “less studied” statement?
- Does the paper avoid presenting the application demo as the whole scientific contribution?
- Are the boundaries of cited papers stated fairly, without claiming they solved the user's exact problem?

## Local Example Pattern

For the user's high-pressure Taylor-flow interface topic, the preferred logic is:

```text
dynamic oil-water-solid contact is common in natural and engineered systems
-> oil-water interfaces are electrically active
-> real microfluidic and underwater systems impose solid-wall constraints
-> liquid-solid dynamic contact electrification provides a partial mechanism basis
-> normal-pressure liquid-solid results cannot be directly extrapolated to deep-sea hydrostatic pressure
-> research gap: high-pressure oil-water-solid dynamic interfacial electrification remains unclear
-> Taylor flow microchannels provide a controllable platform to study charge transfer, electric double layers, and charge-release pathways
```

