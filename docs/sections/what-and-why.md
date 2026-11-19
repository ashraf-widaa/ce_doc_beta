# CE: What & Why

<!-- Preserve descriptive anchors from the previous review layout. -->
<span id="choose-the-question-you-want-answered"></span>
<span id="from-a-prediction-to-questions-about-it"></span>


What can you learn about a prediction before relying on it? This route explains
the purpose of CE without requiring code or a statistics course.

## Start with the question, not the software

A predictive model estimates a target from a case's input features. A classifier
might estimate a category; a regressor a numeric quantity. The shared
{doc}`predictive-task page <../foundations/concepts/predictive_tasks>` defines
these terms. CE combines calibration with local explanations of model responses.

Prediction, explanation and decision answer different questions:

| Question | Information you need |
| --- | --- |
| What does the model predict? | The target, class or event definition and its output scale. |
| What does the reported range describe? | Which quantity has a range and which method/conditions support it. |
| Why does the model respond this way? | Feature conditions and comparison responses for this case. |
| What should I do? | The prediction plus costs, constraints, relevant evidence and decision responsibility. |

A housing-value estimate, for example, is not itself a purchase decision. An
explanation can help you inspect a model response without establishing that a
particular intervention will change the real outcome.

## What CE adds

CE uses separate labelled calibration data with a trained model. Depending on
the task, it returns class-probability information, numeric prediction intervals
or probabilities for events on a numeric target. It also provides factual and
alternative explanations where supported by the chosen interface and version.

A factual explanation describes conditions holding for the query, with weights
and ranges. An alternative asks what the model would report under another
condition. These are model comparisons, not proofs of causation.

Read {doc}`tasks, modes and capabilities <../foundations/concepts/tasks_modes_capabilities>`
for the distinction, or {doc}`inspect a real browser result <../get-started/expert-hub>`
without installing anything.

## Why calibration and explanation belong together

Accuracy checks predictions against outcomes; probability calibration concerns
how probability reports relate to observed frequencies. Explaining a model's
score does not by itself calibrate that score. Conversely, prediction uncertainty
alone does not explain feature conditions for the particular query.

The {doc}`statistical background <../foundations/concepts/calibration_background>`
develops those ideas. CE's different ranges must still be read separately;
they do not share one universal guarantee.

## Decide where CE fits

You need a compatible predictive model and labelled calibration data with the
required feature representation. Consider the task, available data, intended
output and evaluation plan before selecting a tool. Use the
{doc}`comparison with SHAP, LIME and other approaches <../compare>` for different
questions and outputs, not an unsupported performance ranking.

**Start with an experience:** {doc}`browser Quickstart <../get-started/index>`.
**Learn the construction:** {doc}`How CE Works <how-ce-works>`.
**Check exact limits:** {doc}`source-version semantics <../foundations/concepts/calibrated_interval_semantics>`.
**Look up a term:** {doc}`Glossary <../glossary/index>`.

```{toctree}
:maxdepth: 1
:hidden:

Calibrated Explanations comparisons (CE-first) <../compare>
```
