# pda-lab

Experiment-first repository for optimizing and evaluating Progressive De-Arbitrarization (PDA) handoff artifacts.

## Purpose

This repo exists to:
- version candidate PDA artifacts such as spells and handoff templates
- package benchmark tasks with reference closure and chosen benchmark directions
- score candidates with PDA-shaped rubrics
- run comparative evaluation loops
- preserve results from optimization runs

## Current Scoring Policy

- `rubrics/pda-handoff-v1` remains the historical scoring frame for existing runs
- `rubrics/pda-handoff-v2` is the forward scoring frame for optimizer work

Why `v2`:
- the strongest empirical failure mode so far is not incoherence, but answering at the wrong abstraction level
- `v2` makes abstraction-level fidelity explicit in scoring and hard-gate language

## Current Optimizer Lesson

So far the repo suggests a three-layer grounding pattern:

1. `reference/closed-formulation.md`
   Improves abstraction-level fidelity.
2. faithfulness-constrained generation
   Reduces fabricated specifics.
3. `reference/chosen-directions.md`
   Recovers benchmark-settled directions on harder tasks where a closed formulation alone is too weak.

This means some benchmark packages need more than a closed formulation. When a benchmark already has settled concrete directions that should not be reopened, they should be represented explicitly.

## Initial Structure

- `artifacts/` candidate prompts, spells, and handoff templates
- `benchmarks/` benchmark packages
- `rubrics/` human-readable and machine-readable scoring rubrics
- `eval/` evaluation harnesses and trace scoring logic
- `results/` run outputs and comparisons
- `scripts/` helper scripts for packaging and evaluation
- `docs/` short operational docs and links back to the canonical concept pages

## Canonical Concept Pages

The public conceptual home remains under:
- `https://andrey.kokoev.name/concepts/progressive-de-arbitrarization/`

This repo is the experimental and operational home.
