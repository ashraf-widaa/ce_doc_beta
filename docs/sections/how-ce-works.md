# How CE Works

How does a trained model become the basis of a calibrated explanation?
Start with the data roles, then follow the mechanism relevant to your task.

## Follow the workflow

| Stage | What it does | Where to continue |
| --- | --- | --- |
| Fit the model | Learn from model-fitting data. | The {doc}`classification <../get-started/quickstart_classification>` and {doc}`regression <../get-started/quickstart_regression>` tutorials show the data splits. |
| Calibrate | Use separate labelled calibration data for the task-specific calibration procedure. | {doc}`Shared concepts <../foundations/concepts/index>`. |
| Query and explain | Use the features of a query case to obtain prediction information and explanations. | {doc}`Read CE explanations <../foundations/how-to/interpret_explanations>`. |

Calibration data is not the model-fitting set or the held-out evaluation set.
For general background, see [dividing datasets](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets).
The CE tutorials show the additional calibration split explicitly.

## Choose an output to understand

- **Class predictions:** use the {doc}`classification task guide <../tasks/classification>`
  beside the shared {doc}`semantics reference <../foundations/concepts/calibrated_interval_semantics>`.
- **Numeric predictions and threshold events:** {doc}`probabilistic and interval regression <../foundations/concepts/probabilistic_regression>` distinguishes the questions.
- **Factual and alternative explanations:** the {doc}`interpretation guide <../foundations/how-to/interpret_explanations>`
  and {doc}`alternatives guide <../foundations/concepts/alternatives>` connect rules to model responses.
- **Assumptions and guarantees:** use {doc}`calibrated interval semantics <../foundations/concepts/calibrated_interval_semantics>`
  as the authoritative reference for this source version.

A probability bound, a target prediction interval and a feature-weight range
must be interpreted separately. None should be treated as evidence of a causal effect.

**See the ideas in code:** {doc}`CE in Practice <in-practice>`.
**Explore the papers:** {doc}`theory and literature <../researcher/advanced/theory_and_literature>`.

```{toctree}
:maxdepth: 1
:hidden:

Shared foundations <../foundations/index>
Read CE explanations <../foundations/how-to/interpret_explanations>
```
