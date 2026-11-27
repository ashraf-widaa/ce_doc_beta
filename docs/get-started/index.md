# CE big picture in 60 seconds

<span class="ce-choice-page" hidden></span>

**Start here to understand what Calibrated Explanations (CE) adds, then read one
worked result.** You can try the browser route without installing Python, or
follow a complete local example. You do not need to learn the software interface
or optional capabilities first.

## 1. See what CE adds

A predictive model estimates a category or a number from a case's features.
CE uses that fitted model and **separate labelled calibration data** to provide
prediction information and explanations with reported ranges.

```{figure} ../_static/figures/ce-wrapper-quickstart.png
:alt: Numbered Calibrated Explanations wrapper workflow: wrap and fit the predictive model using training data; prepare calibration using separate labelled data; predict from test or new-case features; choose factual or alternative explanations. Test targets are kept aside for evaluation. Blue denotes machine learning and inputs; orange denotes additions from Calibrated Explanations.
:width: 100%
:class: ce-quickstart-wrapper

One wrapper connects training, calibration, prediction and explanation.
[Open the full-size figure](../_static/figures/ce-wrapper-quickstart.png), or
{ref}`read the accessible step-by-step description <ce-wrapper-workflow-map>`.
```

First read the **prediction and its range**. Then ask:

- **Factual explanation:** which conditions holding for this case contribute
  to the response? Read comparison weights and their ranges.
- **Alternative explanation:** what would the model report under another
  condition? Read that prediction and its range.

The predictive model is not retrained by calibration. For test observations or
new cases, prediction and explanation use **features only**. Test targets are
known and kept aside for evaluation; a new case's target may be unknown.
Ranges have method-specific assumptions, and explanations do not establish causal effects.

## 2. Choose one worked example

**Not sure where to begin? Start with the classification example.** Each page
lets you read a captured result, try the browser workflow, or run Python locally.
Choose one route; you do not need to complete them all.

| Your question | Start here |
| --- | --- |
| Which category, and how probable? | {doc}`Classification: read one prediction <example-classification>` — the recommended first example. |
| What numerical value, with what interval? | {doc}`Interval regression <example-interval>`. |
| How probable is a numerical event, such as a value below a budget? | {doc}`Event probabilities <example-event>`. |

Classification predicts categories; regression predicts numerical targets. The
two regression questions concern the same kind of target but return different
quantities: target values or event probabilities. For more depth, use the shared
{doc}`task and mode guide <../foundations/concepts/tasks_modes_capabilities>`.

## 3. Read the result before adding options

In your chosen example, identify the reported quantity and its units, read one
factual condition and weight, then compare one alternative prediction with the
original. The example explains what you should see.

**Next:** use {doc}`Interpret explanations <../foundations/how-to/interpret_explanations>`
with that result open. It is the same guide whichever example or environment you chose.

## Continue for your goal

- **Understand the ideas:** {doc}`CE: What & Why <../sections/what-and-why>`.
- **Learn the construction and assumptions:** {doc}`How CE Works <../sections/how-ce-works>`.
- **Use your own data:** {doc}`CE in Practice <../sections/in-practice>`.
- **Find software calls or integrate CE:** {doc}`Software & Integration <../sections/software-integration>`.

Optional capabilities can wait until you have read one result. The shared
{doc}`optional-capability overview <../foundations/concepts/optional_capabilities>`
explains when to use grouping, guarding, conjunctions, alternative filtering or rejection.
The detailed {ref}`wrapper workflow <ce-wrapper-workflow-map>` and
{doc}`Quick API <quick_api>` are available when you want the software view.

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

<!-- Preserve links from previous Beta candidates. -->
<span id="from-a-conventional-prediction-to-ce"></span>
<span id="ce-wrapper-workflow-map"></span>
<span id="ce-core-comparison"></span>
<span id="ce-wrapper-workflow"></span>
<span id="tasks-and-modes-what-question-are-you-asking"></span>
<span id="capabilities-read-one-result-in-two-complementary-ways"></span>
<span id="choose-how-to-try-ce"></span>
<span id="when-you-need-more-than-the-basic-workflow"></span>
<span id="ce-optional-capability-map"></span>
<span id="at-calibration-should-regions-be-treated-separately"></span>
<span id="while-building-explanations-are-candidate-conditions-supported"></span>
<span id="after-generating-alternatives-which-ones-should-i-inspect"></span>
<span id="when-using-the-prediction-should-some-cases-be-flagged-or-set-aside"></span>
<span id="continue-learning"></span>
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
<span id="quick-start-the-ce-big-picture"></span>
<span id="what-changes-when-you-add-ce"></span>
<span id="choose-the-question-you-want-to-answer"></span>
<span id="what-can-an-explanation-tell-you"></span>
<span id="what-do-the-ranges-mean"></span>
<span id="after-your-first-result"></span>
<span id="go-deeper-when-you-need-it"></span>
<span id="capabilities-what-can-ce-show-you"></span>
