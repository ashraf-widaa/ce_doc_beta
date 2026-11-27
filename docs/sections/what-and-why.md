# CE: What & Why

<span class="ce-course-step" hidden></span>

A model's prediction tells you what it estimates. Before you rely on it, you
may also want to know three more things:

- **How certain is it?** What range is reported around the prediction, and what
  does that range mean?
- **Why this prediction?** Which feature conditions in this case contribute to it?
- **What if?** What would the model report if one of those conditions were different?

**Calibrated Explanations (CE)** is an open-source Python library that answers
these questions together, around a model you have already trained. It uses
separate labelled calibration data to report calibrated prediction information
and explanations, each with a range.

You do not need to install CE or learn its API to read this page. By the end,
you should be able to say what CE adds and choose an example to try.

**Reading route:** this page →
{doc}`predictive tasks and data roles <../foundations/concepts/predictive_tasks>` →
{doc}`tasks, modes and capabilities <../foundations/concepts/tasks_modes_capabilities>`.
Each page links to the next one. No installation is needed to read them.

## Start with a familiar prediction

Suppose a model estimates the median housing value in an area. It uses
**features**, such as median income and location, to estimate the **target**:
the housing value.

- Predicting a number is **regression**.
- Predicting a category, such as an Iris flower's species, is **classification**.

Both are supervised learning: the training examples include features and known
targets. The {doc}`predictive-task guide <../foundations/concepts/predictive_tasks>`
defines these terms. [Google's supervised-learning introduction](https://developers.google.com/machine-learning/intro-to-ml/supervised)
is optional background.

The predicted number or class is useful, but it leaves the three questions
above open. Answering them describes the prediction and the model's behaviour.
It does not, by itself, tell you what to do.

(what-ce-adds-to-a-conventional-workflow)=
## What CE adds to a conventional workflow

The figure shows supervised machine learning (blue, top) and what
Calibrated Explanations adds to it (orange, below).

<figure>
<picture>
<source media="(max-width: 600px)" srcset="../_static/figures/ce-adds-to-workflow-narrow.svg">
<img src="../_static/figures/ce-adds-to-workflow.svg" width="920" height="470" alt="Top row, supervised machine learning, in blue: labelled training data train an ML model, which becomes a fitted predictive model; given an instance (test data or a new case, features only) it returns a prediction, a class or a value. Below, Calibrated Explanations, in orange: CE uses the same fitted model, not retrained, with separate labelled calibration data not used for training, and the same instance. It returns four things: 1, the prediction; 2, uncertainty by task, shown as probability bounds on a 0 to 1 scale or an interval in the target's units; 3, a factual explanation (why?); 4, alternative explanations (what if?). Each explanation reports its own ranges.">
</picture>
<figcaption><strong>What CE adds to supervised machine learning.</strong> CE reuses the same fitted model and the same instance. It adds separate calibration data and returns four outputs.</figcaption>
</figure>

[Download the figure (SVG)](../_static/figures/ce-adds-to-workflow.svg).

**Supervised machine learning (blue).** Labelled training data (features plus
known targets) train a model. Given an **instance**, the fitted model returns
a prediction: a class or a value. An instance is one case to predict or
explain: a row of test data or a new case, given as features only. Its target
is not needed.

**With Calibrated Explanations (orange).** CE keeps that same fitted model and
does not retrain it. It adds **separate labelled calibration data** that were
not used for training. For the same instance, CE returns four outputs:

1. **Prediction**: the calibrated prediction for the instance.
2. **Uncertainty, by task**: probability bounds on a 0–1 scale, or an interval
   in the target's units.
3. **Factual explanation** (*why?*): which conditions in this case contribute,
   as feature weights with ranges.
4. **Alternative explanations** (*what if?*): what the model would report under
   other feature conditions, as predictions with ranges.

**Held-out evaluation, before relying on either side.** Test features go to the
model or the CE system to obtain outputs. The test targets are kept aside and
used only to check those outputs. They never enter a prediction or explanation.

What the range means depends on the question you ask, called the
{term}`mode <CE mode>`:

| Your question | Mode | CE reports | Calibration method |
| --- | --- | --- | --- |
| Which class, and how probable? | Classification | Class probability with bounds | Venn–Abers |
| What numerical value? | Interval regression | Value with an interval in target units | Conformal predictive system |
| How probable is a numerical event, such as a value at most a budget? | Thresholded (probabilistic) regression | Event probability with bounds | Conformal predictive system scores, calibrated with Venn–Abers |

The same regressor can serve both regression modes; the call decides which.
The {doc}`task, mode and capability guide <../foundations/concepts/tasks_modes_capabilities>`
explains the three words.

In code, the same steps are `fit(X_train, y_train)`, then
`calibrate(X_cal, y_cal)`, then `predict(X)`, `explain_factual(X)` or
`explore_alternatives(X)`. The last three take features only.

The figure compares CE with *basic* supervised learning. Real systems can add their own
calibration or explanation tools. CE's contribution is to provide calibrated
prediction information and both kinds of explanation together, around one model.

## Why an explanation helps

When it is hard to see how a model turns inputs into outputs, it is often
called a **black box**. Explainable AI (**XAI**) studies ways to make model
behaviour easier to inspect. An explanation can focus on one case instead of
summarising the whole model.

CE offers two complementary views of one case:

- A **factual explanation** describes conditions that hold for the case and how
  much each contributes to the model's response.
- An **alternative explanation** shows what the model would report under
  another feature condition.

For housing, these help you inspect how the model responds to income or
location. They do not prove that changing either would cause a particular price.

## Why calibration matters too

Explaining a score does not make it a calibrated probability. Calibration is
about whether reported probabilities match how often outcomes occur across
cases. Accuracy and calibration answer different questions: a model can classify
many cases correctly while reporting probabilities that need calibration.

CE uses the fitted model and the calibration data to build prediction
information that fits the task and question, then explains that calibrated
response. The {doc}`calibration background <../foundations/concepts/calibration_background>`
gives the intuition and statistics. {doc}`How CE Works <how-ce-works>` covers
the precise methods and their conditions.

## Read one result: prediction, range, explanation

Read three things together: **the prediction**, **the range for that
quantity**, and **the explanation**. A factual weight and an alternative
prediction are different quantities. Read each range on its own scale.

For example, a housing-value interval is in monetary units. Bounds for the
probability that the value is below a budget are on a probability scale. Bars
that look similar in a plot do not share a meaning or a guarantee. The
{doc}`task and mode guide <../foundations/concepts/tasks_modes_capabilities>`
connects each question to its output.

## When to consider CE, and its limits

Consider CE when you have:

- a fitted classifier or regressor that CE supports;
- suitable labelled calibration data, separate from the training data;
- a need to inspect predictions together with their uncertainty and explanations.

You still need an evaluation plan and domain knowledge to judge whether the
outputs are useful for your application. If you know SHAP or LIME, the
{doc}`comparison page <../compare>` relates the questions and quantities each
method addresses. CE does not replace every explanation method.

Keep these limits in mind:

- The ranges are only as trustworthy as the calibration data are representative
  of the cases you query. Distribution shift can break this.
- Explanations describe the model's behaviour. They do not establish causes,
  feasible interventions or a correct decision.
- Prediction bounds and feature-weight ranges do not share one guarantee. The
  {doc}`range meanings and limitations <../foundations/concepts/calibrated_interval_semantics>`
  state the conditions for each.

## Where the ideas come from

CE addresses one research question: how to explain individual predictions
together with calibrated uncertainty information. The
[classification paper](https://doi.org/10.1016/j.eswa.2024.123154) introduces CE
with uncertainty information and counterfactuals. The
[regression paper](https://doi.org/10.1007/s10994-024-06642-8) extends it to
numerical targets. The {doc}`citation list <../citing>` also covers multiclass and
conditional developments.

The papers and their assumptions govern the formal results. A worked example or
a successful code cell adds no further guarantee. This documentation says
"alternative" for these model comparisons, without assuming they are real-world
causal or actionable counterfactuals.

## What to read next

Continue with {doc}`predictive tasks and data roles <../foundations/concepts/predictive_tasks>`.
From there, the pages follow one Iris example through calibration, explanation
and interpretation. You can read them without running Python. If you mainly want
to know how the method is built, start with the
{doc}`How CE Works overview <how-ce-works>`; it leads to the same pages.

The {ref}`reading map <guided-reading-route>` lists those pages in order and
what each one teaches.

Prefer to start with code? The {doc}`complete plotted Python example <../get-started/first-python-explanation>`
uses the same Iris case. You do not need to do both.

```{toctree}
:maxdepth: 1
:hidden:

Predictive tasks and data roles <../foundations/concepts/predictive_tasks>
Compare CE with other approaches <../compare>
```

<!-- Entry-point tier: Tier 1. -->

<!-- Preserve earlier section links. -->
<span id="begin-with-one-prediction"></span>
<span id="choose-the-question-you-want-answered"></span>
<span id="decide-where-ce-fits"></span>
<span id="from-a-prediction-to-questions-about-it"></span>
<span id="start-with-the-question-not-the-software"></span>
<span id="what-ce-adds"></span>
<span id="why-calibration-and-explanation-belong-together"></span>
<span id="why-calibration-matters-as-well"></span>
<span id="what-ce-adds-to-an-individual-result"></span>
<span id="when-should-you-consider-ce"></span>
<span id="connect-the-motivation-to-the-research"></span>
<span id="continue-from-motivation-to-understanding"></span>
<span id="continue-the-guided-introduction"></span>
<span id="continue-as-a-guided-tutorial"></span>

**Next page:** {doc}`Predictive tasks and data roles <../foundations/concepts/predictive_tasks>`.
