# Interval regression: first result

<span class="ce-choice-page" hidden></span>

**Goal:** read a predicted value and its interval, then inspect which feature
conditions contribute to the model’s response. The target is a number; this example asks
about the value itself, not the probability of an event.

## Choose where to run it

Choose one environment. The browser and Python examples use different datasets;
follow the selected guide's labels, units and setup. You can also read the captured
results below without running either route.

<div class="ce-route-grid" role="navigation" aria-label="Ways to run this example">
<a class="ce-route-card" href="expert-hub.html#expert-interval"><strong>Browser: California Housing</strong><span>Prepare and calibrate, then read a value and target-value interval.</span><span>Open the browser guide →</span></a>
<a class="ce-route-card" href="quickstart_regression.html"><strong>Python: numerical diabetes target</strong><span>Run setup, then the value-and-interval part of the regression tutorial.</span><span>Open the Python example →</span></a>
</div>

**Before running:** leave **Use Threshold** off for the browser housing exercise.
In Python, run the prerequisites through “Ask for a value and its interval”.
That tutorial's target is disease progression; do not attach housing units to it.

## Read the housing result

One captured case reports **0.5170**, with interval **[0.3087, 0.7948]**.
California Housing uses units of **$100,000**, so read this as a prediction of
**$51,700**, with a target-value interval of **$30,870–$79,480**.

This is a range for the numerical target. It does not mean “a 0.517 probability”,
and the displayed interval is not certainty that this particular outcome lies
inside it. Read its method-specific conditions below.

Now inspect one factual condition. Its weight describes a numerical model-response
difference in target units; its range belongs to that weight, not to the original
housing-value prediction. An alternative instead reports a prediction under a
different condition. Use the {doc}`interpretation guide <../foundations/how-to/interpret_explanations>`
with your result open if those quantities are hard to distinguish.

The housing numbers come from the dated {doc}`browser capture <expert-hub>`.
The local tutorial uses different data and will produce different values.

## Check your understanding

Can you name the predicted quantity, its units and the class or event if applicable?
Can you distinguish the prediction range, a factual weight and an alternative
prediction? If not, use {doc}`Interpret calibrated explanations <../foundations/how-to/interpret_explanations>`
with the result still open. You do not need to learn every API field to read one case.

<details><summary>Go deeper: how this mode produces its outputs</summary>

<span id="see-the-mode-specific-workflow"></span>

**Mode-specific workflow**

Follow the three activities: prepare the model and CE calibration, evaluate
with held-out test data, then reuse the same system with new-case features.
Only the last activity needs the new case; its target is not required.

<figure>
<picture>
<source media="(max-width: 600px)" srcset="../_static/figures/ce-mode-interval-mobile.svg">
<img src="../_static/figures/ce-mode-interval.svg" width="1100" height="1110" alt="Prepare: training data fit the model; separate labelled calibration data configure CE. Evaluate: test features query the same system; test targets are used only to check outputs. Use: new-case features query the same fitted model and CE state without its target or refitting the predictive model.">
</picture>
</figure>

[Open the full-size figure](../_static/figures/ce-mode-interval.svg).

The test targets are used to assess outputs, not to obtain them. The arrows
show information flow, not a required sequence of API calls.
Prediction and explanation operate on the same calibrated system; the
explanation call can obtain its own prediction. Read the result in this mode's
units and keep the prediction range separate from a feature-weight range.
For exact assumptions and limitations, use
{doc}`calibrated interval semantics <../foundations/concepts/calibrated_interval_semantics>`.


</details>

## Semantics for this example

- **Mode:** Interval regression (CPS; no threshold).
- **Calibration prerequisites:** a fitted model and separate labelled calibration data.
- **Guarantees:** use the method-specific statements in {doc}`calibrated interval semantics <../foundations/concepts/calibrated_interval_semantics>`.
- **Assumptions:** check the mode’s sampling conditions and calibration/deployment relationship there.
- **Non-guarantees:** no individual-case certainty or unconditional protection under drift.
- **Feature-level limits:** weight ranges are not causal or universal per-feature coverage guarantees.


## Continue from this result

**Next: {doc}`read the interpretation guide <../foundations/how-to/interpret_explanations>`
with this result open.** It explains predictions, weights and ranges using the
same terminology. You do not need to run a second environment first.


**Try another question:** return to {doc}`the big picture <index>`.
**Understand the construction:** {doc}`How CE Works <../sections/how-ce-works>`.
**Adapt to your data:** {doc}`Checking results <../practitioner/check_results>`.
**Find the exact call:** {doc}`Quick API <quick_api>`.

<!-- Entry-point tier: Tier 2. -->

<!-- Preserve previous section links. -->
<span id="continue-from-the-result"></span>
<span id="read-your-result"></span>

<span id="interval-regression-explain-a-numerical-prediction"></span>
