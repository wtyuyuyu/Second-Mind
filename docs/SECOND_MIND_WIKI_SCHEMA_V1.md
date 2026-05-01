# SECOND_MIND_WIKI_SCHEMA_V1

## Purpose

This document defines the first practical wiki schema for Second Mind.

The schema is designed to support:

- local-first memory
- readable structure
- controlled cross-linking
- action-oriented compilation
- future extension to other systems

The schema is intentionally simple.  
It should support the first strong closed loop before growing larger.

## Core Idea

Second Mind does not use a graph-first interface.

Instead, it uses:

- tree-like structure for navigation
- selective links for meaningful cross-system relationships
- action and review layers for operational clarity

This means the schema should be readable like a structured library, not a cloud of nodes.

## Root Structure

```text
Second Mind Wiki/
├── index.md
├── inbox/
├── systems/
├── graph/
├── actions/
├── reviews/
├── meta/
└── archive/
```

## Root Layer Meanings

### index.md
The top-level map of the wiki.

### inbox/
Raw intake area before durable compilation.

### systems/
The four main systems:
- research
- life
- invest
- ai

### graph/
Shared entities, concepts, people, companies, and important cross-system relationships.

### actions/
Current action-oriented outputs.

### reviews/
Daily, weekly, and monthly reflection outputs.

### meta/
Rules, taxonomy, scoring logic, and ingest standards.

### archive/
Inactive, outdated, or deprioritized material.

## System Structure

Each system should have its own local organization.

An example for research:

```text
systems/research/
  _index.md
  directions/
  papers/
  concepts/
  decisions/
  actions/
  reviews/
```

## Page Types

Second Mind v1 uses a small set of core page types.

### Source
A structured page for one input source.

### Concept
A page for a mechanism, term, framework, or idea.

### Project
A page for an ongoing effort or direction.

### Decision
A page for a judgment, tradeoff, acceptance, rejection, or commitment.

### Action
A page for what should happen next.

### Review
A page for reflective updates over time.

## Why Page Types Matter

Page types are not the same as raw materials.

A paper, a chat, or a note is not the final knowledge unit.

The system first interprets inputs, then writes them into one of a few stable page forms.

This is what makes the wiki coherent instead of chaotic.

## Suggested Naming Convention

Use stable, readable, system-aware names:

```text
[system]-[type]-[slug].md
```

Examples:

```text
research-project-deepsea-tactile-roadmap.md
research-concept-taylor-flow-contact-mechanism.md
research-decision-hydrogel-direction-priority-2026-05-01.md
invest-project-yunnan-baiyao-thesis.md
life-review-weekly-2026-W18.md
ai-action-codex-ingest-pipeline.md
```

## Suggested Frontmatter

```yaml
title:
type:
system:
status:
confidence:
importance:
created:
updated:
sources:
tags:
links:
related_systems:
valid_until:
next_review:
```

## Cross-System Philosophy

Second Mind does not want indiscriminate linking.

It wants selective, meaningful relationship mapping.

Important cross-system relations include:

- Research <-> Investment
- Research <-> Life
- Investment <-> Life
- AI -> all systems

The goal is not maximum connectivity.  
The goal is maximum useful interpretability.

## Input Compilation

Inputs may come from:

- Obsidian notes
- Zotero papers
- Codex conversation summaries
- curated web material later

Each input should go through:

```text
source intake -> system routing -> scoring -> structure extraction -> page merge or page creation -> action output -> review scheduling
```

## Research V1 Intake Rule

For Research v1, Zotero intake is limited to:

- starred papers
- highlighted papers

This keeps the knowledge base high-signal at the beginning.

## V1 Simplicity Rule

The schema should remain simple enough that:

- the user can still read it directly
- Codex can maintain it reliably
- later automation does not corrupt it
- implementation remains understandable

The wiki should feel like an intelligible knowledge operating system, not an unreadable data exhaust.
