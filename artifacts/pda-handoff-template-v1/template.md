# PDA Handoff Template v1

Use this template before delegating or executing a task when hidden semantic or policy ambiguity may materially affect implementation.

## Governing Rule

Do not proceed from the raw task statement directly to implementation or delegation if decision-relevant ambiguity remains hidden.

Instead:
1. localize the live ambiguity
2. separate forced structure from contingent policy
3. make residual freedom explicit
4. resolve explicit policy where needed
5. return to descent whenever optioning exposes a deeper ambiguity
6. recompose into a canonical implementation-ready handoff only after closure

## Process Shape

The phases below are conceptually distinct, but not strictly one-way.

Allowed flow:
- descent -> option resolution -> descent -> option resolution -> recomposition

Return from option resolution to descent whenever:
- a chosen option reveals a deeper hidden ambiguity
- the live ambiguity was mislocalized
- the current option set is not yet well-formed

## Phase 1: Descent

### Raw Task

State the task in its original or near-original form.

### Live Ambiguity

State where the ambiguity actually resides.

Use one or more of:
- semantics
- policy
- scope
- persistence
- ownership
- environment assumptions
- delegation shape
- validation target

### Forced Structure

List what is already forced by the problem, repo, product context, or user instruction.

### Contingent Policy

List what is still a choice and would materially affect implementation if left tacit.

### Decision-Relevant Question

State the single next question that would most reduce hidden arbitrariness.

Selection rule:
- ask only one question at a time
- ask from the layer where the live ambiguity currently resides
- prefer the question whose answer most constrains future valid continuations
- do not ask broad catch-all clarification questions
- do not enumerate options until the ambiguity is explicit enough to do so cleanly

## Optioning Readiness Test

Enter option resolution only if all of the following are true:
- the live ambiguity has been localized to a specific layer
- the unresolved fork can be named as a concrete choice point
- the options can be stated without mixing layers or hidden sub-questions
- choosing among them would materially constrain implementation or delegation

If any of these are false, remain in descent.

## Phase 2: Option Resolution

Enter this phase only when the remaining ambiguity is explicit enough to enumerate.

### Explicit Choice Point

Name the unresolved policy or semantic fork.

### Options

Present one choice point at a time using lettered options.

For each option include:
- the option itself
- the main consequence/tradeoff
- your current best default marked clearly

### Recorded Choice

After the answer, restate the selected option and its consequence for the task shape.

### Return Check

After each recorded choice, ask:
- did this resolve the live ambiguity
- or did it expose a deeper or adjacent ambiguity that must be descended into before further optioning?

If a deeper ambiguity has appeared, return to Phase 1.

### Repeat Condition

Repeat Phase 2 only while the remaining ambiguity is still decision-relevant and well-formed enough for explicit options.

Stop when the remaining ambiguity is:
- forced
- explicitly chosen
- or irrelevant to execution

## Phase 3: Recomposition

Produce a handoff that is concise, canonical, and executable.

### Closure Summary

State what is now non-ambiguous because of prior descent and choice.

### Declared Irrelevancies / Non-goals

List any ambiguities that were identified but are now explicitly out of scope or irrelevant to execution.

If none, say `None`.

### Closed Formulation

State the resolved formulation of the task.

This should preserve:
- key semantic distinctions discovered during descent
- chosen policy decisions
- explicit non-goals or declared irrelevancies

### Implementation Task

State what should now be done.

Include only:
- scope
- required behavior
- relevant constraints
- validation target

Do not reintroduce distinctions that were already declared irrelevant.

### Validation Target

State how success should be checked.

Use one or more of:
- code review criteria
- behavioral acceptance criteria
- tests/checks to run
- explicit failure modes to watch for

## Hard Prohibitions

Do not:
- jump to implementation while policy is still tacit
- mix forced constraints with contingent choices
- ask multiple broad ambiguities at once when one live ambiguity can be isolated
- enumerate options before the ambiguity is properly localized
- remain in optioning after deeper ambiguity has been revealed
- recompose before the residual freedom is resolved or declared irrelevant
- omit known non-goals or declared irrelevancies from the final handoff

## Completion Condition

The handoff is ready only when:
- the live ambiguity has been localized
- forced structure is separated from chosen policy
- residual freedom is explicit
- remaining choices are either resolved or irrelevant
- any deeper ambiguity exposed during optioning has been processed
- declared irrelevancies are stated explicitly
- the final task statement is directly executable by another competent agent
