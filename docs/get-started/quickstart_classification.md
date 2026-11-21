# Classification quickstart

Run calibrated explanations for binary or multiclass classification.

**First visit?** {doc}`First explanation in Python <first-python-explanation>` runs this same Iris dataset and split
through a complete result and plot. This page retains the broader classification
calls, including the explicitly experimental all-class option below.

```{warning}
In the reviewed 1.0.2 source, some multiclass returned bounds can fall outside
`[0, 1]`. For example, the first query in the split below produced an upper
bound around `1.453` in the review environment. Keep this output for diagnosis;
do not clip it or interpret it as a conventional bounded probability interval.
The statistical interpretation and behavior need maintainer review.
```


## Prerequisites

```bash
pip install calibrated-explanations scikit-learn
```

## Classification semantics note

- **Calibration prerequisites**: fit on `x_proper, y_proper` and calibrate on held-out `x_cal, y_cal`.
- **Mode-specific guarantees**: Venn-Abers provides calibrated probability intervals for class predictions.
- **Assumptions**: calibration and deployment data are exchangeable or distribution-matched.
- **Explicit non-guarantees**: no guarantee under drift or regime shift.
- **Explanation-envelope limits**: feature-level intervals are model-behavior summaries, not causal guarantees.
- **Formal semantics**: {doc}`../foundations/concepts/calibrated_interval_semantics`.

## 1. Load data and split sets

Each Iris row describes one flower. The four measurements are features and the
species is the target. Reserve evaluation data before splitting the remaining
rows into model-fitting and calibration data. The fixed seed makes this example
repeatable; the split proportions are an example, not a CE requirement.


```{literalinclude} ../_examples/first_explanation.py
:language: python
:lines: 1-19
```

The cell creates 90 proper-training, 30 calibration and 30 evaluation rows; it
does not print output. Read the {doc}`data-role guide <../foundations/concepts/predictive_tasks>`
if those roles are unfamiliar, then continue here.

## 2. Fit and calibrate the explainer

Fit the classifier first, then calibrate with the separate labelled examples.
Keep all three feature arrays in the same representation and order.


```{literalinclude} ../_examples/first_explanation.py
:language: python
:lines: 21-23
```

The cell prepares a fitted, calibrated wrapper. It has no printed output.
For the construction behind calibration, use {doc}`How CE Works <../sections/how-ce-works>`.

## 3. Generate calibrated factual explanations

Explain the first five held-out rows. The result is a collection with one item
per query; an item contains the prediction information and feature conditions.


```python
factual = explainer.explain_factual(x_test[:5])
print("Factual explanations:", len(factual))
```

```text
Factual explanations: 5
```

This checks the collection size, not accuracy or validity. To interpret a plotted
item, follow {doc}`First explanation in Python <first-python-explanation>` and
{doc}`the interpretation guide <../foundations/how-to/interpret_explanations>`.

For multiclass all-class explanations (optional depth):

```python
multi_factual = explainer.explain_factual(x_test[:5], multi_labels_enabled=True)
```

`multi_labels_enabled` remains an explicitly experimental call-time option; its
spelling is canonical, but its contract is not part of the frozen stable surface.
The call returns an object without printed output; it is not required for your
first explanation. Use the version-specific API contract when inspecting it.

## 4. Explore calibrated alternatives

Request alternatives for two held-out cases. Each collection item can contain
several alternative conditions; the number of collection items is not the
number of individual alternative rules.


```python
alternatives = explainer.explore_alternatives(x_test[:2])
print("Alternative explanation items:", len(alternatives))
```

```text
Alternative explanation items: 2
```

Compare one alternative prediction with the original case, preserving class
ordering and probability units. An alternative is a model comparison, not an
action guaranteed to change a flower's species. Keep the multiclass warning
above visible when reading bounds.

Next steps:
- {doc}`../foundations/how-to/interpret_explanations`
- {doc}`../foundations/concepts/alternatives`
- {doc}`../citing`

Entry-point tier: Tier 2.
