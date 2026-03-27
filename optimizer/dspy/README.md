# DSPy Integration

This directory is the initial DSPy-facing integration surface for `pda-lab`.

## Goal

Use DSPy to generate and compare candidate PDA handoff artifacts against the exported optimizer dataset.

## Current Status

Executable scripts:
- `optimizer/dspy/src/generate_candidate.py`
- `optimizer/dspy/src/check_provider.py`

`generate_candidate.py` supports:
- `--dry-run` for local smoke testing without an LM
- real LM-backed generation via DSPy when `--model` or `DSPY_MODEL` is provided
- automatic loading of repo-local `.env` from the project root
- `OPENAI_API_BASE` or `OPENAI_BASE_URL` for OpenAI-compatible providers

`check_provider.py` supports:
- direct auth/endpoint/model validation against an OpenAI-compatible provider
- isolating provider config issues before blaming DSPy

## Credentials

The scripts load `.env` from the repo root automatically.

Recommended repo-root `.env` values for Kimi / Moonshot:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_API_BASE=https://api.moonshot.cn/v1
DSPY_MODEL=openai/kimi-k2.5
```

A starter file is provided at:
- `optimizer/dspy/.env.example`

Copy it to the repo root as `.env` and fill in your real values.

## Examples

```bash
uv run python optimizer/dspy/src/check_provider.py
uv run python optimizer/dspy/src/generate_candidate.py build-update-visibility candidate-202 --dry-run
uv run python optimizer/dspy/src/generate_candidate.py build-update-visibility candidate-203 --model openai/kimi-k2.5
```

## Why Separate Generation And Scoring

Keeping DSPy on the generation side only prevents the optimizer loop from quietly changing the lab's evaluation semantics.
