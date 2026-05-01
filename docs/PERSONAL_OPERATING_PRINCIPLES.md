# PERSONAL_OPERATING_PRINCIPLES

## Purpose

This document records the user's enduring operating principles.

These principles are both:

- personal preferences
- Second Mind design and development principles

They should influence product decisions, system architecture, visual design, scope control, and structured response style.

## Apple-Like Product Principles

### Clarity First
The most important information should be understandable immediately.

Clarity is prioritized over density, novelty, or decoration.

### Subtraction Before Addition
The system should remove unnecessary parts before adding new ones.

Features, interface elements, and structure should be reduced until only the essential remains.

### Calm Precision
The system should feel controlled, legible, and exact.

Layouts, spacing, hierarchy, and wording should be restrained and deliberate, not noisy or overstimulating.

### Product-Like Finish
Even early prototypes should feel like products rather than rough experiments.

This means consistent hierarchy, readable composition, strong restraint, and credible polish.

## First-Principles Engineering

### Start from the irreducible need
Before designing any module, ask what problem it solves at the most basic level.

### Remove non-essential modules first
Before optimizing, reduce structure.

Do not keep a feature merely because it feels advanced or impressive.

### Build the smallest closed loop first
The first milestone is not feature completeness.

The first milestone is one working loop with clear value.

### Depend on abstractions, not specific tools
The system should not become fragile by binding itself too tightly to one implementation detail.

Obsidian, Zotero, Codex, and future tools should be treated as replaceable interfaces where possible.

## Research and Answering Preferences

### Search in English by default when external research is needed
For Chinese questions that require online research, first translate the search intent into English when useful, search and cross-check sources, then respond in Chinese.

### Respond with structured output
When answering substantial questions, prefer structured output that makes judgment and action legible.

A default structure is:

- core conclusion
- key reasoning
- important tradeoffs or unknowns
- next actions

## Additional Engineering Principles

### KISS
Keep the system simple enough to remain understandable and maintainable.

### DRY
Avoid duplicate structures, duplicate judgments, and duplicate storage.

### High Cohesion, Low Coupling
Each subsystem should have a clear responsibility.

Cross-system collaboration should exist, but through disciplined interfaces rather than uncontrolled entanglement.

## Implications for Second Mind

These principles imply the following:

- do not start with graph-first visualization
- do not overbuild automation early
- do not expand all systems in parallel
- do not confuse storage with cognition
- do not confuse visual complexity with intelligence

Instead:

- define clear source-of-truth layers
- close one domain loop first
- design for legibility
- prefer durable summaries over noisy accumulation
- build systems that help judgment and action

## Current Strategic Consequence

Based on these principles, Second Mind v1 should focus on the Research System first.
