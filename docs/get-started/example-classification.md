# Classification: explain a class prediction

**Your question:** Which class is predicted, and what probability information supports it?

The browser example uses Pima Diabetes: the target is a binary class. The existing local tutorial uses Iris species, a multiclass task. These are different cases; the local tutorial records a multiclass-bound limitation.

## See the mode-specific workflow

<figure>
<picture>
<source media="(max-width: 600px)" srcset="../_static/figures/ce-mode-classification-mobile.svg">
<img src="../_static/figures/ce-mode-classification.svg" width="1000" height="570" alt="Classification: fitted model and separate labelled calibration data, method-specific calibration, new-case features, prediction information and factual or alternative explanations.">
</picture>
</figure>

[Open the full-size figure](../_static/figures/ce-mode-classification.svg).

The arrows show information flow, not a required sequence of API calls.
Prediction and explanation operate on the same calibrated system; the
explanation call can obtain its own prediction. Read the result in this mode's
units and keep the prediction range separate from a feature-weight range.
For exact assumptions and limitations, use
{doc}`calibrated interval semantics <../foundations/concepts/calibrated_interval_semantics>`.

## Choose where to run it

### In your browser

No installation is needed. Follow the {ref}`Expert Hub guide: Diabetes classification <expert-classification>`.
Select Diabetes, prepare and calibrate the model, choose a test case, then inspect Factual and Alternatives.

The guide contains dated real screenshots, controls and output interpretation.
If the application is unavailable, use those captures or choose the local route.

### Install and run locally

Use {doc}`Installation <installation>` if needed, then follow the existing
{doc}`classification tutorial <quickstart_classification>` from the beginning. It includes data preparation, separate
training/calibration/evaluation roles, model fitting and explanation calls.
For a full installation-to-first-plot walkthrough, use {doc}`First explanation in Python <first-python-explanation>`.

## Read your result

Class probabilities and their reported bounds. A factual weight describes a difference in the explained probability; an alternative reports a probability under another condition.

Identify one feature condition, its weight and its range, then one alternative
and its reported prediction. Use {doc}`the shared interpretation guide <../foundations/how-to/interpret_explanations>`
to distinguish them. An alternative describes the model response, not an
established effect of changing the real-world case.

## Semantics for this example

- **Mode:** Classification (Venn–Abers).
- **Calibration prerequisites:** a fitted model and separate labelled calibration data.
- **Guarantees:** use the method-specific statements in {doc}`calibrated interval semantics <../foundations/concepts/calibrated_interval_semantics>`.
- **Assumptions:** check the mode’s sampling conditions and calibration/deployment relationship there.
- **Non-guarantees:** no individual-case certainty or unconditional protection under drift.
- **Feature-level limits:** weight ranges are not causal or universal per-feature coverage guarantees.

## Continue from the result

Return to {doc}`the big picture <index>` to change your question. For the
construction, read {doc}`How explanations are built <../foundations/concepts/how_explanations_are_built>`.
Before adapting an example, use {doc}`Checking results on your data <../practitioner/check_results>`.

Entry-point tier: Tier 2.
