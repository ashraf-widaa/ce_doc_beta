# How a prediction becomes an explanation

<span class="ce-course-step" hidden></span>

What connects a feature condition to the numbers in an explanation? Begin with
the quantity being explained, then distinguish a factual weight from an
alternative prediction.

## Keep the running case in view

The preceding chapter reports 0.910 for the selected flower's versicolor
probability. We now ask which feature conditions contribute to that response
and what the model reports under different conditions. Keep the same flower and
class so that a changed quantity does not get mistaken for a changed case.

## Start with the output quantity

The **baseline** is the prediction information for the original case, before
considering another feature condition. It may be a class probability,
a numeric target prediction or a threshold-event probability. Its units follow
that choice. The {doc}`task and mode map <tasks_modes_capabilities>` helps you
identify it before reading any weights.

## Compare model responses under feature conditions

<div class="ce-workflow-grid">
<div class="ce-workflow-lane"><p class="ce-workflow-heading">Factual explanation</p><ol><li>Obtain the baseline prediction quantity.</li><li>Identify conditions that hold for this case.</li><li>Use the method's substituted feature scenarios to obtain comparison responses.</li><li>Report weights and their ranges for those comparisons.</li></ol></div>
<div class="ce-workflow-lane"><p class="ce-workflow-heading">Alternative explanation</p><ol><li>Keep the same baseline and task.</li><li>Consider a different feature condition.</li><li>Obtain the prediction information under that condition.</li><li>Compare the alternative prediction and its range with the baseline.</li></ol></div>
</div>

A **comparison response** is what the fitted model with CE calibration reports under the
feature scenarios used by the explanation method. A factual weight compares
the original response with those comparison responses. An alternative reports
the response under a different condition. Conditions describe the model query,
not an experiment that has changed the real-world case.

<details><summary>Go deeper: schematic notation for a factual weight</summary>

For the ordinary factual comparison, a schematic description of a feature
weight is

```{math}
w_j(x)=q(x)-r_j(x),
```

Here {math}`q(x)` is the original output for query {math}`x`; {math}`r_j(x)` summarizes the responses used for feature {math}`j`'s comparison.
The actual substitutions and aggregation depend on the method, feature type
and options; this notation is not an alternative implementation specification.
The source's ordinary factual construction uses prediction-minus-comparison
weights. Alternative records instead report the alternative prediction and may
also expose its difference from baseline.

As illustrative arithmetic only, 0.70 minus 0.50 gives a factual weight of 0.20
on a probability scale. It does not say that changing that feature in the real
world increases an outcome probability by 0.20.

</details>

## Read signs, units and ranges together

| Quantity | What to inspect |
| --- | --- |
| Baseline prediction | Class/event definition or numeric target, units and its own range. |
| Factual condition | Whether the condition holds for the query. |
| Factual weight | The comparison quantity, its sign, units and range. |
| Alternative condition | What differs from the original condition. |
| Alternative prediction | Its output and range; compare with the baseline on the same scale. |

A point weight's sign and a range crossing zero need to be read together.
The feature-range construction does not automatically inherit a prediction
coverage theorem. These are not Shapley values; do not assume they sum to the
prediction or form a unique decomposition.

## Why these are model explanations, not causes

Feature dependence and implausible substitutions can affect interpretation.
A changed condition in a model query is not a controlled intervention on a
patient, district or production process. Alternatives need not be actionable,
minimal or feasible. A browser game can add costs and constraints, but that
does not turn every library alternative into a causal recommendation.

## Inspect a weight and an alternative in Python

Continue the fitted and calibrated Iris session from
{doc}`calibration_background`, or run the
{download}`complete shared lab <../../_examples/learning_lab.py>` first.
`build_rules_payload()` returns structured rule records; `core` contains the
explanation quantities, while metadata retains additional construction details.
Here we inspect one rule to connect the terminology to an actual result.
`factual[0]` selects the first queried case. Dictionary keys such as `["core"]`
and `["feature_rules"]` select named records inside that case’s payload; the
second `[0]` selects its first rule.

```{literalinclude} ../../_examples/learning_lab.py
:language: python
:start-after: explanation:start
:end-before: explanation:end
```

Verified output from the review environment:

```{literalinclude} ../../_examples/learning_lab_output.txt
:language: text
:start-after: EXPLANATION_START
:end-before: EXPLANATION_END
```

The factual condition `sepal length (cm) > 5.55` holds for the selected flower.
Its reported weight is +0.388 with bounds [0.240, 0.433]. Read this as a comparison
on the explained class-probability scale, not a second prediction probability
or a causal effect of changing a sepal.

The alternative collection has one item for this queried flower; that item
contains eight rules in the captured run. Its first alternative condition reports
a prediction of 0.522. A rule count is not the collection length, and an alternative
prediction is not a factual weight. The output is version-specific; a different
case can produce different rules, ranges or no usable alternatives.

To see the same Iris case as a plot, follow
{doc}`First explanation in Python <../../get-started/first-python-explanation>`.
The shared {doc}`interpretation guide <../how-to/interpret_explanations>` then
explains how to read records and figures without assuming they prove causation.


<span id="continue-with-a-concrete-result"></span>

## Continue the guided introduction

**Previous chapter:** {doc}`calibration_background`.

**Next chapter:** {doc}`Read the results and figures <../how-to/interpret_explanations>`. This sequence is for readers learning CE from the beginning; you can still use this page independently as a topic guide.

For the method-specific conditions behind the ranges, use {doc}`calibrated_interval_semantics`.

<!-- Entry-point tier: Tier 3. -->
