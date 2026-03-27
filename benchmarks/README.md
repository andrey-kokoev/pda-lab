# Benchmarks

Each benchmark package should contain:
- raw task statement
- baseline repo state reference
- reference closed formulation
- expected policy questions
- validation criteria

Some benchmarks should also contain:
- chosen directions

Use `reference/chosen-directions.md` when the benchmark has already settled concrete directions that are stronger than a general closed formulation. This file exists to prevent the generator from either:
- inventing plausible generic specifics
- or staying too abstract after avoiding invention

A good rule:
- closed formulation captures the shape of adequate closure
- chosen directions capture benchmark-specific commitments that should be preserved rather than reopened
