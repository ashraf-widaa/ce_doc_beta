# Explore the Expert Hub

Use this route to inspect CE's technical workflow without installing Python.
The instructions below were tested with built-in examples on 19 November 2026.
This application is under active development; these are captured observations,
not a promise that all labels or values remain unchanged.

**Open the [Expert Hub](https://calibrated-explanations-demo.ju.se/expert).**
Use a built-in example first. Uploads and advanced options are not prerequisites.

## Classification: inspect one Diabetes case

1. On **Project**, under **Quick Start — Demo Datasets**, choose
   **Diabetes (Binary Classification)**.
2. Keep the displayed defaults: 20% test, 33% calibration of all rows and
   47% proper training. Select **Next: Prepare & Calibrate**.
3. Select **Prepare Random Forest + Calibrate**. Wait for **Calibrated** and
   **Status: ready**, then choose **Next: Explain**.
4. Under **Test Set Instances**, select row **0**. Inspect **Factual**.
5. Open **Alternatives (n)**. The count can initially be zero before the
   alternatives are loaded. Compare one condition and its reported prediction.
6. Optionally open **Predict** and select **Run Predictions** to inspect a batch.

If the optional feedback prompt interrupts, **Not now** dismisses it. Feedback
submission is not part of this tutorial.

```{figure} browser_assets/expert-calibrated.png
:alt: Actual Expert Hub Diabetes screen with Calibrated status, ready model configuration and Next Explain action.
:width: 100%

A real calibration-ready screen. Start with the status and next action; the diagnostic explorer is optional depth.
```

The Diabetes example is a binary classifier using public Pima data. It is an
educational example, not diagnosis or treatment advice. The table uses abbreviated
feature names such as `plas`, `mass` and `preg`; do not assume another tutorial's
feature labels or selected patient are identical.

## Read the factual result, then an alternative

In one captured trial, row 0 reported **P(Y=positive)=0.7448**, with bounds
**[0.7273, 0.7959]**. The condition `plas > 139.50` had reported weight
`+0.517`, range `[0.510, 0.538]`. The alternative `plas < 147.50` reported
probability `0.2719`, bounds `[0.2487, 0.2811]`. Your session can differ.

Read these as three different things: the original probability, a factual
weight, and an alternative probability. The alternative is a model-response
comparison, not a recommendation to change a patient's glucose level.

```{figure} browser_assets/expert-factual-focus.png
:alt: Actual focused Expert Hub panel with Diabetes factual rule conditions, weight ranges and interactive plots.
:width: 100%

Actual rule and plot panel for the captured case. Select the image for full-size access; the original prediction values are given just above.
```

```{figure} browser_assets/expert-alternatives.png
:alt: Captured Expert Hub alternative conditions with probability estimates and bounds for the same Diabetes query.
:width: 100%

Alternatives report predictions under different conditions. Compare their output scale and class with the original query.
```

{download}`Download the complete factual-page capture <browser_assets/expert-factual.png>`.

These captures preserve the real interface. On a phone, opening the
full-size image may be easier than reading every label in the page-width view.
Use the {doc}`shared interpretation guide <../foundations/how-to/interpret_explanations>`
for the returned quantities, not colour alone.

## Numeric prediction: California Housing

Repeat the preparation flow using **California Housing (Regression)**. On
**Explain**, leave **Use Threshold (probabilistic regression)** off and select a
row. Inspect the numeric prediction, target-value interval and alternatives.

In the captured row-0 trial the primary output was `0.5170`, interval
`[0.3087, 0.7948]`. This Sklearn dataset's target is in **$100,000 units**:
about $51,700 with an interval of [$30,870, $79,480]. The Python CSV-based
Housing example in another review version uses different features/units;
its numbers are not expected browser output.

## Event probability: a threshold on the same target

Use the **switch** beside **Use Threshold (probabilistic regression)**;
clicking its text label did not toggle it in the reviewed UI. Enter **3** in
**Threshold**, then select a row. For this dataset, 3 means **$300,000**.
The generic placeholder `e.g. 250000` is not a statement of the dataset's units.

The captured query reported **P(Y ≤ 3)=0.9986**, bounds **[0.9986, 1.0000]**.
The `Longitude < -121.63` alternative reported `0.9331 [0.9319,0.9418]`.
Those are event probabilities, not dollar intervals. The selected-case factual
and alternative paths worked; the final threshold batch was still running at
capture, so its completion was not verified in this review.

## Interface qualifications to keep visible

```{warning}
The reviewed UI retains a **90% Conformal Interval / Conformal (CPS)** badge
beside some threshold probability output. It also displays a regression header
`ŷ = 1.0` alongside a different primary numeric prediction, and its threshold
narrative can label decreasing alternatives as increases. These need maintainer
review. Use the event definition, raw numeric cards and units; do not copy the
misleading labels into an interpretation or silently correct screenshots.
```

Iris was listed but not run in this browser review. Custom uploads, all advanced
settings and backend statistical correctness were not exhaustively tested.
The browser service's capabilities and version are not automatically the same
as the installed Python library.

**Change activity:** {doc}`Decision Lab <decision-lab>` for decision context;
{doc}`first Python explanation <first-python-explanation>` for local code;
{doc}`statistical background <../foundations/concepts/calibration_background>`
for concepts; {doc}`canonical semantics <../foundations/concepts/calibrated_interval_semantics>`
for source-version conditions and non-guarantees.
