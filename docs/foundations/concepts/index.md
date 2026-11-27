# Concepts and methods

<span id="concepts-architecture"></span>

Use this collection to understand an output or mechanism after the
{doc}`workflow overview <../../sections/how-ce-works>`. Choose a topic below;
you do not need to read the software architecture first.

The shared {doc}`semantics reference <calibrated_interval_semantics>` records
mode-specific assumptions and limits. For papers and replication, use the
{doc}`researcher hub <../../researcher/index>`.

## Learn the core ideas in order

The {doc}`How CE Works tutorial <../../sections/how-ce-works>` gives these pages their reading sequence:

1. {doc}`Predictive tasks and data roles <predictive_tasks>`.
2. {doc}`Tasks, modes and capabilities <tasks_modes_capabilities>`.
3. {doc}`Calibration and statistical background <calibration_background>`.
4. {doc}`How explanations are built <how_explanations_are_built>`.
5. {doc}`Interpret explanations <../how-to/interpret_explanations>`.

## Deepen a specific topic

- {doc}`Optional capabilities <optional_capabilities>` explains when to add grouping, guarding, combined rules, alternative filtering or rejection after reading a core result.


- {doc}`Regression: values and events <probabilistic_regression>` separates target-value intervals from event probabilities.
- {doc}`Alternative explanations <alternatives>` introduces comparisons and triangular views.
- {doc}`Guarded explanations <guarded_explanations>` explains support filtering and its limitations.
- {doc}`Range meanings and assumptions <calibrated_interval_semantics>` is the authoritative shared semantics reference.
- {doc}`Historical terminology <terminology>` and {doc}`regression terminology <terminology_thresholded_vs_probabilistic_regression>` help when reading older material.

## Looking for software details?

Use {doc}`Software & Integration <../../sections/software-integration>` for public
calls and integration, or {doc}`Technical reference <../reference/index>` for
architecture, errors, structures and parameters. They are not prerequisites for
understanding calibration or an explanation.

<!-- Entry-point tier: Tier 3. -->

```{toctree}
:maxdepth: 1

Optional capabilities: when and how <optional_capabilities>
Alternative explanations and ensured filters <alternatives>
Guarded explanations <guarded_explanations>
Terminology: thresholded vs probabilistic regression <terminology_thresholded_vs_probabilistic_regression>
```

<!-- Preserve section links from earlier review versions. -->
<span id="related-pages"></span>
