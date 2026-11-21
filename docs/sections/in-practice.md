# CE in Practice

<!-- Preserve descriptive anchors from the previous review layout. -->
<span id="build-on-the-ordinary-example"></span>
<span id="choose-a-practical-route"></span>


What do you want to do with CE? Choose one practical route, inspect the result,
then check whether the workflow is appropriate for your own data.

## Choose your starting activity

| Your goal | Start here | Continue with |
| --- | --- | --- |
| Explore without installation | {doc}`Browser Quickstart <../get-started/index>`. | {doc}`Expert Hub <../get-started/expert-hub>` or {doc}`Decision Lab <../get-started/decision-lab>`. |
| Run a complete local example | {doc}`First explanation in Python <../get-started/first-python-explanation>`. | {doc}`Interpretation <../foundations/how-to/interpret_explanations>`. |
| Use a classifier | {doc}`Classification tutorial <../get-started/quickstart_classification>`. | {doc}`Check results <../practitioner/check_results>`. |
| Predict a number or an event on it | {doc}`Regression tutorial <../get-started/quickstart_regression>`. | {doc}`Regression mode meanings <../foundations/concepts/probabilistic_regression>`. |
| Connect an existing model or preprocessing | {doc}`Pipeline integration <../foundations/how-to/integrate_with_pipelines>`. | {doc}`Software & Integration <software-integration>`. |

## Follow one case before changing the workflow

Choose one route above and keep its dataset, selected case and output question
unchanged for the first run. Identify the prediction, its units and its reported
range before inspecting feature conditions. Then inspect one alternative and
ask which model output changed. This gives you a complete first pass without
requiring every available capability.

If a plot is hard to read, use the
{doc}`interpretation guide <../foundations/how-to/interpret_explanations>` beside
the example. When you are ready to understand how its numbers are constructed,
follow {doc}`How CE Works <how-ce-works>`. Before adapting the example to your
own data, use {doc}`Checking results <../practitioner/check_results>` to plan
held-out evaluation. A successful tutorial run is the beginning of that check,
not evidence that your deployment is reliable.

## Know which dataset and target you are using

| Example | Target / task | Important distinction |
| --- | --- | --- |
| Browser Diabetes | Pima binary class | This is not Sklearn's numeric diabetes regression dataset. |
| Browser California Housing | Numeric housing value; target units $100,000 | A threshold of 3 means $300,000 for this dataset. |
| First Python example | Iris species / multiclass classification | It uses the reviewed library source and records its multiclass limitation. |
| Existing Python regression tutorial | Numeric diabetes target | Numeric intervals and event probabilities answer different questions. |

Use the example's actual labels, units, split and selected row. Do not transplant
browser values into another dataset or assume a teaching game's backend matches
the installed library version.

## Interpret before extending

Use the shared {doc}`interpretation guide <../foundations/how-to/interpret_explanations>`
for conditions, weights, predictions and ranges. Then move to
{doc}`guarded explanations <../get-started/quickstart_guarded>` if filtering is
relevant, or {doc}`practitioner playbooks <../practitioner/playbooks/index>` for
specific decision workflows. These are optional, not prerequisites.

## Check what the example does not establish

One plot is not an evaluation. Use {doc}`checking results on your data <../practitioner/check_results>`
for task-appropriate held-out checks and limitations. Keep scientific
{doc}`assumptions and non-guarantees <../foundations/concepts/calibrated_interval_semantics>`
visible when adapting the workflow.

**Understand the mechanism:** {doc}`How CE Works <how-ce-works>`.
**Find advanced material:** {doc}`Practitioner Hub <../practitioner/index>`.

```{toctree}
:maxdepth: 1
:hidden:

Classification tutorial <../get-started/quickstart_classification>
Regression tutorial <../get-started/quickstart_regression>
Guarded explanations (advanced) <../get-started/quickstart_guarded>
Tasks and capabilities <../tasks/index>
Practitioner hub <../practitioner/index>
```

Entry-point tier: Tier 1.
