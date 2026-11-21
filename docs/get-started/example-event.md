# Probabilistic regression: explain an event probability

**Your question:** How probable is a specified event on a numerical target?

Use a regression model, but change the question from a value to an event. In browser California Housing, P(Y ≤ 3) asks whether the value is at most $300,000. Enter 3 in that dataset’s units, not 300000. The local regression tutorial uses its own target and threshold.

## See the mode-specific workflow

<figure>
<picture>
<source media="(max-width: 600px)" srcset="../_static/figures/ce-mode-event-mobile.svg">
<img src="../_static/figures/ce-mode-event.svg" width="1000" height="570" alt="Event-probability regression: fitted model and separate labelled calibration data, method-specific calibration, new-case features, prediction information and factual or alternative explanations.">
</picture>
</figure>

[Open the full-size figure](../_static/figures/ce-mode-event.svg).

The arrows show information flow, not a required sequence of API calls.
Prediction and explanation operate on the same calibrated system; the
explanation call can obtain its own prediction. Read the result in this mode's
units and keep the prediction range separate from a feature-weight range.
For exact assumptions and limitations, use
{doc}`calibrated interval semantics <../foundations/concepts/calibrated_interval_semantics>`.

## Choose where to run it

### In your browser

No installation is needed. Follow the {ref}`Expert Hub guide: California Housing threshold probability <expert-event>`.
Prepare and calibrate California Housing first, then enable Use Threshold, enter 3 and inspect a test case. The linked guide records a misleading application badge; read the output as an event probability.

The guide contains dated real screenshots, controls and output interpretation.
If the application is unavailable, use those captures or choose the local route.

### Install and run locally

Use {doc}`Installation <installation>` if needed, then follow the existing
{doc}`regression tutorial <quickstart_regression>` from the beginning. It includes data preparation, separate
training/calibration/evaluation roles, model fitting and explanation calls.
At “Interval and threshold predictions”, follow the threshold call and its probability output. Use the event factual and alternative calls with the same threshold; the preceding value-route explanations remain in target units.

## Read your result

The event definition, its probability and reported probability bounds. Factual differences concern the event probability. Do not read these bounds as an interval for a house value.

Identify one feature condition, its weight and its range, then one alternative
and its reported prediction. Use {doc}`the shared interpretation guide <../foundations/how-to/interpret_explanations>`
to distinguish them. An alternative describes the model response, not an
established effect of changing the real-world case.

## Semantics for this example

- **Mode:** Probabilistic regression (CPS + Venn–Abers).
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
