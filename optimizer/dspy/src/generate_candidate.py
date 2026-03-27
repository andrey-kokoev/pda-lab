#!/usr/bin/env python3
"""DSPy-backed candidate generation for pda-lab.

This script consumes the exported optimizer dataset and writes a run slot containing:
- manifest.json
- trace/generated-trace.md
- handoff/generated-handoff.md

It does not score outputs. Scoring remains external to generation.
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


class HandoffGeneration(dspy.Signature):
    """Generate a reasoning trace and final handoff for an engineering benchmark."""

    benchmark_id = dspy.InputField(desc="Benchmark identifier")
    raw_task = dspy.InputField(desc="Original messy task statement")
    reference_closed_formulation = dspy.InputField(desc="Reference closed formulation for the benchmark")
    expected_policy_questions = dspy.InputField(desc="Expected policy questions that often need to be surfaced")
    validation_criteria = dspy.InputField(desc="Validation criteria for the benchmark")

    trace_markdown = dspy.OutputField(desc="Markdown reasoning trace showing how the task was shaped")
    handoff_markdown = dspy.OutputField(desc="Markdown final handoff ready for later scoring")


class HandoffGenerator(dspy.Module):
    def __init__(self) -> None:
        super().__init__()
        self.generate = dspy.Predict(HandoffGeneration)

    def forward(
        self,
        benchmark_id: str,
        raw_task: str,
        reference_closed_formulation: str,
        expected_policy_questions: str,
        validation_criteria: str,
    ):
        return self.generate(
            benchmark_id=benchmark_id,
            raw_task=raw_task,
            reference_closed_formulation=reference_closed_formulation,
            expected_policy_questions=expected_policy_questions,
            validation_criteria=validation_criteria,
        )


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
    (run_dir / "score-v2").mkdir(parents=True, exist_ok=True)
    return run_dir


def configured_api_base() -> str | None:
    return os.getenv("OPENAI_API_BASE") or os.getenv("OPENAI_BASE_URL")


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


def dry_run_generation(benchmark: dict) -> tuple[str, str]:
    trace = (
        "# Generated Trace\n\n"
        "## Dry Run\n\n"
        "This trace was produced without calling an LM. It exists only to verify the run-slot contract.\n\n"
        f"Benchmark: {benchmark['benchmark_id']}\n\n"
        "## Raw Task\n\n"
        f"{benchmark['raw_task']}\n\n"
        "## Reference Pressure\n\n"
        "The eventual DSPy generator should use the benchmark's closed formulation and expected policy questions to shape a real candidate trace.\n"
    )
    handoff = (
        "# Generated Handoff\n\n"
        "## Dry Run\n\n"
        "This handoff was produced without calling an LM. Replace it with DSPy-generated output in real runs.\n\n"
        "## Raw Task\n\n"
        f"{benchmark['raw_task']}\n\n"
        "## Validation Criteria\n\n"
        f"{benchmark['validation_criteria']}\n"
    )
    return trace, handoff


def real_generation(benchmark: dict) -> tuple[str, str]:
    generator = HandoffGenerator()
    prediction = generator(
        benchmark_id=benchmark["benchmark_id"],
        raw_task=benchmark["raw_task"],
        reference_closed_formulation=benchmark["reference_closed_formulation"],
        expected_policy_questions=benchmark["expected_policy_questions"],
        validation_criteria=benchmark["validation_criteria"],
    )
    return prediction.trace_markdown, prediction.handoff_markdown


def write_outputs(run_dir: Path, trace_markdown: str, handoff_markdown: str) -> None:
    (run_dir / "trace" / "generated-trace.md").write_text(trace_markdown.rstrip() + "\n")
    (run_dir / "handoff" / "generated-handoff.md").write_text(handoff_markdown.rstrip() + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("benchmark_id")
    parser.add_argument("candidate_id")
    parser.add_argument("--model", default=os.getenv("DSPY_MODEL"))
    parser.add_argument("--temperature", type=float, default=float(os.getenv("DSPY_TEMPERATURE", "1")))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    dataset = load_dataset()
    benchmark = benchmark_record(dataset, args.benchmark_id)
    manifest = load_manifest_template()
    manifest["benchmark_id"] = args.benchmark_id
    manifest["candidate_id"] = args.candidate_id
    manifest["summary"] = "DSPy-generated candidate run."

    run_dir = write_run_slot(args.benchmark_id, args.candidate_id)
    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")

    if args.dry_run:
        trace_markdown, handoff_markdown = dry_run_generation(benchmark)
    else:
        if not args.model:
            raise SystemExit(
                "A model must be provided via --model or DSPY_MODEL unless --dry-run is used. "
                "You can place DSPY_MODEL and provider credentials in .env."
            )
        configure_lm(args.model, args.temperature)
        trace_markdown, handoff_markdown = real_generation(benchmark)

    write_outputs(run_dir, trace_markdown, handoff_markdown)
    print(f"Prepared run slot: {run_dir}")
    print(f"Mode: {'dry-run' if args.dry_run else 'lm'}")
    if ENV_PATH.exists():
        print(f"Loaded env from: {ENV_PATH}")
    api_base = configured_api_base()
    if api_base:
        print(f"Using api base: {api_base}")


if __name__ == "__main__":
    main()
