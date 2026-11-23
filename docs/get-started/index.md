# Quick Start: the CE big picture

<span class="ce-choice-page" hidden></span>

A machine-learning model predicts an outcome from a case's **features**: the
information describing that case. The outcome is its **target**. In supervised
learning, training examples contain both features and known targets.

**Calibrated Explanations (CE) helps you inspect an individual prediction.** It
uses a fitted model and separate labelled calibration data to provide calibrated
prediction information and factual or alternative explanations, with reported ranges.

Read the workflow below, choose a prediction question, then inspect or run one
example. You do not need to install CE to begin.

**Prefer to see a result first?** {ref}`Read one Iris prediction without running code <classification-one-case>`,
or {doc}`run the same case in Python <first-python-explanation>`.

## What changes when you add CE?

<figure>
<picture>
<source media="(max-width: 600px)" srcset="../_static/figures/ce-big-picture-mobile.svg">
<img src="../_static/figures/ce-big-picture.svg" width="1100" height="680" alt="White boxes show training data, the fitted model and a new case leading to a conventional prediction. Orange boxes add separate labelled calibration data and CE using the same fitted model and new-case features. Four output boxes distinguish prediction, its task-specific range, factual conditions with weights and ranges, and alternative conditions with predictions and ranges.">
</picture>
<figcaption>CE uses the same fitted model. The orange outputs distinguish quantities; they are not four required API calls.</figcaption>
</figure>

[Open the full-size figure](../_static/figures/ce-big-picture.svg).

Read the figure from the inputs to the outputs:

1. **Fit the predictive model.** Training examples have features and known targets.
   The fitted model can predict a class, numerical value or score for a new case.
2. **Add separate calibration data.** CE uses labelled examples that were not used
   to fit the model. Calibrating does not retrain that predictive model. Keep
   evaluation data separate to check the resulting system.
3. **Supply the new case's features.** Its unknown target is not an input. CE uses
   the fitted model and calibration to produce information for your chosen question.
4. **Read the different outputs separately.** Identify the prediction and its range,
   then inspect a factual condition and an alternative. Their quantities are
   explained below. Other ML workflows can also include calibration and uncertainty methods.

## Choose the question you want to answer

A **task** says what the model predicts. Classification predicts a category,
with two classes (binary) or more than two (multiclass). Regression predicts a
number. A **mode** is the question you ask CE about that prediction:

- **Which class, and how probable?** Follow the
  {doc}`classification example <example-classification>`.
- **What value, and within what interval?** Follow the
  {doc}`numerical prediction example <example-interval>`.
- **How probable is an event, such as a value below a threshold?** Follow the
  {doc}`event-probability example <example-event>`.

Each example explains its output and offers two ways to run it: **in the browser**
without installation, or **locally in Python**. Choose one; completing both is optional.
Installation belongs to the Python route, not a separate step for every reader.

## What can an explanation tell you?

These are explanation **capabilities**, not additional predictive tasks:

- **Factual:** which feature conditions contribute to the model's response for
  this case, with weights and reported ranges?
- **Alternative:** what would the model report under a different feature condition?

An alternative describes the model; it does not establish that changing the
real-world case will cause that outcome.

## What do the ranges mean?

First name the quantity. Class and event probabilities have probability bounds;
a numerical prediction interval is in the target's units. Feature-weight ranges
are a separate quantity. They do not share one universal guarantee.

Guarantees depend on the mode and its assumptions. Use the
{doc}`range meanings and limitations <../foundations/concepts/calibrated_interval_semantics>`
when interpreting a result; a range is not certainty about an individual case
or protection against distribution shift.

## After your first result

Before adding more features or methods, check that you can answer:

- What quantity was predicted, and for which class or event if applicable?
- Which range belongs to the prediction, and what does it mean in this mode?
- What does one factual weight compare, and how does an alternative prediction differ?

Use the shared {doc}`interpretation guide <../foundations/how-to/interpret_explanations>`
with the result open if needed. The next step depends on your goal:

- **Apply CE to your own data:** follow {doc}`the practical sequence <../sections/in-practice>`
  to adapt the workflow and check held-out results.
- **Understand why CE exists:** read {doc}`CE: What & Why <../sections/what-and-why>`.
- **Understand the construction:** follow {doc}`How CE Works <../sections/how-ce-works>`.
- **Connect it to an application:** use {doc}`Software & Integration <../sections/software-integration>`.

<span id="go-deeper-when-you-need-it"></span>

<!-- Entry-point tier: Tier 1. -->

```{toctree}
:hidden:
:maxdepth: 1

Classification example <example-classification>
Interval regression example <example-interval>
Event-probability example <example-event>
First explanation in Python <first-python-explanation>
Browser workflow: Expert Hub <expert-hub>
Decision practice: Decision Lab <decision-lab>
```

<!-- Preserve previous section links. -->
<span id="1-ce-in-60-seconds"></span>
<span id="2-choose-your-predictive-task-and-ce-mode"></span>
<span id="3-choose-your-browser-experience"></span>
<span id="4-explore-one-explanation"></span>
<span id="5-understand-what-you-see"></span>
<span id="6-continue-learning"></span>
<span id="choose-one-step-by-step-example"></span>
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
<span id="task-mode-and-capability-three-different-choices"></span>
<span id="what-can-you-rely-on"></span>
<span id="what-ce-adds"></span>
<span id="what-ce-adds-to-the-workflow"></span>

<span id="ce-big-picture-in-60-seconds"></span>
