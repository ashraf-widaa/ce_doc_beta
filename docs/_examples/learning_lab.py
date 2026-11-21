# ruff: noqa: E402
# Imports appear in the lesson cell that introduces them.
from __future__ import annotations

# data:start
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Rows are flowers; columns are measurements; y contains species codes.
dataset = load_iris()
x, y = dataset.data, dataset.target
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, stratify=y, random_state=0
)
x_proper, x_cal, y_proper, y_cal = train_test_split(
    x_train, y_train, test_size=0.25, stratify=y_train, random_state=0
)
print("Observations and features:", x.shape)
print("Species:", ", ".join(dataset.target_names))
print("Fit / calibration / evaluation rows:", len(x_proper), len(x_cal), len(x_test))
# data:end

# modes:start
print("Target codes:", sorted(int(value) for value in set(y)))
for code, name in enumerate(dataset.target_names):
    print(f"{code} means {name}")
# modes:end

# calibration:start
from sklearn.ensemble import RandomForestClassifier

from calibrated_explanations import WrapCalibratedExplainer

model = RandomForestClassifier(random_state=0)
explainer = WrapCalibratedExplainer(model)
explainer.fit(x_proper, y_proper)
explainer.calibrate(x_cal, y_cal, feature_names=dataset.feature_names)
assert explainer.fitted and explainer.calibrated
case = x_test[1:2]  # Features only; its target is not an input to CE.
raw = model.predict_proba(case)[0]
probabilities, (low, high) = explainer.predict_proba(case, uq_interval=True)
class_index = int(probabilities[0].argmax())
print("Raw model probabilities:", ", ".join(f"{p:.3f}" for p in raw))
print("CE probabilities:", ", ".join(f"{p:.3f}" for p in probabilities[0]))
print("Selected class:", dataset.target_names[class_index])
print(f"Reported bounds: [{low[0, class_index]:.3f}, {high[0, class_index]:.3f}]")
# calibration:end

# explanation:start
factual = explainer.explain_factual(case)
alternatives = explainer.explore_alternatives(case)
rule = factual[0].build_rules_payload()["core"]["feature_rules"][0]
condition = rule["condition"]
weight = rule["weight"]
interval = weight["uncertainty_interval"]
print("Factual condition:", condition["feature"], condition["operator"], condition["value"])
print(f"Weight: {weight['value']:+.3f}")
print(f"Weight bounds: [{interval['lower']:.3f}, {interval['upper']:.3f}]")
alt_rules = alternatives[0].build_rules_payload()["core"]["feature_rules"]
print("Alternative rules for this case:", len(alt_rules))
if alt_rules:
    alt = alt_rules[0]
    print("Alternative condition:", alt["condition"]["feature"], alt["condition"]["operator"], alt["condition"]["value"])
    print(f"Alternative prediction: {alt['prediction']['value']:.3f}")
# explanation:end

# checking:start
from sklearn.metrics import accuracy_score, log_loss

predicted_labels = explainer.predict(x_test)
all_probabilities, (all_low, all_high) = explainer.predict_proba(
    x_test, uq_interval=True
)
print("Evaluation rows:", len(y_test))
print(f"Accuracy: {accuracy_score(y_test, predicted_labels):.3f}")
class_codes = list(range(len(dataset.target_names)))
loss = log_loss(y_test, all_probabilities, labels=class_codes)
print(f"Log loss: {loss:.3f}")
out_of_range_bounds = (all_low < 0) | (all_high > 1)
print("Out-of-range class-bound entries:", int(out_of_range_bounds.sum()))
# checking:end
