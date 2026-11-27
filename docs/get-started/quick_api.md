# Quick API

Use this page to choose a public `WrapCalibratedExplainer` call after fitting
and calibration. It is a lookup guide, not a complete executable tutorial.
For a first run, use {doc}`First explanation in Python <first-python-explanation>`;
for exact parameter and return contracts, use {doc}`the API reference <../api/index>`.

## Before calling the methods

Wrap a compatible model, fit it on the proper training data, then calibrate with
separate labelled data. Keep query features in the same order and representation
as the fitting and calibration features. `X_query` and `X_sample` below are query
feature arrays; their targets are not inputs to explanation calls. The snippets
assume an already-created explainer and the named data arrays.

## Numbered wrapper lifecycle

The {ref}`core workflow figure <ce-wrapper-workflow-map>` connects each concept
to its software entry point. The same wrapper coordinates fitting, calibration,
prediction and explanation.

```{include} ../_shared/wrapper-lifecycle.md
```

## Choose a call by the question

- **Which class?** Use `predict`; for class probabilities use `predict_proba`.
- **Which numerical value and interval?** On a regressor, use `predict` with
  `uq_interval=True` and the requested `low_high_percentiles`.
- **How probable is an event on a number?** On a regressor, use `predict_proba`
  with `threshold=`. Without a threshold, this is not a regression probability query.
- **Which feature conditions contribute?** Use `explain_factual`.
- **What would the model report under another condition?** Use `explore_alternatives`.

For regression explanations, keep `threshold=` consistent with the event you
predicted. Without a threshold, the explanation concerns the numerical target.
The {doc}`task and mode guide <../foundations/concepts/tasks_modes_capabilities>`
explains these distinctions before introducing API details.

## Core methods

The compact map below uses a classification explainer. For a regressor, follow
the value or threshold section below instead. `uq_interval=True` asks for the
reported lower/upper information as well as the prediction; it does not give
every output the same statistical meaning.


```python
pred = explainer.predict(X_query)
pred, (low, high) = explainer.predict(X_query, uq_interval=True)
probs = explainer.predict_proba(X_query)
probs, (low, high) = explainer.predict_proba(X_query, uq_interval=True)
factual = explainer.explain_factual(X_query)
alternatives = explainer.explore_alternatives(X_query)
```

## Reject-aware prediction note

<details><summary>Advanced: return types when a reject policy is enabled</summary>

When `predict(...)` or `predict_proba(...)` is called with a non-`NONE`
`reject_policy`, the return value is a `RejectResult` envelope. For
`ONLY_ACCEPTED` and `ONLY_REJECTED`, `result.prediction` remains full-batch;
use `result.metadata["source_indices"]` and `result.metadata["matched_count"]`
to identify the matched subset. Reject-enabled `explain_factual(...)` and
`explore_alternatives(...)` return reject-aware collections
(`RejectCalibratedExplanations` / `RejectAlternativeExplanations`), not a
`RejectResult` envelope.

</details>

## Classification

`probs` contains class-probability information; `low` and `high` contain the
reported bounds. Check the class ordering and version-specific return shapes
before selecting a column or displaying a bound. Multiclass handling has an
{doc}`existing limitation <quickstart_classification>`; do not silently clip bounds.


```python
explainer.fit(x_proper, y_proper)
explainer.calibrate(x_cal, y_cal, feature_names=feature_names)
probs, (low, high) = explainer.predict_proba(X_sample, uq_interval=True)
```

## Percentile or interval regression

`pred`, `low` and `high` refer to numerical target values, in the target's units.
The requested 5th/95th percentiles specify a nominal central 90% interval;
interpretation still depends on the method and assumptions in the semantics note.
This snippet assumes a fitted, calibrated regression explainer.


```python
pred, (low, high) = explainer.predict(
    X_sample,
    uq_interval=True,
    low_high_percentiles=(5, 95),
)
```

## Probabilistic or thresholded regression

Here `threshold=120.0` defines the event `Y <= 120.0`, using the target's units.
`p`, `plo` and `phi` describe its probability information, not target values.
Use a threshold meaningful for your dataset, rather than copying this number
into another problem. For explanation calls, see the
{doc}`worked regression example <quickstart_regression>`.


```python
p = explainer.predict_proba(X_sample, threshold=120.0)
p, (plo, phi) = explainer.predict_proba(X_sample, uq_interval=True, threshold=120.0)
```

## Mode-specific semantics notes

The same `low` and `high` variable names do not make the returned quantities
interchangeable. Use the shared {doc}`range guide <../foundations/concepts/calibrated_interval_semantics>`
for the detailed statements and assumptions rather than treating an API snippet
as a guarantee.

### Classification

Select the class before reading its probability and bounds. Check binary versus
multiclass return shapes and the documented multiclass limitation.

### Percentile or interval regression

Read the point prediction and endpoints in the target's units. Percentiles
specify the requested interval; they do not fix its numerical width or guarantee
that this individual outcome is inside it.

### Probabilistic or thresholded regression

Name the event first. Its probability and bounds have a different meaning from
target-value endpoints. Use the same threshold for its explanation calls.

## Continue from a call

- **Understand the returned result:** {doc}`Interpret calibrated explanations <../foundations/how-to/interpret_explanations>`.
- **Understand its construction:** {doc}`How CE Works <../sections/how-ce-works>`.
- **Integrate preprocessing or troubleshoot:** {doc}`Software & Integration <../sections/software-integration>`.
- **Check a result on your data:** {doc}`Checking results <../practitioner/check_results>`.

Entry-point tier: Tier 2.

(optional-capability-api-map)=
## Optional capabilities: concept to software

Start with ordinary fitted/calibrated calls. Enable an option only for a stated
need and after reading its supported setup. The {ref}`optional workflow figure
<ce-optional-capability-map>` shows where these choices fit.

```{include} ../_shared/optional-capabilities.md
```

The public types are imported as follows; this is a lookup, not a complete
example or an instruction to enable both options together:

Import `GuardedOptions` from
`calibrated_explanations.explanations.guarded_options`, and `RejectPolicy` from
`calibrated_explanations.core.reject.policy`.
