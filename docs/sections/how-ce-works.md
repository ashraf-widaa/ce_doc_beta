# How CE Works

<!-- Preserve descriptive anchors from the previous review layout. -->
<span id="choose-an-output-to-understand"></span>
<span id="follow-the-workflow"></span>


How does CE turn a trained model and calibration data into prediction information
and an explanation? This route moves from the workflow to mechanisms and their
statistical conditions. You can stop at the depth needed for your question.

## Follow the same model through the workflow

```{include} ../_shared/ce-workflow.md
```

The model-fitting set, calibration set and evaluation set have different roles.
A query uses features of the case to predict or explain. Read the shared
{doc}`data-role definitions <../foundations/concepts/predictive_tasks>` before
interpreting a split or reusing data.

## Choose what to understand next

| Your question | Shared explanation | Afterward |
| --- | --- | --- |
| Which output answers my task? | {doc}`Tasks, modes and capabilities <../foundations/concepts/tasks_modes_capabilities>`. | Try that route in the browser or Python. |
| What is calibration, and how do the statistical methods differ? | {doc}`Calibration and statistical background <../foundations/concepts/calibration_background>`. | Check source-version assumptions and literature. |
| How does a feature become a weight or alternative? | {doc}`How explanations are built <../foundations/concepts/how_explanations_are_built>`. | Read the resulting rules and plot. |
| How do I interpret an actual object or figure? | {doc}`Interpret CE explanations <../foundations/how-to/interpret_explanations>`. | Compare one real example. |
| What can the method guarantee? | {doc}`Canonical interval semantics <../foundations/concepts/calibrated_interval_semantics>`. | Check that the assumptions fit the intended use. |

## Keep the quantities separate

Class-probability bounds concern a probability. A numeric prediction interval
concerns target values in their units. A threshold-event probability concerns a
defined event on that target. Feature-weight ranges concern model-response
comparisons. A similar-looking bar does not make them interchangeable.

The {doc}`regression-mode guide <../foundations/concepts/probabilistic_regression>`
shows how the same model can answer value and event questions. The
{doc}`explanation-construction page <../foundations/concepts/how_explanations_are_built>`
separates baseline predictions, factual weights and alternative predictions.

## Go deeper without restarting

Use {doc}`shared foundations <../foundations/index>` as a topic collection,
and {doc}`theory and literature <../researcher/advanced/theory_and_literature>`
for papers. Statistical claims need their method, assumptions and version;
this introduction does not strengthen the canonical guarantees or resolve
open author-review issues.

**See it happen:** {doc}`browser Quickstart <../get-started/index>`.
**Run a task:** {doc}`CE in Practice <in-practice>`.
**Integrate an implementation:** {doc}`Software & Integration <software-integration>`.

```{toctree}
:maxdepth: 1
:hidden:

Shared foundations <../foundations/index>
Read CE explanations <../foundations/how-to/interpret_explanations>
```
