# pda-lab

Experiment-first repository for optimizing and evaluating Progressive De-Arbitrarization (PDA) handoff artifacts.

## Purpose

This repo exists to:
- version candidate PDA artifacts such as spells and handoff templates
- package benchmark tasks with reference closed formulations
- score candidates with PDA-shaped rubrics
- run comparative evaluation loops
- preserve results from optimization runs

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
