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
| [Predictive tasks and data roles](predictive_tasks.md) | Shared definitions of features, targets, observations and separate data roles. |
| [Interpret explanations](../how-to/interpret_explanations.md) | Reuses notebook screenshots and walks through dual uncertainty plus the triangular plot. |
| [Probabilistic & interval regression](probabilistic_regression.md) | Shows how calibrated probabilities and interval regression stay in lockstep across quickstarts and notebooks. |
| [Alternatives & triangular plots](alternatives.md) | Explains how the triangular view pairs with rule tables for calibrated alternatives. |
| [Architecture overview](architecture.md) | Connects runtime components, caching, and plugin guardrails. |
| [Error handling](error_handling.md) | Summarises runtime safeguards and expected exceptions. |
| [Explanation structures](explanation_structures.md) | Documents the internal data structures used by CalibratedExplanation classes. |
| [Guarded explanations](guarded_explanations.md) | In-distribution filtering via conformal anomaly detection for trustworthy rules. |
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
Probabilistic and interval regression <probabilistic_regression>
Alternative explanations and ensured filters <alternatives>
Guarded explanations <guarded_explanations>
Calibrated interval semantics <calibrated_interval_semantics>
Terminology: thresholded vs probabilistic regression <terminology_thresholded_vs_probabilistic_regression>
```
