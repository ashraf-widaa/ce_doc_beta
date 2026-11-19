from __future__ import annotations

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from calibrated_explanations import WrapCalibratedExplainer

dataset = load_iris()
x = dataset.data
y = dataset.target

# Set aside evaluation rows before splitting model-fitting and calibration rows.
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, stratify=y, random_state=0
)
x_proper, x_cal, y_proper, y_cal = train_test_split(
    x_train, y_train, test_size=0.25, stratify=y_train, random_state=0
)

explainer = WrapCalibratedExplainer(RandomForestClassifier(random_state=0))
explainer.fit(x_proper, y_proper)
explainer.calibrate(x_cal, y_cal, feature_names=dataset.feature_names)

# Explain the second held-out case, using only its features.
case = x_test[1:2]
probabilities, (low, high) = explainer.predict_proba(case, uq_interval=True)
class_index = int(probabilities[0].argmax())
class_name = dataset.target_names[class_index]
factual = explainer.explain_factual(case)

print(f"Data rows: fit={len(x_proper)}, calibrate={len(x_cal)}, evaluate={len(x_test)}")
print(f"Predicted class: {class_name}")
print("Class probabilities: " + ", ".join(f"{p:.3f}" for p in probabilities[0]))
print(f"Reported bounds for {class_name}: [{low[0, class_index]:.3f}, {high[0, class_index]:.3f}]")
print(f"Factual explanations: {len(factual)}")

factual[0].plot(uncertainty=True, filter_top=4)
