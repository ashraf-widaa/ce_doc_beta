# Integrate with scikit-learn pipelines

<span class="ce-choice-page" hidden></span>

A preprocessing pipeline turns raw columns into model inputs. Imputation learns
how to fill missing values; scaling learns how to express measurements on a new
scale. Those learned transformations must be applied consistently at fitting,
calibration and query time. This guide follows one complete software task after
the conceptual introduction.

WrapCalibratedExplainer can manage preprocessing pipelines so calibration and
inference use the same transformations.

## Configure a preprocessing pipeline

This example uses a binary breast-cancer dataset supplied by scikit-learn and
selects three numerical columns for illustration. The `ColumnTransformer` drops
other columns; it does not imply those features are unimportant. Start a fresh session or run all cells from the top; this example is independent
of the Iris lab. The first cell prepares split arrays and a configured wrapper
without printing output.

`ColumnTransformer` selects columns and `Pipeline` applies transformations in
order. `SimpleImputer` learns training medians for missing values;
`StandardScaler` learns training means and standard deviations for feature
standardization. It does not normalize class probabilities. The random forest
here does not require scaling; scaling is included to demonstrate consistent
preprocessing. `ExplainerConfig` holds the model and preprocessing settings,
and `from_config` creates the public wrapper from them.


```python
from sklearn.compose import ColumnTransformer
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from calibrated_explanations.api.config import ExplainerConfig
from calibrated_explanations import WrapCalibratedExplainer

dataset = load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(
    dataset.data,
    dataset.target,
    test_size=0.2,
    stratify=dataset.target,
    random_state=0,
)
x_proper, x_cal, y_proper, y_cal = train_test_split(
    x_train,
    y_train,
    test_size=0.25,
    stratify=y_train,
    random_state=0,
)

numeric = [0, 1, 2]
preprocessor = ColumnTransformer(
    [
        (
            "num",
            Pipeline(
                steps=[
                    ("impute", SimpleImputer(strategy="median")),
                    ("scale", StandardScaler()),
                ]
            ),
            numeric,
        )
    ],
    remainder="drop",
)

config = ExplainerConfig(
    model=RandomForestClassifier(random_state=0),
    preprocessor=preprocessor,
)
explainer = WrapCalibratedExplainer.from_config(config)
```

In the sequence below, `fit` learns the preprocessing transformation and the
predictive model from the proper training data. `calibrate` then applies the
already fitted transformation to calibration features and builds CE's calibrated
runtime; it does not refit the learner. This distinction prevents the roles from
being confused. When wrapping a pre-fitted model, ensure its preprocessing is
consistent with the representation on which it was trained.

```python
explainer.fit(x_proper, y_proper)
explainer.calibrate(x_cal, y_cal)
factual = explainer.explain_factual(x_test[:1])
print("Explained rows:", len(factual))
```

Verified output for the second cell:

```text
Explained rows: 1
```

It returns one explanation for one held-out row, not an evaluation of the whole
system. Read the next cell's telemetry as optional provenance, not statistical
validation. Inspect one item with
{doc}`Interpret calibrated explanations <interpret_explanations>` before exporting
it. If a call fails, use {doc}`Troubleshooting <../../get-started/troubleshooting>`.

## Inspect telemetry snapshots

The runtime attaches preprocessing metadata to telemetry so you can audit which
transformers executed:

```python
telemetry = explainer.runtime_telemetry
pre = telemetry.get("preprocessor", {})
print(pre.get("transformer_id"))
print(pre.get("mapping_snapshot"))
```

Each entry includes the transformer identifier, mapping snapshot (when
available), and whether auto-encoding is enabled.

## Tips

- Keep preprocessing deterministic so calibration and inference remain aligned.
- Prefer column selectors over positional slicing when working with pandas
  DataFrames.
- Construct configured wrappers through the public
  `WrapCalibratedExplainer.from_config(config)` factory.

> **Telemetry note:** Runtime telemetry remains opt-in. Enable it only when governance teams need pipeline provenance, then follow {doc}`configure_telemetry` to capture preprocessing metadata for each batch.

## Classification semantics for this example

- **Calibration prerequisites:** fit the learner and preprocessing on proper training data; calibrate on separate labelled data.
- **Guarantees:** use the classification statements in the shared semantics reference, not successful execution as evidence of validity.
- **Assumptions:** check the mode's sampling and calibration/deployment conditions.
- **Non-guarantees:** no individual-case certainty or unconditional guarantee under drift.
- **Feature-level limits:** weight ranges describe model-response comparisons, not causal effects or universal feature coverage.
- **Reference:** {doc}`../concepts/calibrated_interval_semantics`.

<!-- Entry-point tier: Tier 2. -->

## Continue the software guide

**Next:** {doc}`Runtime configuration <configure_runtime>` when you need to control
execution settings. For presenting the returned result, use
{doc}`Export explanations <export_explanations>`. If a call failed, use
{doc}`Troubleshooting <../../get-started/troubleshooting>` before adding more settings.
