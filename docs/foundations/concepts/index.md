# Concepts and methods

<span id="concepts-architecture"></span>

Use this collection to understand an output or mechanism after the
{doc}`workflow overview <../../sections/how-ce-works>`. Choose a topic below;
you do not need to read the software architecture first.

The shared {doc}`semantics reference <calibrated_interval_semantics>` records
mode-specific assumptions and limits. For papers and replication, use the
{doc}`researcher hub <../../researcher/index>`.

| Concept | Why it matters |
| --- | --- |
| [Tasks, modes and capabilities](tasks_modes_capabilities.md) | Choose the output question and operation separately. |
| [Calibration and statistical background](calibration_background.md) | Understand accuracy, calibration, quantiles and assumptions. |
| [How explanations are built](how_explanations_are_built.md) | Connect conditions, comparison responses and reported quantities. |
| [Predictive tasks and data roles](predictive_tasks.md) | Shared definitions of features, targets, observations and separate data roles. |
| [Interpret explanations](../how-to/interpret_explanations.md) | Connects prediction information, factual weights and alternative predictions to records and figures. |
| [Probabilistic & interval regression](probabilistic_regression.md) | Distinguishes target-value intervals from event probabilities and their API calls. |
| [Alternatives & triangular plots](alternatives.md) | Explains how the triangular view pairs with rule tables for calibrated alternatives. |
| [Architecture overview](architecture.md) | Connects runtime components, caching, and plugin guardrails. |
| [Error handling](error_handling.md) | Summarises runtime safeguards and expected exceptions. |
| [Explanation structures](explanation_structures.md) | Documents the internal data structures used by CalibratedExplanation classes. |
| [Guarded explanations](guarded_explanations.md) | Explains support-filtered candidates, prerequisites and limitations. |
| [Calibrated interval semantics](calibrated_interval_semantics.md) | Canonical semantics, assumptions, and non-guarantees for all three modes. |
| [Terminology standardization](terminology.md) | Summarises the shift to probabilistic regression terminology and compatibility guarantees. |
| [Terminology: thresholded vs probabilistic regression](terminology_thresholded_vs_probabilistic_regression.md) | Clarifies language used across ADR-021 and user-facing regression docs. |
| [Parameter reference](parameter-reference.md) | Canonical definitions and disambiguation table for `threshold`, `confidence`, `significance`, `confidence_level`, and `low_high_percentiles`. |


Entry-point tier: Tier 3.

## Related pages

- {doc}`Architecture <architecture>`.
- {doc}`Error handling and validation <error_handling>`.
- {doc}`Explanation Structures <explanation_structures>`.
- {doc}`Glossary and terminology <terminology>`.
- {doc}`Parameter reference <parameter-reference>`.

```{toctree}
:maxdepth: 1

Predictive tasks and data roles <predictive_tasks>
Tasks, modes and capabilities <tasks_modes_capabilities>
Calibration and statistical background <calibration_background>
How explanations are built <how_explanations_are_built>
Probabilistic and interval regression <probabilistic_regression>
Alternative explanations and ensured filters <alternatives>
Guarded explanations <guarded_explanations>
Calibrated interval semantics <calibrated_interval_semantics>
Terminology: thresholded vs probabilistic regression <terminology_thresholded_vs_probabilistic_regression>
```
