# CE big picture in 60 seconds

<span class="ce-choice-page" hidden></span>

A machine-learning model predicts an outcome from a case's **features**: the
information describing that case. The outcome is its **target**. In supervised
learning, training examples contain both features and known targets.

**Calibrated Explanations (CE) helps you inspect an individual prediction.** It
uses a fitted model and separate labelled calibration data to provide calibrated
prediction information and factual or alternative explanations, with reported ranges.

**Learn by doing:** start with the {doc}`Diabetes classification example <example-classification>`.
Or read the big picture below before choosing another question.

## What changes when you add CE?

<picture>
<source media="(max-width: 600px)" srcset="../_static/figures/ce-big-picture-mobile.svg">
<img src="../_static/figures/ce-big-picture.svg" width="960" height="510" alt="White boxes show labelled training data, a fitted model and a conventional prediction for a new case. Orange boxes show separate labelled calibration data and CE, using the same fitted model and new case, to return calibrated prediction information and factual or alternative explanations with reported ranges.">
</picture>

White boxes show the conventional workflow; orange boxes show CE's additions.
CE can use the same fitted model. Calibration uses separate labelled examples;
you then supply a new case's features to predict or explain it. Keep evaluation
data separate to check the resulting system. Other ML workflows can also include
calibration or uncertainty methods.

[Open the full-size figure](../_static/figures/ce-big-picture.svg).

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

Each example offers browser and local Python routes. Choose one; completing
both is optional.

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

## Go deeper when you need it

- **Why use CE?** {doc}`CE: What & Why <../sections/what-and-why>`.
- **How is it constructed?** {doc}`How CE Works <../sections/how-ce-works>`.
- **How do I use it in software?** {doc}`Software & Integration <../sections/software-integration>`.
- **What do the terms mean?** {doc}`Tasks, modes and capabilities <../foundations/concepts/tasks_modes_capabilities>`.

<!-- Entry-point tier: Tier 1. -->

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
