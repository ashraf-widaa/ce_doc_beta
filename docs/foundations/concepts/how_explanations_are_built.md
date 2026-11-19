# How a prediction becomes an explanation

What connects a feature condition to the numbers in an explanation? Begin with
the quantity being explained, then distinguish a factual weight from an
alternative prediction.

## Start with the output quantity

Call that quantity {math}`q(x)` for the query {math}`x`. It may be a class probability,
a numeric target prediction or a threshold-event probability. Its units follow
that choice. The {doc}`task and mode map <tasks_modes_capabilities>` helps you
identify it before reading any weights.

## Compare model responses under feature conditions

<div class="ce-workflow-grid">
<div class="ce-workflow-lane"><p class="ce-workflow-heading">Factual explanation</p><ol><li>Obtain the baseline prediction quantity.</li><li>Identify conditions that hold for this case.</li><li>Use the method's substituted feature scenarios to obtain comparison responses.</li><li>Report weights and their ranges for those comparisons.</li></ol></div>
<div class="ce-workflow-lane"><p class="ce-workflow-heading">Alternative explanation</p><ol><li>Keep the same baseline and task.</li><li>Consider a different feature condition.</li><li>Obtain the prediction information under that condition.</li><li>Compare the alternative prediction and its range with the baseline.</li></ol></div>
</div>

For the ordinary factual comparison, a schematic description of a feature
weight is

```{math}
w_j(x)=q(x)-r_j(x),
```

where {math}`r_j(x)` summarizes the responses used for feature {math}`j`'s comparison.
The actual substitutions and aggregation depend on the method, feature type
and options; this notation is not an alternative implementation specification.
The source's ordinary factual construction uses prediction-minus-comparison
weights. Alternative records instead report the alternative prediction and may
also expose its difference from baseline.

As illustrative arithmetic only, 0.70 minus 0.50 gives a factual weight of 0.20
on a probability scale. It does not say that changing that feature in the real
world increases an outcome probability by 0.20.

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

## Continue with a concrete result

- {doc}`Interpretation guide <../how-to/interpret_explanations>` connects the
  returned records to plots.
- {doc}`Expert Hub guide <../../get-started/expert-hub>` inspects actual browser
  factual and alternative outputs.
- {doc}`First Python explanation <../../get-started/first-python-explanation>`
  produces a checked local result.
- {doc}`Alternatives and filters <alternatives>` develops optional operations.
- {doc}`Canonical semantics <calibrated_interval_semantics>` records the
  qualifications that these introductory comparisons do not replace.
