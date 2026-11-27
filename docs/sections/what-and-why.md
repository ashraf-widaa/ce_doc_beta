# CE: What & Why

<span class="ce-course-step" hidden></span>

A prediction tells you what a model estimates. Before using it, you may also
want to know what its reported range means, which information contributes to
the prediction, and what the model would report under different conditions.
**Calibrated Explanations (CE) brings these questions into one workflow.**

CE is an open-source Python library. It uses a trained model and separate labelled
calibration examples to provide calibrated prediction information and feature
explanations with reported ranges.

Start here to understand the ideas. You do not need to install CE or learn its
API first. By the end, you should be able to explain what CE adds and decide
which question to explore in an example.

**Your reading route:** this introduction →
{doc}`predictive tasks and data roles <../foundations/concepts/predictive_tasks>` →
{doc}`tasks, modes and capabilities <../foundations/concepts/tasks_modes_capabilities>`.
The shared chapters continue from there; no installation is needed to read them.

## Start with a familiar prediction

Suppose a model estimates the median housing value in an area. It uses
**features**, such as median income and location, to estimate the **target**:
the housing value. A model predicting a number performs **regression**. A model
predicting a category, such as an Iris flower's species, performs **classification**.
Both are supervised learning: training examples include features and known targets.

The predicted number or class is useful, but leaves questions open. What range
is reported around it? Which conditions distinguish this case? What if one of
those conditions were different? These questions concern the prediction and
the model's behavior; answering them does not automatically tell us what to do.

For the vocabulary and data roles, use the shared
{doc}`predictive-task guide <../foundations/concepts/predictive_tasks>`.
[Google's supervised-learning introduction](https://developers.google.com/machine-learning/intro-to-ml/supervised)
is optional general background.

## Why an explanation helps

When a model's mapping from inputs to outputs is difficult to inspect directly,
it is often described as a **black box**. Explainable AI (**XAI**) studies ways
to make model behavior easier to inspect. An explanation can focus on one case
rather than trying to summarize the whole model.

CE offers two complementary views. A **factual explanation** describes conditions
holding for the case and their model-response contributions. An **alternative
explanation** asks what the model would report under another feature condition.
For housing, these can help you inspect how the model responds to income or
location. They do not prove that changing either will cause a particular sale price.

## Why calibration matters as well

Explaining a score does not establish that it behaves like a calibrated probability.
Probability calibration concerns the relationship between reported probabilities
and outcomes across cases. Accuracy and calibration therefore answer different
questions: a model can classify many cases correctly while reporting probabilities
that need calibration.

CE uses a fitted model and **separate labelled calibration data** to construct
prediction information appropriate to the task and question. It then explains
that calibrated response. For a numerical target, its interval mode provides a
prediction interval in target units; an event mode instead reports probability
information for a question such as “Is the value at most a budget?”

The {doc}`calibration background <../foundations/concepts/calibration_background>`
explains the intuition and statistical concepts. The precise methods and their
conditions belong in {doc}`How CE Works <how-ce-works>`, not in an assumption-free
promise that every output becomes reliable.

## What CE adds to an individual result

Read three things together: **the prediction**, **the range for the relevant
quantity**, and **the explanation**. A factual weight and an alternative prediction
are different quantities. Their ranges must be interpreted separately from the
original prediction range.

For example, a numerical housing-value interval is in monetary units. Bounds
for the probability that the value is below a budget are on a probability scale.
A similar-looking bar does not give those outputs the same meaning or guarantee.
The {doc}`task and mode guide <../foundations/concepts/tasks_modes_capabilities>`
connects these questions to the available output forms.

## When should you consider CE?

Consider CE when you have a compatible fitted classifier or regressor, suitable
labelled calibration data, and a need to inspect predictions together with
mode-specific uncertainty information. You still need an evaluation plan and
domain knowledge to judge whether the outputs are useful for your application.

If you know SHAP or LIME, use the
{doc}`comparison page <../compare>` to compare the questions and quantities each
method addresses. CE is not a universal replacement for every explanation method;
choose according to your question, available data and required interpretation.

Calibration assumptions can fail under distribution shift. Explanations do not
establish causation, feasible interventions or a universally correct decision.
The {doc}`range meanings and limitations <../foundations/concepts/calibrated_interval_semantics>`
state the method-specific conditions; prediction bounds and feature-weight ranges
do not inherit one common guarantee.

## Connect the motivation to the research

The research question is how to present explanations of individual model
predictions together with calibrated uncertainty information. The
[classification paper](https://doi.org/10.1016/j.eswa.2024.123154) develops CE with
uncertainty information and counterfactuals; the
[regression paper](https://doi.org/10.1007/s10994-024-06642-8) extends the programme
to numerical targets. The maintained {doc}`citation list <../citing>` also includes
multiclass and conditional developments.

The teaching examples below make those ideas concrete. The papers and their
assumptions govern the formal results; an intuitive explanation or successful
code cell does not add a guarantee. We use “alternative” for model-condition
comparisons without assuming real-world causal or actionable counterfactuals.

## Continue from motivation to understanding

Begin with the shared data-role chapter, then follow the same Iris case through
calibration, explanation and interpretation. The prose teaches the concepts;
the code and captured output let you investigate them. Reading without running
Python is also useful. If your main question is how the method is constructed,
the {doc}`How CE Works overview <how-ce-works>` introduces the workflow before
these same chapters. You will not need to repeat a different set of definitions.

1. {doc}`Features, targets and separate data roles <../foundations/concepts/predictive_tasks>`.
2. {doc}`Choose a task, output question and operation <../foundations/concepts/tasks_modes_capabilities>`.
3. {doc}`Understand calibration and run it <../foundations/concepts/calibration_background>`.
4. {doc}`Construct and inspect an explanation <../foundations/concepts/how_explanations_are_built>`.
5. {doc}`Read the resulting rules and plots <../foundations/how-to/interpret_explanations>`.
6. {doc}`Evaluate held-out results <../practitioner/check_results>`.

The {doc}`complete plotted Python example <../get-started/first-python-explanation>`
is an alternative hands-on entry using the same Iris case. You do not need to
repeat it after executing the shared chapter cells.

For the scientific origins, use {doc}`the method papers and citations <../citing>`:
they connect CE's uncertainty-information and alternative-explanation research to
classification, multiclass and regression developments. Do not interpret the
teaching narrative as an additional historical or statistical claim.

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


## Continue the guided introduction

**Next chapter:** {doc}`Predictive tasks and data roles <../foundations/concepts/predictive_tasks>`. This sequence is for readers learning CE from the beginning; you can still use this page independently as a topic guide.

<!-- Preserve section links from earlier review versions. -->
<span id="continue-as-a-guided-tutorial"></span>
