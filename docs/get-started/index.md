# Get started

<span id="where-ce-fits"></span>

<span id="quick-start-understand-explore-and-apply-ce"></span>

**Calibrated Explanations (CE)** is an open-source Python library for explaining
individual predictions from supervised classification and regression models.
It uses a fitted model and separate labelled calibration data to provide
prediction information and explanations with reported ranges. Their meanings
and assumptions depend on the task, output question and method.

This section takes you from the definition to an explanation of your own
data. The first two steps need **no installation**; the Quick Start also offers a
complete Python route for readers who prefer to install CE straight away.

```{raw} html
<figure class="ce-preferred-workflow">
  <a href="quickstart.html#see-what-ce-adds" title="The workflow, explained step by step in the Quick Start">
    <picture>
      <source media="(max-width: 600px)" srcset="../_static/figures/ce-adds-to-workflow-narrow.svg">
      <img src="../_static/figures/ce-adds-to-workflow.svg" width="900" height="450" alt="Two aligned lanes share one fitted model. Lane 1, supervised prediction, in blue: the training set is used to fit a model, and the model predicts for a new case; this example baseline returns one value without uncertainty. Lane 2, workflow with CE, in orange: CE takes the same fitted model and a separate labelled calibration set, held out from training, calibrates, and predicts the same new case. It returns a calibrated prediction with its uncertainty, shown as probability bounds on a 0 to 1 scale for classification or as a prediction interval in the target's units for regression, and then factual and alternative explanations.">
    </picture>
  </a>
  <figcaption><strong>What CE adds to a supervised prediction workflow.</strong> The Quick Start explains this workflow before linking to worked examples.</figcaption>
</figure>
```

The **instance** is one observation selected from test data or supplied as a new
case. Prediction and explanation use its features; known test targets are kept
aside for evaluation.

<span id="your-learning-journey"></span>

(choose-your-path)=

## Your path through this section

Start with the overview or one example; installation is only needed for the
Python route. The links below reuse the shared concept and interpretation pages.

1. **{doc}`What CE is <../sections/what-and-why>` .** The definition, the
   problem CE addresses, what it provides and what it does not.
2. **{doc}`Quick Start <quickstart>` .**
   Understand what CE adds, choose your task, then create your first
   explanation in the browser (no installation) or in Python with
   {doc}`Your First CE Explanation in Python <first-python-explanation>`.
   Start here if you read only one page.
3. **{doc}`Installation <installation>` .**
   `pip install "calibrated-explanations[viz]"`; the `viz` extra adds plots.
4. **{doc}`Read your first explanation <../foundations/how-to/interpret_explanations>` .**
   Which number is the prediction, which is a weight, and what each range is.
5. **{doc}`Apply CE to your own data <../sections/in-practice>` .**
   Split, wrap, calibrate, explain, check and save.
6. **{ref}`Next steps <quick-start-next>`**, below.

**Coming from SHAP or LIME?** {doc}`Compare the questions and outputs <../compare>`
before translating your workflow.

**Prefer one worked prediction without code?** {doc}`CE by example <example-classification>`
follows a single prediction from the Python quickstart, with every number
explained.

<span id="which-ce-task-am-i-doing"></span>

## Which CE mode am I using?

| Your question | CE mode | Prediction call |
|---|---|---|
| Which class, and how probable? | Classification | `predict_proba(X, uq_interval=True)` |
| Which value, and within what range? | Interval regression | `predict(X, uq_interval=True)` |
| How probable is it that the value is at most *t*? | Probabilistic (thresholded) regression | `predict_proba(X, uq_interval=True, threshold=t)` |

The main explanation calls are `explain_factual(X)` and
`explore_alternatives(X)`. Read their output on the selected question's scale;
these learning-mode names are not three constructor strings.
Quick Start introduces task, mode and capability before the examples. For the
full account, use {doc}`Tasks, modes and capabilities <../foundations/concepts/tasks_modes_capabilities>`.
What each range
guarantees differs by mode: see
{doc}`Guarantees and limits by mode <../foundations/concepts/calibrated_interval_semantics>`.

<span id="reference-and-further-reading"></span>

(before-you-start)=

## Look things up

- The {doc}`Glossary <../glossary/index>` defines the terms.
- The {doc}`API reference <../api/index>` gives full signatures, and the
  {doc}`Quick API <quick_api>` the main calls on one page.
- {doc}`Troubleshooting <troubleshooting>` covers installation and runtime
  problems.

<span id="where-should-i-go-next"></span>

(quick-start-next)=

## Next steps

| I want to… | Go to |
|---|---|
| Understand the theory: why CE, calibration by task, guarantees and limits | {doc}`Understand CE <../sections/understand-ce>` |
| Practise in the browser with a guided scenario | {doc}`Decision Lab <decision-lab>` |
| Experiment with CE outputs in the browser | {doc}`Expert Hub <expert-hub>` |
| Run a complete first example in Python | {doc}`Your First CE Explanation in Python <first-python-explanation>` |
| Run the Python tutorials and task recipes | {doc}`CE in Practice <../sections/in-practice>` and the {doc}`Practitioner Hub <../practitioner/index>` |
| Integrate CE into an application, or understand and extend its code | {doc}`Software Architecture & Integration <../sections/software-integration>` |
| Find the research, how to cite CE, governance and support | {doc}`Project <../sections/project-resources>` |

```{toctree}
:hidden:
:maxdepth: 1

Quick Start <quickstart>
```

<span id="2-choose-one-worked-example"></span>
<span id="3-read-the-result-before-adding-options"></span>
<span id="ce-big-picture-in-60-seconds"></span>
<span id="id1"></span>
<span id="1-see-what-ce-adds"></span>
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
