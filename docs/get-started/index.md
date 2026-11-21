# CE big picture in 60 seconds

Calibrated Explanations (CE) works with **supervised machine-learning models**:
models trained on examples with known outcomes. CE combines calibration with
explanations of individual model predictions. Start with the overview below;
follow the deeper links only when you need them.

## What CE adds to the workflow

<picture>
<source media="(max-width: 600px)" srcset="../_static/figures/ce-big-picture-mobile.svg">
<img src="../_static/figures/ce-big-picture.svg" width="960" height="510" alt="White boxes show labelled training data, a fitted model and a conventional prediction for a new case. Orange boxes show separate labelled calibration data and CE, using the same fitted model and new case, to return calibrated prediction information and factual or alternative explanations with reported ranges.">
</picture>

**White boxes:** the conventional prediction workflow shown here.
**Orange boxes:** CE's additions. Other ML workflows can also include uncertainty
or calibration methods. [Open the full-size figure](../_static/figures/ce-big-picture.svg).

1. **Learn from labelled training data.** Each observation has input **features**
   describing a case and a known **target**, the outcome to predict. Training
   produces the fitted model.
2. **Predict a new case.** The fitted model uses the new case's features to
   estimate its target. A class, value or score alone does not describe the
   feature conditions contributing to that response.
3. **Calibrate with separate labelled data.** CE uses the fitted model and
   calibration cases not used to fit it. This supports task-specific calibrated
   prediction information; CE need not retrain the model. Keep a separate
   evaluation set to check the resulting system.
4. **Read prediction information and explanations.** For the new case, inspect
   the calibrated output and its reported range. A factual explanation shows
   feature conditions and their weights with ranges; alternatives show what the
   model would report under different conditions. These comparisons help inspect
   the model; they do not establish real-world causes or prescribe a decision.

For the data roles and vocabulary, see
{doc}`Predictive tasks <../foundations/concepts/predictive_tasks>`.
For general background, see
[supervised learning — Google for Developers](https://developers.google.com/machine-learning/intro-to-ml/supervised).

## Task, mode and capability: three different choices

A **task** says what the model predicts: **classification** predicts a category;
**regression** predicts a numerical quantity. A **mode** says which question you
ask CE about that prediction. Regression supports both value and event questions.
A **capability** is an operation you perform, such as a factual explanation or
exploring alternatives; it is not another predictive task.

```{include} ../_shared/task-mode-map.md
:start-after: <!-- task-mode-map:start -->
:end-before: <!-- task-mode-map:end -->
```

In every mode, keep the prediction, factual weight and alternative prediction
separate. Probability differences use a probability scale; numerical differences
use the target's units. See the
{doc}`task, mode and capability guide <../foundations/concepts/tasks_modes_capabilities>`
for detailed distinctions and version-specific support. Conceptual modes are not
three interchangeable constructor settings.

## What can you rely on?

CE's guarantees and assumptions are **mode-specific**. Probability bounds,
target-value prediction intervals and feature-weight ranges do not share one
universal guarantee. Read the
{doc}`calibrated interval semantics <../foundations/concepts/calibrated_interval_semantics>`
for the precise statements and limitations; a range is not a guarantee for this
individual case, a causal effect or protection against distribution shift.

## Choose one step-by-step example

Choose your question first. Each example page then offers **browser** and
**local Python** routes; you do not need to complete both.

- **Which class, and how probable?** Start the
  {doc}`classification example <example-classification>`.
- **What numerical value, and within what interval?** Start the
  {doc}`interval regression example <example-interval>`.
- **How probable is an event on a numerical target?** Start the
  {doc}`event-probability example <example-event>`.

Browser and local tutorials can use different datasets and software versions.
Compare the workflow and output meanings, not identical numerical results.

**Go deeper:** {doc}`Why CE? <../sections/what-and-why>` ·
{doc}`How CE works <../sections/how-ce-works>` ·
{doc}`Read an explanation <../foundations/how-to/interpret_explanations>`.

Entry-point tier: Tier 1.

```{toctree}
:hidden:
:maxdepth: 1

Classification example <example-classification>
Interval regression example <example-interval>
Event-probability example <example-event>
Expert Hub: technical exploration <expert-hub>
Decision Lab: learn through decisions <decision-lab>
First explanation in Python <first-python-explanation>
Choose your task <../getting_started_60s>
```

<!-- Preserve links from earlier Quick Start candidates. -->
<span id="1-ce-in-60-seconds"></span>
<span id="2-choose-your-predictive-task-and-ce-mode"></span>
<span id="3-choose-your-browser-experience"></span>
<span id="4-explore-one-explanation"></span>
<span id="5-understand-what-you-see"></span>
<span id="6-continue-learning"></span>
<span id="choose-your-next-step"></span>
<span id="get-started"></span>
<span id="if-the-result-differs-or-no-plot-appears"></span>
<span id="install"></span>
<span id="keep-the-data-roles-separate"></span>
<span id="predictive-tasks"></span>
<span id="quickstart"></span>
<span id="quickstart-create-and-read-your-first-explanation"></span>
<span id="read-the-plot"></span>
<span id="run-the-complete-example"></span>
<span id="what-ce-adds"></span>
