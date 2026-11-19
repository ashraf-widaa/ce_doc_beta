# Calibrated Explainer API

This reference documents the public API for the `calibrated_explanations` package. It includes the main explainer classes, the explanation containers, and the specific explanation types.

For the reviewed source's multiclass bound limitation, see the
{doc}`classification tutorial <../get-started/quickstart_classification>`. Keep unexpected
raw output for diagnosis rather than clipping it.

## Core Explainers

The core of the library is the `CalibratedExplainer`, which handles the calibration of the underlying model. For a scikit-learn compatible interface, use `WrapCalibratedExplainer`.

### CalibratedExplainer

The `CalibratedExplainer` is the core class of the library. It takes a machine learning model (classifier or regressor) and a calibration dataset. It fits Venn-Abers calibrators (for classification) or Conformal Predictive Systems (for regression) to the model's predictions. These classes provide task-specific prediction information and explanation outputs. Their statistical meaning depends on the method and assumptions; see {doc}`canonical semantics <../foundations/concepts/calibrated_interval_semantics>`.

For a task-oriented view of the same capabilities (classification, conformal interval regression via CPS, and probabilistic/thresholded regression), see {doc}`../tasks/index`.

**Example Usage:**

```python
from calibrated_explanations import CalibratedExplainer
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load data
X, y = load_iris(return_X_y=True)
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=0
)
x_train, x_cal, y_train, y_cal = train_test_split(
    x_train, y_train, test_size=0.25, stratify=y_train, random_state=0
)

# Train model
model = RandomForestClassifier(random_state=0)
model.fit(x_train, y_train)

# Initialize explainer
explainer = CalibratedExplainer(model, x_cal, y_cal, mode='classification')

# Explain a test instance
explanations = explainer.explain_factual(x_test[:1])
```

{doc}`Generated class and method reference <../_autosummary/calibrated_explanations.core.CalibratedExplainer>`

### WrapCalibratedExplainer

The `WrapCalibratedExplainer` acts as a wrapper around `CalibratedExplainer` to provide a standard scikit-learn interface (`fit`, `predict`, `predict_proba`). Callers retain control of the proper-training and held-out calibration splits: call `fit(...)`, then `calibrate(...)`, before requesting predictions or explanations.

**Example Usage:**

```python
from calibrated_explanations import WrapCalibratedExplainer
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load data
X, y = load_iris(return_X_y=True)
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=0
)
x_proper, x_cal, y_proper, y_cal = train_test_split(
    x_train, y_train, test_size=0.25, stratify=y_train, random_state=0
)

# Initialize wrapper with a base model
model = RandomForestClassifier(random_state=0)
wrapper = WrapCalibratedExplainer(model)

# Fit on the proper-training split and calibrate on held-out data
wrapper.fit(x_proper, y_proper)
wrapper.calibrate(x_cal, y_cal)

# Explain through the canonical public method
explanations = wrapper.explain_factual(x_test[:1])
```

{doc}`Generated class and method reference <../_autosummary/calibrated_explanations.core.WrapCalibratedExplainer>`

## Explanation Containers

When you request explanations for a set of instances, the result is returned in a `CalibratedExplanations` object. This collection holds the individual explanations and provides methods for visualization and export.

### CalibratedExplanations

A `CalibratedExplanations` object is returned when you call `explain_factual()` on a `CalibratedExplainer` or `WrapCalibratedExplainer`. It is a collection of explanations for the provided test instances. It serves as a container that allows you to iterate over individual explanations, visualize them, or export them.

**Example Usage:**

```python
# Assuming 'explanations' is a CalibratedExplanations object
# Iterate over explanations
for explanation in explanations:
    print(explanation.prediction)

# Plot all explanations
explanations.plot()

# Get a specific explanation
first_explanation = explanations[0]
```

**Metadata Attributes:**

When FAST-based feature filtering is enabled (experimental), the `CalibratedExplanations` object may include additional metadata for transparency and debugging:

- `feature_filter_per_instance_ignore`: On the returned collection, a best-effort list of per-instance feature-index masks produced by filtering. The `CalibratedExplainer` also exposes the transient mask from the most recent filtered batch under the same attribute name. This diagnostic metadata is not part of the stable API.

{doc}`Generated class and method reference <../_autosummary/calibrated_explanations.explanations.CalibratedExplanations>`

## Explanation Types

Individual explanations are represented by specific classes depending on the type of explanation requested.

### CalibratedExplanation

This is the abstract base class for a single explanation. It contains the instance data, the prediction, and the feature weights (rules) that explain the prediction. It provides methods for plotting the explanation.

{doc}`Generated class and method reference <../_autosummary/calibrated_explanations.explanations.CalibratedExplanation>`

### FactualExplanation

A `FactualExplanation` explains the model's calibrated prediction for an instance through local feature rules, weights, and uncertainty intervals. It describes the observed instance; use `explore_alternatives(...)` when you need candidate changes.

**Example Usage:**

```python
# Plot a factual explanation
factual_explanation.plot()

# Add a conjunction to the explanation
factual_explanation.add_conjunctions()
```

{doc}`Generated class and method reference <../_autosummary/calibrated_explanations.explanations.FactualExplanation>`

### AlternativeExplanation

An `AlternativeExplanation` (often called a counterfactual explanation) explores *what if* scenarios. It suggests changes to the feature values that would result in a different prediction (e.g., flipping a classification label or moving a regression prediction into a different range).

**Example Usage:**

```python
# Plot an alternative explanation
alternative_explanation.plot()
```

{doc}`Generated class and method reference <../_autosummary/calibrated_explanations.explanations.AlternativeExplanation>`

Entry-point tier: Tier 3.
