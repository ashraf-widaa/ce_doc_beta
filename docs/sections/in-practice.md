# CE in Practice

<span class="ce-choice-page" hidden></span>

Use this path to obtain an explanation, understand its output and check the
workflow before adapting it to your own data. Start with one case and one
question; advanced filters and deployment settings can wait.

## Start with one worked result

If you are new to CE, follow the
{doc}`classification example <../get-started/example-classification>`. It offers
a binary Diabetes exercise in the browser and a complete multiclass Iris example
in Python. You will identify the prediction, its reported range, a factual
condition and an alternative prediction.

For a numerical target, choose the question you actually need:

- **A predicted value and interval:** {doc}`interval regression <../get-started/example-interval>`.
- **The probability of an event on that value:** {doc}`event-probability regression <../get-started/example-event>`.

Each example provides browser and local routes. Choose one; they need not use
the same dataset or produce matching numbers. If the workflow itself is unfamiliar,
the {doc}`Quick Start <../get-started/index>` explains the big picture first.

## Read the result before adding features

Name the quantity and units before interpreting its range. Then read one factual
condition: which feature does it concern, what comparison does its weight describe,
and what range belongs to that weight? Finally inspect one alternative and compare
its prediction with the original case. This is a model comparison, not a proven
real-world intervention.

The shared {doc}`interpretation guide <../foundations/how-to/interpret_explanations>`
explains each element of the records and plots. Keep it beside your result when
needed; you do not need to learn every payload field for a first reading.

## Choose a browser learning environment for a purpose

Use the {doc}`Expert Hub guide <../get-started/expert-hub>` when you want to follow
dataset preparation, calibration and explanation without writing code. It guides
the controls and interprets dated real outputs. Use the
{doc}`Decision Lab guide <../get-started/decision-lab>` when you want to inspect a
prediction alongside decision costs and then reflect on feedback. Its teaching
games identify their own service and do not establish library guarantees.

You can follow either guide directly; you do not need to complete both. After
an exercise, return to interpretation and evaluation rather than treating a
successful game outcome as a calibration check. If you want the underlying
construction, the {doc}`shared guided introduction <what-and-why>` provides concept,
code and output chapters instead of a separate set of definitions.

## Use your own model and data

Follow the {doc}`pipeline integration guide <../foundations/how-to/integrate_with_pipelines>`
when adding CE to a model with preprocessing. Keep fitting, calibration and
held-out evaluation roles separate, and use the same feature representation.
The {doc}`Software & Integration path <software-integration>` connects this
workflow to installation, public calls, configuration and error handling.

A working example is not an evaluation. Before relying on your results, use
{doc}`Checking results on your data <../practitioner/check_results>` to choose
probability, interval or event checks appropriate to your question. Read the
{doc}`method-specific assumptions <../foundations/concepts/calibrated_interval_semantics>`
together with any claimed guarantee.

## Go further for a specific reason

The {doc}`Practitioner Hub <../practitioner/index>` groups existing guides by goal:
calibration, intervals, alternatives, subgroups, rejection and evidence review.
Use {doc}`guarded explanations <../get-started/quickstart_guarded>` when you need
to understand support filtering, or the
{doc}`playbooks <../practitioner/playbooks/index>` for a particular decision workflow.
These are extensions to the basic example, not prerequisites for it.

<details><summary>Check which dataset an example uses</summary>

- Browser Diabetes uses a Pima binary target; it is not scikit-learn's numeric diabetes target.
- Browser California Housing uses $100,000 target units: a threshold of 3 means $300,000.
- The first Python example uses Iris species and records a multiclass-bound limitation.
- The Python regression tutorial uses the numeric diabetes target.

Use each example's actual labels, units, split and query row. Do not transfer
numbers or service guarantees between browser apps and the installed library.

</details>

## Continue from practice

**Understand why the numbers arise:** {doc}`How CE Works <how-ce-works>`.
**Find a particular call:** {doc}`Quick API <../get-started/quick_api>`.
**Interpret a term:** {doc}`Glossary <../glossary/index>`.

```{toctree}
:maxdepth: 1
:hidden:

Classification tutorial <../get-started/quickstart_classification>
Regression tutorial <../get-started/quickstart_regression>
Guarded explanations (advanced) <../get-started/quickstart_guarded>
Tasks and capabilities <../tasks/index>
Practitioner hub <../practitioner/index>
```

<!-- Entry-point tier: Tier 1. -->

<!-- Preserve earlier section links. -->
<span id="build-on-the-ordinary-example"></span>
<span id="check-what-the-example-does-not-establish"></span>
<span id="choose-a-practical-route"></span>
<span id="choose-your-starting-activity"></span>
<span id="follow-one-case-before-changing-the-workflow"></span>
<span id="interpret-before-extending"></span>
<span id="know-which-dataset-and-target-you-are-using"></span>
