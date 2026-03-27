#!/usr/bin/env python3
"""DSPy-backed candidate generation for pda-lab.

This script consumes the exported optimizer dataset and writes a run slot containing:
- manifest.json
- trace/generated-trace.md
- handoff/generated-handoff.md
- optionally critique/generated-critique.md

Scoring remains external to generation.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from dotenv import load_dotenv
import dspy

ROOT = Path(__file__).resolve().parents[3]
DATASET_PATH = ROOT / "results" / "optimizer-dataset.json"
RUNS_DIR = ROOT / "results" / "runs"
MANIFEST_TEMPLATE_PATH = ROOT / "optimizer" / "dspy" / "run-slot-template.json"
ENV_PATH = ROOT / ".env"

load_dotenv(ENV_PATH, override=False)


class HandoffDraft(dspy.Signature):
    """Produce a benchmark-faithful PDA trace and handoff.

    Requirements:
    - Treat the reference closed formulation as a normative target, not background context.
    - Stay at the governing ambiguity level before recomposition.
    - Preserve benchmark scope and closure state rather than inventing plausible generic policy.
    - If an exact concrete value is not supported by the raw task or reference material, do not invent one; either keep it abstract or mark it as unresolved.
    - Prefer benchmark-faithfulness over generic completeness.
    """

    benchmark_id = dspy.InputField(desc="Benchmark identifier")
    raw_task = dspy.InputField(desc="Original messy task statement")
    reference_closed_formulation = dspy.InputField(desc="Reference closed formulation for the benchmark")
    expected_policy_questions = dspy.InputField(desc="Expected policy questions that often need to be surfaced")
    chosen_directions = dspy.InputField(desc="Settled benchmark-specific directions that should be preserved rather than reopened")
    validation_criteria = dspy.InputField(desc="Validation criteria for the benchmark")
    faithfulness_contract = dspy.InputField(desc="Benchmark-faithfulness instructions that constrain invention and preserve closure state")

    trace_markdown = dspy.OutputField(desc="Markdown reasoning trace")
    handoff_markdown = dspy.OutputField(desc="Markdown final handoff")


class HandoffCritiqueLite(dspy.Signature):
    """Produce a short critique of a draft against benchmark-faithfulness.

    Keep this concise and only call out concrete benchmark-faithfulness issues such as:
    - wrong abstraction level
    - reopening chosen directions
    - invented concrete specifics
    - narrowed or widened scope drift
    - missing settled directions that the benchmark already fixes
    """

    benchmark_id = dspy.InputField(desc="Benchmark identifier")
    reference_closed_formulation = dspy.InputField(desc="Reference closed formulation for the benchmark")
    expected_policy_questions = dspy.InputField(desc="Expected policy questions that often need to be surfaced")
    chosen_directions = dspy.InputField(desc="Settled benchmark-specific directions")
    validation_criteria = dspy.InputField(desc="Validation criteria for the benchmark")
    draft_trace_markdown = dspy.InputField(desc="Draft markdown reasoning trace")
    draft_handoff_markdown = dspy.InputField(desc="Draft markdown final handoff")

    needs_revision = dspy.OutputField(desc="Answer yes if the draft materially drifts from benchmark faithfulness, otherwise no")
    critique_markdown = dspy.OutputField(desc="Short markdown critique with only the highest-signal benchmark-faithfulness issues")


class HandoffRevision(dspy.Signature):
    """Revise a draft using a short benchmark-faithfulness critique.

    Requirements:
    - Apply the critique directly.
    - Preserve any correct settled directions already present.
    - Recover missing chosen directions when grounded.
    - Do not invent new specifics just to satisfy the critique.
    - Keep the revision compact.
    """

    benchmark_id = dspy.InputField(desc="Benchmark identifier")
    raw_task = dspy.InputField(desc="Original messy task statement")
    reference_closed_formulation = dspy.InputField(desc="Reference closed formulation for the benchmark")
    expected_policy_questions = dspy.InputField(desc="Expected policy questions that often need to be surfaced")
    chosen_directions = dspy.InputField(desc="Settled benchmark-specific directions")
    validation_criteria = dspy.InputField(desc="Validation criteria for the benchmark")
    faithfulness_contract = dspy.InputField(desc="Benchmark-faithfulness instructions")
    draft_trace_markdown = dspy.InputField(desc="Draft markdown reasoning trace")
    draft_handoff_markdown = dspy.InputField(desc="Draft markdown final handoff")
    critique_markdown = dspy.InputField(desc="Short benchmark-faithfulness critique")

    trace_markdown = dspy.OutputField(desc="Revised markdown reasoning trace")
    handoff_markdown = dspy.OutputField(desc="Revised markdown final handoff")


class HandoffGenerator(dspy.Module):
    def __init__(self) -> None:
        super().__init__()
        self.draft = dspy.Predict(HandoffDraft)
        self.critique = dspy.Predict(HandoffCritiqueLite)
        self.revise = dspy.Predict(HandoffRevision)

    def forward(
        self,
        benchmark_id: str,
        raw_task: str,
        reference_closed_formulation: str,
        expected_policy_questions: str,
        chosen_directions: str,
        validation_criteria: str,
        faithfulness_contract: str,
        with_critique: bool,
        auto_revise: bool,
    ):
        draft = self.draft(
            benchmark_id=benchmark_id,
            raw_task=raw_task,
            reference_closed_formulation=reference_closed_formulation,
            expected_policy_questions=expected_policy_questions,
            chosen_directions=chosen_directions,
            validation_criteria=validation_criteria,
            faithfulness_contract=faithfulness_contract,
        )

        result = {
            "draft_trace_markdown": draft.trace_markdown,
            "draft_handoff_markdown": draft.handoff_markdown,
            "critique_markdown": None,
            "trace_markdown": draft.trace_markdown,
            "handoff_markdown": draft.handoff_markdown,
            "needs_revision": None,
        }

        if not with_critique:
            return result

        critique = self.critique(
            benchmark_id=benchmark_id,
            reference_closed_formulation=reference_closed_formulation,
            expected_policy_questions=expected_policy_questions,
            chosen_directions=chosen_directions,
            validation_criteria=validation_criteria,
            draft_trace_markdown=draft.trace_markdown,
            draft_handoff_markdown=draft.handoff_markdown,
        )
        result["critique_markdown"] = critique.critique_markdown
        result["needs_revision"] = critique.needs_revision

        if auto_revise and critique.needs_revision.strip().lower() == "yes":
            revision = self.revise(
                benchmark_id=benchmark_id,
                raw_task=raw_task,
                reference_closed_formulation=reference_closed_formulation,
                expected_policy_questions=expected_policy_questions,
                chosen_directions=chosen_directions,
                validation_criteria=validation_criteria,
                faithfulness_contract=faithfulness_contract,
                draft_trace_markdown=draft.trace_markdown,
                draft_handoff_markdown=draft.handoff_markdown,
                critique_markdown=critique.critique_markdown,
            )
            result["trace_markdown"] = revision.trace_markdown
            result["handoff_markdown"] = revision.handoff_markdown

        return result


def load_dataset() -> dict:
    return json.loads(DATASET_PATH.read_text())


def load_manifest_template() -> dict:
    return json.loads(MANIFEST_TEMPLATE_PATH.read_text())


def benchmark_record(dataset: dict, benchmark_id: str) -> dict:
    for item in dataset["benchmarks"]:
        if item["benchmark_id"] == benchmark_id:
            return item
    raise KeyError(f"Unknown benchmark_id: {benchmark_id}")


def write_run_slot(benchmark_id: str, candidate_id: str) -> Path:
    run_dir = RUNS_DIR / benchmark_id / candidate_id
    (run_dir / "trace").mkdir(parents=True, exist_ok=True)
    (run_dir / "handoff").mkdir(parents=True, exist_ok=True)
    (run_dir / "critique").mkdir(parents=True, exist_ok=True)
    (run_dir / "score-v2").mkdir(parents=True, exist_ok=True)
    return run_dir


def configured_api_base() -> str | None:
    return os.getenv("OPENAI_API_BASE") or os.getenv("OPENAI_BASE_URL")


def build_faithfulness_contract(benchmark: dict) -> str:
    return (
        "Use the benchmark reference as a binding target for scope and policy direction.\n"
        "Do not invent concrete numeric thresholds, percentages, margins, sizes, or platform scope restrictions unless they are grounded in the raw task or reference materials.\n"
        "If a policy locus is explicit but its exact value is not grounded, keep it abstract or name it as unresolved instead of fabricating a specific choice.\n"
        "Preserve the benchmark's intended scope; do not narrow it for convenience.\n"
        "Preserve distinctions named in the reference closed formulation and expected policy questions.\n"
        "If chosen directions are provided, treat them as already settled and do not reopen or replace them with generic alternatives unless the raw task explicitly conflicts.\n"
        f"Reference closure target:\n{benchmark['reference_closed_formulation']}\n\n"
        f"Chosen directions:\n{benchmark.get('chosen_directions') or '(none)'}\n\n"
        f"Expected policy questions:\n{benchmark['expected_policy_questions']}"
    )


def configure_lm(model: str, temperature: float) -> None:
    kwargs = {"temperature": temperature}
    api_key = os.getenv("OPENAI_API_KEY")
    api_base = configured_api_base()
    if api_key:
        kwargs["api_key"] = api_key
    if api_base:
        kwargs["api_base"] = api_base
    lm = dspy.LM(model=model, **kwargs)
    dspy.configure(lm=lm)


def dry_run_generation(benchmark: dict, with_critique: bool) -> dict[str, str | None]:
    draft_trace = (
        "# Generated Draft Trace\n\n"
        "## Dry Run\n\n"
        "This draft trace was produced without calling an LM.\n"
    )
    draft_handoff = (
        "# Generated Draft Handoff\n\n"
        "## Dry Run\n\n"
        "This draft handoff was produced without calling an LM.\n"
    )
    critique = (
        "# Generated Critique\n\n"
        "## Dry Run\n\n"
        "No critique was generated because the LM path was not used.\n"
        if with_critique else None
    )
    return {
        "draft_trace_markdown": draft_trace,
        "draft_handoff_markdown": draft_handoff,
        "critique_markdown": critique,
        "trace_markdown": draft_trace,
        "handoff_markdown": draft_handoff,
        "needs_revision": None,
    }


def real_generation(benchmark: dict, with_critique: bool, auto_revise: bool) -> dict[str, str | None]:
    generator = HandoffGenerator()
    return generator(
        benchmark_id=benchmark["benchmark_id"],
        raw_task=benchmark["raw_task"],
        reference_closed_formulation=benchmark["reference_closed_formulation"],
        expected_policy_questions=benchmark["expected_policy_questions"],
        chosen_directions=benchmark.get("chosen_directions") or "",
        validation_criteria=benchmark["validation_criteria"],
        faithfulness_contract=build_faithfulness_contract(benchmark),
        with_critique=with_critique,
        auto_revise=auto_revise,
    )


def write_outputs(run_dir: Path, outputs: dict[str, str | None]) -> None:
    (run_dir / "trace" / "draft-trace.md").write_text(outputs["draft_trace_markdown"].rstrip() + "\n")
    (run_dir / "handoff" / "draft-handoff.md").write_text(outputs["draft_handoff_markdown"].rstrip() + "\n")
    if outputs.get("critique_markdown"):
        (run_dir / "critique" / "generated-critique.md").write_text(outputs["critique_markdown"].rstrip() + "\n")
    (run_dir / "trace" / "generated-trace.md").write_text(outputs["trace_markdown"].rstrip() + "\n")
    (run_dir / "handoff" / "generated-handoff.md").write_text(outputs["handoff_markdown"].rstrip() + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("benchmark_id")
    parser.add_argument("candidate_id")
    parser.add_argument("--model", default=os.getenv("DSPY_MODEL"))
    parser.add_argument("--temperature", type=float, default=float(os.getenv("DSPY_TEMPERATURE", "1")))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--with-critique", action="store_true")
    parser.add_argument("--auto-revise", action="store_true")
    args = parser.parse_args()

    dataset = load_dataset()
    benchmark = benchmark_record(dataset, args.benchmark_id)
    manifest = load_manifest_template()
    manifest["benchmark_id"] = args.benchmark_id
    manifest["candidate_id"] = args.candidate_id
    manifest["summary"] = "DSPy-generated candidate run."
    manifest["notes"] = (
        "Includes critique pass and automatic revision."
        if args.auto_revise else
        "Includes critique pass only."
        if args.with_critique else
        "Single-shot draft only."
    )

    run_dir = write_run_slot(args.benchmark_id, args.candidate_id)
    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")

    if args.dry_run:
        outputs = dry_run_generation(benchmark, args.with_critique)
    else:
        if not args.model:
            raise SystemExit(
                "A model must be provided via --model or DSPY_MODEL unless --dry-run is used. "
                "You can place DSPY_MODEL and provider credentials in .env."
            )
        configure_lm(args.model, args.temperature)
        outputs = real_generation(benchmark, args.with_critique, args.auto_revise)

    write_outputs(run_dir, outputs)
    print(f"Prepared run slot: {run_dir}")
    print(f"Mode: {'dry-run' if args.dry_run else 'lm'}")
    print(f"Critique: {'on' if args.with_critique else 'off'}")
    print(f"Auto revise: {'on' if args.auto_revise else 'off'}")
    if ENV_PATH.exists():
        print(f"Loaded env from: {ENV_PATH}")
    api_base = configured_api_base()
    if api_base:
        print(f"Using api base: {api_base}")


if __name__ == "__main__":
    main()
