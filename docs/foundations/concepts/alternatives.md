# Understanding alternative explanations

An **alternative explanation** asks what the model would report if a feature
condition were different. Start with the original prediction, change a condition,
then compare the alternative prediction on the same scale.

This differs from a factual explanation: a **factual weight** summarizes a
model-response comparison for a condition holding for the case. An alternative
reports the prediction under another condition. Neither is a causal intervention.

## Start with one case

In the shared Iris case, the original versicolor probability is about 0.910.
One alternative uses `sepal length (cm) < 5.55` and reports probability 0.522.
The useful reading is “under this condition, the model reports this probability”,
not “changing a real flower will cause this outcome”.

The {doc}`code-free case <../../get-started/example-classification>` shows the
captured output. The {doc}`explanation-construction page <how_explanations_are_built>`
explains comparisons and the same example's code without repeating its definitions here.

## Generate alternatives

The following snippets assume a fitted, calibrated `explainer` and a query-feature
array `X_query`. Run the {doc}`first Python example <../../get-started/first-python-explanation>`
for setup if needed. Query targets are not inputs to these calls.

```python
alternatives = explainer.explore_alternatives(X_query)
alt0 = alternatives[0]
```

The collection has one item per queried case. `alt0` selects the first case's
alternative explanation; it can contain several rules. A collection length of
one does not mean that only one alternative condition was found. Inspect the
conditions, predictions and reported ranges using the
{doc}`interpretation guide <../how-to/interpret_explanations>`.

For probabilistic regression, keep the threshold used in the original event query:

```python
alternatives = explainer.explore_alternatives(X_query, threshold=150.0)
```

Here the question is **Y ≤ 150** on a numerical target. Without that threshold,
a regression explanation concerns the target value instead. Use the
{doc}`regression guide <probabilistic_regression>` if those units differ from what you expected.

## Ensured filters

After reading the unfiltered result, choose a filter only for a stated purpose.
The methods select rules; by default they copy rather than modify the
original alternative object. Their criteria depend on the explained quantity.

| Method | What it selects in the reviewed implementation |
| --- | --- |
| `super_explanations()` | Alternatives reinforcing the current probability decision, or higher outputs in plain regression. |
| `semi_explanations()` | Probability alternatives moving toward the decision boundary without crossing it; lower outputs in plain regression. |
| `counter_explanations()` | Probability alternatives crossing the decision boundary; lower outputs in plain regression. |
| `ensured_explanations()` | Alternatives whose reported interval is no wider than the baseline prediction interval. |
| `pareto_explanations()` | An output-envelope frontier using the selected cost, such as interval width or rule size. |

The probability filters use the implementation's 0.5 comparison convention;
this is not an arbitrary application's cost-sensitive decision rule. Potential
alternatives and options affect filtering; consult the
{doc}`API reference <../../api/index>` for exact criteria. “Ensured” names a
width-based filter here. Selecting a narrower reported range does not, by itself,
prove a feasible intervention, a causal effect or a general reduction in predictive error.

## Plotting and conjunctions

A **conjunction** joins feature conditions in one rule. Add these only after
reading ordinary one-feature alternatives; extra conditions do not establish
real-world feasibility. This snippet uses the previously selected `alt0`:

```python
alt0.add_conjunctions(n_top_features=5, max_rule_size=2)
alt0.plot(style="triangular")
```

`max_rule_size=2` limits the number of conditions in a conjunction. The triangular
view displays alternative prediction information; it does not turn a prediction
into a factual weight. The plot needs a notebook or supported interactive backend to appear. Setting
`show=False` suppresses display; do not assume this legacy plotting call returns
a figure object. Use the {doc}`plotting guide <../how-to/plot_with_plotspec>`
for supported rendering and saving options, including headless environments.

## Related pages

- {doc}`Interpret predictions, weights and ranges <../how-to/interpret_explanations>`.
- {doc}`Range meanings and limits <calibrated_interval_semantics>`.
- {doc}`Guarded filtering <guarded_explanations>` for support-based candidate filtering, a different criterion from interval width.
- {doc}`Ensured playbook <../../practitioner/playbooks/ensured-explanations>` for additional filter calls; its research interpretation should be read with the relevant papers and assumptions.

<span id="alternative-explanations-and-ensured-filters"></span>

<!-- Entry-point tier: Tier 3. -->
