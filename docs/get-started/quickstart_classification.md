# Classification quickstart

Run calibrated explanations for binary or multiclass classification.

**First visit?** {doc}`Quickstart <index>` runs this same Iris dataset and split
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

```{literalinclude} ../_examples/first_explanation.py
:language: python
:lines: 1-19
```

## 2. Fit and calibrate the explainer

```{literalinclude} ../_examples/first_explanation.py
:language: python
:lines: 21-23
```

## 3. Generate calibrated factual explanations

```python
factual = explainer.explain_factual(x_test[:5])
```

For multiclass all-class explanations:

```python
multi_factual = explainer.explain_factual(x_test[:5], multi_labels_enabled=True)
```

`multi_labels_enabled` remains an explicitly experimental call-time option; its
spelling is canonical, but its contract is not part of the frozen stable surface.

## 4. Explore calibrated alternatives

```python
alternatives = explainer.explore_alternatives(x_test[:2])
```

Next steps:
- {doc}`../foundations/how-to/interpret_explanations`
- {doc}`../foundations/concepts/alternatives`
- {doc}`../citing`

Entry-point tier: Tier 2.
