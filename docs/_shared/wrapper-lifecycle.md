| Step | Concept: what happens | Software entry point |
| --- | --- | --- |
| **1. Wrap** | Use one interface to a compatible predictive ML model. The wrapper is not a second predictive model. | `WrapCalibratedExplainer(model)` |
| **2. Fit** | Training data supply features and known targets to fit the predictive model. Skip this step if the model is already fitted. | `explainer.fit(X_train, y_train)` |
| **3. Calibrate** | Separate labelled calibration data prepare method-specific calibration and reference information around the fixed predictive model. | `explainer.calibrate(X_cal, y_cal)` |
| **4. Predict** | Use test-data or new-case features to obtain prediction information. Request reported ranges explicitly; choose the call for your task and output question. | `explainer.predict(...)` or `explainer.predict_proba(...)`, with `uq_interval=True` |
| **5a. Factual explanation** | Inspect conditions holding for the case, with comparison weights and their ranges. | `explainer.explain_factual(X_case)` |
| **5b. Alternative explanations** | Compare predictions and ranges under other feature conditions. | `explainer.explore_alternatives(X_case)` |

`X_case` means the features of the selected test observations or new cases. Other
pages may name the same role `X_query` or `x_test`; these are variable names, not
different CE capabilities. Their targets are not supplied to prediction or
explanation calls. Test targets are kept separately for evaluation.

Steps 5a and 5b are complementary choices. An explanation call obtains the
prediction information it needs internally; a separate step-4 call is not
required. For an event-probability question, keep `threshold=` consistent across
prediction and explanation calls. Without a threshold, numerical-regression
explanations concern target values. These lookup calls assume compatible data
and a fitted, calibrated wrapper; use a complete example for setup.
