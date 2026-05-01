# RESEARCH_FIRST_STRATEGY

## Why Research Comes First

Second Mind should not expand all four systems at once.

The system needs one real closed loop before it earns the complexity of broader expansion.

Research is the right first domain because it has:

- high-value but noisy inputs
- long time horizons
- strong need for prioritization
- clear links between ideas, papers, projects, and decisions
- a natural need for action and review

Research is therefore the reference implementation for Second Mind v1.

## V1 Goal

Research v1 is designed to close one loop fully:

```text
input -> scoring -> compilation -> memory -> action -> review
```

This means Research v1 is not just a paper archive.  
It is a research operating loop.

## Scope Boundary

Research v1 will not prioritize:

- automatic mentor scheduling
- graph visualization
- multi-system auto-linked dashboards
- broad social content ingestion
- complicated autonomous multi-agent orchestration

The goal is to make the research loop strong, simple, and durable first.

## Initial Input Sources

Research v1 ingests only three sources:

- starred and highlighted papers from Zotero
- Codex research discussion summaries
- Obsidian research notes

This scope is intentionally narrow.

It avoids the trap of collecting too much information before the system has a reliable method of filtering and compiling it.

## Why Zotero Is Limited to Starred and Highlighted Papers

Not every paper deserves durable attention.

Research v1 uses a strong selection bias:

- if a paper is starred, it has already passed a relevance threshold
- if a paper is highlighted, it contains locally important evidence or ideas

This makes Zotero intake more focused and reduces low-value noise.

## Research Scoring

Each input should be scored before it enters long-term structure.

A suggested early scoring model is:

\[
ResearchScore = 0.30R + 0.25E + 0.20N + 0.15A + 0.10U
\]

Where:

- \(R\) = Relevance to current research directions
- \(E\) = Evidence quality
- \(N\) = Novelty
- \(A\) = Actionability
- \(U\) = Undernoticed potential

The final term matters because some important papers are not initially obvious.

## Research Page Types

Research v1 mainly compiles information into five page types:

- Paper Source
- Concept
- Direction
- Decision
- Action

### Paper Source
A structured page for one paper.

### Concept
A page for a mechanism, term, method, or technical idea.

### Direction
A page for a long-running research direction.

### Decision
A page for important scientific judgment, selection, or rejection.

### Action
A page for what should be read, tested, discussed, or verified next.

## Research Memory Structure

Research pages should live under a dedicated subtree such as:

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

This keeps the system coherent and extensible.

## Expected Outputs

Research v1 should produce operational outputs, not just summaries.

Examples:

- the three most valuable papers to read next
- the key unresolved question for a direction
- the next experimental or conceptual step
- what should be delayed, archived, or deprioritized

## Review Layer

A research system without review becomes a storage system.

So Research v1 must also support:

- weekly review
- dropped directions
- changing confidence
- invalidated assumptions
- updated priorities

This is what turns a wiki into a living decision system.

## Success Criteria

Research v1 succeeds when the user can reliably move from:

- scattered papers and conversations

to:

- direction clarity
- better judgment
- next actions
- stable memory
- repeatable review

Only after this loop is stable should Second Mind expand deeply into Life and Investment.
