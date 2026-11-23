# Understanding guarded explanations

An explanation can consider feature conditions that have little support in the
calibration data. **Guarded explanations** add a support check to candidate
conditions before emitting rules. Read an ordinary explanation first, then use
this option when you want to inspect how that filtering affects the rules.

A **candidate interval** is a numerical feature range being considered for a
rule. A categorical candidate can instead be a category value. The guard tests
representative values from a numerical range in perturbed copies
of the query. It does not check every possible value in the interval, and it does
not automatically certify that the original query is in distribution.

A **perturbed copy** is a query in which a selected feature value has been
replaced for the check. The guard uses nearest-neighbor distance information:
nearby calibration feature vectors provide the comparison. Its conformity p-value
is part of this support check, not the class probability predicted by the model.

## Follow the check through the CE workflow

1. Fit the model and calibrate CE with separate labelled data as usual.
2. Request factual or alternative explanations with `GuardedOptions`.
3. The guard checks candidate conditions using calibration-derived support information.
4. Inspect the emitted rules **and the audit** to see what was tested or removed.

Filtering changes which candidate rules are returned. An empty or shorter result
is not proof that no feature matters, and a retained rule is not an intervention
recommendation. The {doc}`semantics reference <calibrated_interval_semantics>`
remains the shared source for the meanings and limitations of prediction and
feature ranges.

## What guarded mode changes

For a first reading, think of the guard as a check of selected representative
inputs, followed by candidate filtering. A **bin** groups feature values into a
range. Its median is the middle representative value; `q10` and `q90` are its
10th and 90th percentile representatives. These checks help define the shipped
rule; they do not test every point between the representatives.

<details><summary>Technical details of the shipped mixed guard rule</summary>

- Uses a mixed guard rule on interval candidates:
  categorical values are checked directly,
  sparse numerical bins are checked at the median representative,
  and dense numerical bins are checked conservatively with `q10` and `q90`.
- Returns standard CE containers and helper-compatible subclasses.
- Removes candidate intervals rejected by the shipped guard rule.
- May merge adjacent conforming bins into wider interval rules when `merge_adjacent=True`.

</details>

## Core calls

Use a fitted, calibrated standard (non-fast) explainer. `X` contains query features;
run {doc}`the guarded tutorial <../../get-started/quickstart_guarded>` for complete
setup. The optional object below is passed to the explanation call; it does not
change the predictive task or select a regression output mode.

```python
from calibrated_explanations.explanations.guarded_options import GuardedOptions
guarded_factual = explainer.explain_factual(X, guarded_options=GuardedOptions(confidence=0.9))
guarded_alts = explainer.explore_alternatives(X, guarded_options=GuardedOptions(confidence=0.9))
```

`GuardedOptions` fields (all optional): `confidence=0.9`, `n_neighbors=5`,
`normalize=True`, `merge_adjacent=False`, `verbose=False`.

> **Migration note**: `guarded=True` was removed in v0.11.5. Replace
> `guarded=True, significance=0.1` with `guarded_options=GuardedOptions(confidence=0.9)`
> (`confidence = 1 − significance`).

## What guarded mode does not guarantee

“Supported by the guard” is narrower than “safe”, “causal” or “valid for every
point in this interval”. Keep these source-version qualifications in view:

- It is not semantically identical to standard CE internals, metrics, or perturbation math.
- It does not certify that every point in an emitted interval would pass the guard.
- In factual mode, `merge_adjacent=True` can emit wider interval rules than standard CE would produce.

## Limitations

Two distinctions matter before relying on the filtered result. First, a test at
representative points is not a guarantee over an entire interval. Second,
checking a modified query is not the same as testing the original query for
**out-of-distribution (OOD)** behavior: whether it departs from the calibration
population. The detailed source-version explanations follow.

**Interval-level false positive rate (FPR).**
The conformal guarantee operates at the representative-point level, not over
the full interval.  Empirically, the interval-level FPR can exceed the nominal
derived significance level, especially for wide bins whose representative point is
near the distribution boundary.  Do not treat `significance` as a certified
per-interval false positive bound.

**Guard tests interval plausibility, not instance OOD-ness.**
The guard evaluates perturbed instances — copies of the test instance with
one feature replaced by the interval's representative value (a calibration-derived
median or percentile).  It does not directly test whether the test instance
itself is out-of-distribution.  When the feature being replaced is the primary
source of distributional shift, the resulting probe is in-distribution by
construction and the guard cannot detect the OOD-ness of the original instance.
In low-dimensional settings this is especially pronounced: for a 1-feature
dataset, replacing the only feature with a calibration representative makes
every probe in-distribution regardless of how far the test instance lies from
the calibration support.  The guard therefore measures *interval plausibility*
(is this hypothetical perturbation a plausible input?) rather than *instance
OOD detection* (is this test instance OOD?).  To test whether a test instance
is itself OOD, use ``InDistributionGuard.is_conforming(x_instance)`` directly.

## Guarded audit

The **audit** records the filtering process. Inspect it alongside the explanation,
especially if few or no rules remain. It describes what the procedure did; it
is not a separate certificate of predictive accuracy or calibration validity.

```python
audit = guarded_factual.get_guarded_audit()
summary = audit["summary"]
print("Accepted candidates:", summary["intervals_conforming"])
print("Removed by guard:", summary["intervals_removed_guard"])
```

The payload contains an aggregate `summary` and an `instances` list for the
queried cases. The printed counts come from `summary`; they depend on your
queries and configuration. They count filtering events, not correct predictions.
The payload reports tested, conforming, removed, and emitted candidates.

- `intervals_conforming`: candidates accepted by the shipped guard rule.
- `intervals_removed_guard`: candidates rejected by the shipped guard rule.

## Parameters

`GuardedOptions.confidence` sets the guard's acceptance threshold, not the
probability of a predicted class or the coverage of a target-value interval.
The representative is accepted when its guard p-value is at least
`1 - confidence`. For example, 0.9 corresponds to a threshold of 0.1. Raising
`confidence` lowers this cutoff and is more inclusive for a fixed set of p-values.
This explains the implementation's direction; it does not add a new statistical
guarantee. See the separate {doc}`range guide <calibrated_interval_semantics>`
for predictive quantities.

| Parameter | Meaning |
| --- | --- |
| `confidence` | Coverage-style conformity threshold. Higher values are more inclusive (`significance = 1 - confidence`). |
| `merge_adjacent` | Merge adjacent conforming bins when enabled. |
| `n_neighbors` | KNN neighbors for conformity scoring. |
| `normalize` | Apply per-feature normalization before distance calculations. |
| `verbose` | Emit additional guarded-mode diagnostic warnings when enabled. |

## Related pages

- {doc}`../../get-started/quickstart_guarded`
- {doc}`alternatives`
- {doc}`../how-to/interpret_explanations`
- [ADR-032: guarded-explanation semantics](https://github.com/Moffran/calibrated_explanations/blob/main/development/adrs/ADR-032-guarded-explanation-semantics.md) for the design record and detailed constraints.

Entry-point tier: Tier 3.

<span id="guarded-explanations"></span>
