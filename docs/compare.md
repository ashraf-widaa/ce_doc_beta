# Choosing an explanation approach

<!-- Preserve descriptive anchors from the previous review layout. -->
<span id="vs-conformal-prediction-packages"></span>
<span id="vs-lime"></span>
<span id="vs-shap"></span>


<span id="calibrated-explanations-comparisons-ce-first"></span>

What question do you need answered, and about which model output? These methods
have different goals; this is not a universal performance ranking.

| Approach | Typical question / output | What to check |
| --- | --- | --- |
| CE | Task-specific calibrated prediction information with factual/alternative conditions and reported ranges. | Calibration data, mode, output semantics and assumptions; alternatives are model comparisons, not guaranteed interventions. |
| SHAP | Feature attributions for a chosen model output relative to a reference/background construction. | Output being explained, background data and explainer assumptions; it can be used with a calibrated model. |
| LIME | A local surrogate explanation around a query under its chosen perturbation/sampling setup. | Locality, sampling and surrogate fidelity; explaining a score does not itself calibrate that score. |
| Counterfactual methods | Changes associated with a different model outcome under the method's search/constraints. | Feasibility, actionability and model-versus-world meaning; properties depend on the method. |
| Conformal prediction tools | Prediction sets, intervals or predictive information under a specified construction. | Task, assumptions and coverage semantics; a prediction interval alone is not a feature explanation. |

CE's factual weights are not Shapley values. CE alternatives need not be minimal
or feasible, and reported explanation ranges do not create a causal guarantee.
Any claim that one approach is more stable or better performing needs a defined
task, evaluation protocol and supporting evidence.

Primary background: [SHAP documentation](https://shap.readthedocs.io/),
[LIME project](https://github.com/marcotcr/lime), and
[DiCE documentation](https://interpret.ml/DiCE/).

Continue with {doc}`What & Why <sections/what-and-why>`,
{doc}`task/mode/capability choices <foundations/concepts/tasks_modes_capabilities>`
or the {doc}`browser Quickstart <get-started/index>`.
