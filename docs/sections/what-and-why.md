# CE: What & Why

What does CE add to a machine-learning prediction? Start here for the purpose
and ideas; no installation is needed.

## From a prediction to questions about it

A predictive model uses input features describing a case to estimate an outcome.
The outcome may be a category, such as a class label, or a numeric target.
A prediction alone does not explain how the model responds to the features
of that case. A score that looks like a probability also needs interpretation.

CE combines prediction calibration with local explanations. It uses separate
labelled calibration data and provides task-specific prediction information,
feature conditions and reported ranges. These quantities have different
meanings; a prediction range and a feature-weight range are not interchangeable.

## Choose the question you want answered

| Your question | Shared explanation |
| --- | --- |
| What can I ask CE to predict? | {doc}`Tasks and capabilities <../tasks/index>`. |
| How do I read a prediction and its explanation? | {doc}`Interpretation guide <../foundations/how-to/interpret_explanations>`. |
| How does CE relate to other explanation methods? | {doc}`Method comparison <../compare>`. |
| What do the terms mean? | {doc}`Glossary and terminology <../foundations/concepts/terminology>`. |
| What assumptions and limits matter? | {doc}`Calibrated interval semantics <../foundations/concepts/calibrated_interval_semantics>`. |

Reported ranges do not establish causal effects. Read their method-specific
meaning with the assumptions on the shared semantics page.

**Try it:** {doc}`Quickstart <../get-started/index>`.
**Go deeper:** {doc}`How CE Works <how-ce-works>` connects the workflow to its outputs.

```{toctree}
:maxdepth: 1
:hidden:

Calibrated Explanations comparisons (CE-first) <../compare>
```
