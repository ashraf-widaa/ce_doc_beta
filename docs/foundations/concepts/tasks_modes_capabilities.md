# Tasks, modes and capabilities

<span class="ce-course-step" hidden></span>

In Calibrated Explanations (CE), what your model predicts, the question you ask
about it, and the operation you request are three separate choices.

A **task** describes the target; a **mode** describes the output question; a
**capability** describes the operation you request. For example, predicting flower
species is classification, asking for species probabilities selects that output,
and inspecting factual conditions requests an explanation. Changing the operation
does not change the target the model learned.

```{include} ../../_shared/task-mode-definitions.md
```

**Read in this order:** identify your target, choose the output question, then
choose an operation. You can stop at the worked example for your question and
return for the software details later.

## Task: the target your model predicts

A classification target is a category. A regression target is a numeric quantity.
The shared {doc}`predictive-task definitions <predictive_tasks>` explain features,
observations, targets and data roles. Classification and regression are the two
predictive tasks used in these guides; do not count factual explanations as a
third task.

## Mode: the question you ask

```{include} ../../_shared/task-output-choice.md
```

The classification branch covers **binary** targets (two categories) and
**multiclass** targets (three or more). Integer-encoded species remain categories;
numeric codes alone do not make a task regression.

A regression model can support both value and event questions. For example,
asking for a housing value interval and asking for the probability that value
is at most a budget concern the same target, but return different quantities.
A probability has no currency unit; a housing-value interval does.

In the Python interface, `threshold=` selects an event question. “Mode” here
is a learning distinction, not a claim that three different strings must be
passed as the constructor's `mode` argument. See {doc}`probabilistic_regression`.

## Follow the same housing target through two modes

The California Housing browser example predicts median housing value in units of
$100,000. Asking “What value, and within what interval?” uses interval regression.
Asking “How probable is a value at most $300,000?” uses probabilistic regression
with threshold 3. The predictive task remains regression. The output quantity
changes from a value in target units to a probability on an event.

Now choose a capability: inspect factual feature conditions or explore alternative
conditions. That choice changes the explanation you request, not the target the
model was trained to predict. See the {doc}`interval example <../../get-started/example-interval>`
or {doc}`event example <../../get-started/example-event>` for browser and local routes.

## Capability: the operation you need

After choosing the output, ask whether you need its prediction information,
a factual explanation, or alternatives. A factual explanation describes conditions
holding for this case; an alternative reports what the model would return under
another condition. Neither establishes a causal effect.


| Capability | Question it helps answer | What it is not |
| --- | --- | --- |
| Calibrated prediction | What prediction information is reported for this query? | Proof that the case will have that outcome. |
| Factual explanation | Which conditions holding for this case are associated with the model response? | A causal explanation of the world. |
| Alternative explanation | What would the model report under another feature condition? | A guaranteed feasible, minimal or effective real-world intervention. |
| Guarded explanations | Which explanation candidates meet the configured support filter? | A guarantee that the whole query or deployment is valid. |

To locate calibration, prediction, explanation and the optional operations, use
{doc}`the capability map and walkthrough <optional_capabilities>`. It explains
Mondrian calibration, rejection, guarding, conjunctions and alternative filtering
in their workflow positions; the {ref}`shared Quick API map <optional-capability-api-map>`
provides the corresponding software entry points.

The last row is an option during explanation construction, not a later rejection of the case; see
{doc}`guarded_explanations`. Alternative filtering and plotting are described in
{doc}`alternatives`. Capabilities and APIs vary with version and browser route:
Python library support does not prove that a browser app exposes the same feature.

## Match the learning terms to Python

`get_mode()` identifies the underlying classification or regression mode; do not
use that string alone to distinguish numerical regression from threshold-event
regression. Read the threshold and output quantity as well. The
{doc}`Quick API <../../get-started/quick_api>` maps questions to calls without
requiring a new constructor for each explanation capability.

## Check the distinctions in the Iris example

This cell continues the Iris session from
{doc}`Predictive tasks and data roles <predictive_tasks>`. If you arrived here
directly, run that setup first or use the
{download}`complete shared lab <../../_examples/learning_lab.py>`.

```{literalinclude} ../../_examples/learning_lab.py
:language: python
:start-after: modes:start
:end-before: modes:end
```

Verified output from the review environment:

```{literalinclude} ../../_examples/learning_lab_output.txt
:language: text
:start-after: MODES_START
:end-before: MODES_END
```

The `for` loop uses `enumerate` to pair each position with its species name.
Although the target codes are numbers, they name species. Their numeric order
does not define an amount: species 2 is not “twice species 1”. The task is therefore
multiclass classification, not regression. Binary classification has two target
categories; multiclass classification has three or more.

We will ask about one flower's class-probability information, then request factual
and alternative explanations of that response. Those are different operations
on the same task. For regression, the output question can instead ask about a
value or an event on that value, as the mode map above shows.


## Read guarantees at the output's level

A mode determines which quantity is reported; it does not make all its ranges
interchangeable. Start with the {doc}`semantics reading guide <calibrated_interval_semantics>`
for the distinctions and then read the applicable assumptions. For a step-by-step
reading of factual weights and alternative predictions, use
{doc}`Interpret calibrated explanations <../how-to/interpret_explanations>`.

<span id="choose-a-route"></span>

## Continue the guided introduction

**Previous chapter:** {doc}`predictive_tasks`.

**Next chapter:** {doc}`Calibration and its methods <calibration_background>`. This sequence is for readers learning CE from the beginning; you can still use this page independently as a topic guide.

<!-- Entry-point tier: Tier 3. -->

<span id="check-what-the-target-codes-mean"></span>
