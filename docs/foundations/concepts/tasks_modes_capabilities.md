# Tasks, modes and capabilities

What is your model predicting, what question do you ask about it, and what do
you want to inspect? These are three separate choices.

## Task: the target your model predicts

A classification target is a category. A regression target is a numeric quantity.
The shared {doc}`predictive-task definitions <predictive_tasks>` explain features,
observations, targets and data roles. Classification and regression are the two
predictive tasks used in these guides; do not count factual explanations as a
third task.

## Mode: the question you ask

```{include} ../../_shared/task-mode-map.md
:start-after: <!-- task-mode-map:start -->
:end-before: <!-- task-mode-map:end -->
```

A regression model can support both value and event questions. For example,
asking for a housing value interval and asking for the probability that value
is at most a budget concern the same target, but return different quantities.
A probability has no currency unit; a housing-value interval does.

In the Python interface, `threshold=` selects an event question. “Mode” here
is a learning distinction, not a claim that three different strings must be
passed as the constructor's `mode` argument. See {doc}`probabilistic_regression`.

## Capability: the operation you need

| Capability | Question it helps answer | What it is not |
| --- | --- | --- |
| Calibrated prediction | What prediction information is reported for this query? | Proof that the case will have that outcome. |
| Factual explanation | Which conditions holding for this case are associated with the model response? | A causal explanation of the world. |
| Alternative explanation | What would the model report under another feature condition? | A guaranteed feasible, minimal or effective real-world intervention. |
| Guarded filtering | Which explanation candidates meet the configured support filter? | A guarantee that the whole query or deployment is valid. |

The last row is an advanced option after an ordinary explanation; see
{doc}`guarded_explanations`. Alternative filtering and plotting are described in
{doc}`alternatives`. Capabilities and APIs vary with version and browser route:
Python library support does not prove that a browser app exposes the same feature.

## Choose a route

- **No installation:** {doc}`browser-first Quickstart <../../get-started/index>`.
- **Run Python:** {doc}`first Python explanation <../../get-started/first-python-explanation>`.
- **Understand construction:** {doc}`how_explanations_are_built`.
- **Check conditions and guarantees:** {doc}`calibrated_interval_semantics`.
