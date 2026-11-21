---
sidebarclass: how-to
---

# Interpret calibrated explanations

<span class="ce-course-step" hidden></span>

Read an explanation by identifying its output, units and range before comparing
feature conditions. Start with the reading steps below; the later sections show
how to inspect the same information in Python payloads and telemetry.

## Read one result first

1. **Name the question.** Is it a class probability, a numerical value, or the
   probability of a defined numerical event? The
   {doc}`task and mode guide <../concepts/tasks_modes_capabilities>` helps choose.
2. **Read the prediction and its range.** Probability bounds use a probability
   scale; numerical intervals use target units. The property name
   `prediction_interval` does not turn every range into a numeric CPS interval.
3. **Read a factual condition and weight.** Identify the condition that holds
   for this case, the direction and size of its model-response comparison, then
   the range reported for that weight. Do not confuse it with the prediction range.
4. **Read one alternative.** Identify its condition and the prediction under that
   condition. It is a model comparison, not an established intervention effect.

For ordinary regression without a threshold, CPS interval percentiles are
controlled by `low_high_percentiles`. With a threshold, read event-probability
information instead. {doc}`Calibrated interval semantics <../concepts/calibrated_interval_semantics>`
is the shared source for assumptions, guarantees and feature-level limitations.
A range crossing zero does not establish a causal effect or a significance test.

**Try a result:** {doc}`Quick Start <../../get-started/index>`.
**Find the calls:** {doc}`Quick API <../../get-started/quick_api>`.

```{admonition} Terminology
:class: tip

- **Factual explanation** – per the original CE classification and regression
  papers, this pairs the calibrated prediction and its uncertainty interval with
  factual feature rules. Every rule binds the observed feature value to a
  condition and surfaces the calibrated feature weight plus its uncertainty
  interval.
- **Alternative explanation** – proposes changes to feature values that would
  produce a different calibrated outcome. Each rule couples the alternative
  condition with the calibrated prediction estimate and uncertainty interval for
  that scenario.
- **Rule** – a feature-level contribution (weight + condition) inside each
  factual explanation and a prediction + condition pair inside each alternative
  explanation. Metadata retains the complementary quantities for ranking and
  provenance.
```

## 1. Start with the explanation collections

The snippets assume a fitted, calibrated `explainer` and a held-out feature
array `x_test`, as prepared by the {doc}`Python tutorial <../../get-started/first-python-explanation>`.
They demonstrate a classification result; the selected row matches the shared Iris lab. For event explanations, pass the same
`threshold=` to both explanation calls as in the event prediction.


Calibrated explanations return collections (`CalibratedExplanations`, `AlternativeExplanations`) that behave like sequences. The first step is to look at the summary for each item:

```python
query = x_test[1:2]  # Same selected Iris row as the shared lab.
factual_batch = explainer.explain_factual(query)
factual = factual_batch[0]
alternative_batch = explainer.explore_alternatives(query)
alternative = alternative_batch[0]

print(f"Mode: {factual.get_mode()}  Calibrated prediction: {factual.predict:.3f}")
print(f"Mode: {alternative.get_mode()}  Calibrated prediction: {alternative.predict:.3f}")
```

Useful attributes and methods shared by factual and alternative explanations:

| Attribute | Description |
| --------- | ----------- |
| `predict` | Calibrated probability (classification) or numeric estimate (regression). |
| `prediction_interval` | Tuple of `(low, high)` values for the explained quantity; interpret it by task and threshold. |
| `build_rules_payload()` | Structured `core` and `metadata` dictionaries; `core["feature_rules"]` lists the rule records. |
| `to_telemetry()` | Instance-level uncertainty and rule records. Collection-level `telemetry` also records component provenance. |

For regression with a scalar `threshold=t`, `predict` concerns `P(Y <= t)`;
an interval threshold defines an interval event. The reported range concerns
that event probability, not percentile endpoints for the target value.
`get_mode()` alone reports classification or regression, so inspect the threshold
and the question as well.

<span id="3-connect-explanations-to-plots"></span>

## 2. Read the plot

A factual plot visualises prediction information, conditions and reported ranges.
Plotting needs the optional visualization dependencies in the same environment:

```bash
python -m pip install "calibrated-explanations[viz]"
```

The following cell uses the factual object created above. The figure is its
output; the reading instructions below explain how its shapes represent the values.

```python
factual.plot(uncertainty=True, filter_top=4)
```

The same selected Iris case appears in the verified example plot below. The
figure is an output to interpret, not evidence that the method's assumptions hold.
Other datasets or renderers need not produce this exact figure.

```{figure} ../../get-started/assets/learning-lab-factual.png
:alt: Verified factual plot for the same Iris versicolor case, showing prediction information above feature conditions, weights and ranges.
:width: 100%

Read prediction information first, then a condition, its weight and its own range.
```

Interpret the chart as follows:

1. **Prediction panel:** in this Iris plot, `y=1` means versicolor and `y!=1`
   means either other species. Read the class probability and its bounds there.
2. **Point weight:** use the printed rule value. For sepal length, it is +0.388
   with reported bounds [0.240, 0.433]; it is not the original class probability.
3. **Solid and translucent portions:** with uncertainty enabled, a positive
   range entirely above zero has a solid portion from zero to its lower bound;
   a negative range entirely below zero has one from its upper bound to zero.
   The overlay shows the reported range. The solid length therefore need not
   equal the point weight. This is a rendering convention, not a new guarantee.
4. **Ranges crossing zero:** the solid portion can be suppressed while the range
   remains visible on both sides. Read the point and endpoints together; this is
   not a significance test or universal per-feature coverage statement.
5. **Colour and labels:** colours depend on the renderer and style. Use signs,
   conditions and numeric records rather than interpreting colour alone.

For an alternative plot, read the alternative prediction and its range on the
same class/event scale as the original case. It is not a factual-weight bar.
The {doc}`alternative guide <../concepts/alternatives>` describes available views.

If the plot and table disagree, check the selected case, filters, output mode and renderer before regenerating. A matching display alone does not validate the statistical assumptions.


<details><summary>Software guide: inspect structured rule payloads</summary>

<span id="2-examine-the-rule-tables-in-detail"></span>

**2. Examine the rule tables in detail**

Rules express model-response comparisons as conditions and reported quantities. Use the helper payloads to inspect them in a structured way.

<span id="21-factual-explanations"></span>

**2.1 Factual explanations**

```python
factual_payload = factual.build_rules_payload()
factual_core = factual_payload["core"]
for rule in factual_core["feature_rules"]:
    interval = rule["weight"]["uncertainty_interval"]
    print(
        f"{rule['condition']['feature']:>20} "
        f"| condition={rule['condition']['operator']} {rule['condition']['value']} "
        f"| weight={rule['weight']['value']:+.3f} "
        f"| weight interval=({interval['lower']:.3f}, {interval['upper']:.3f})"
    )

# the metadata block preserves the detailed calibration artefacts
factual_metadata = factual_payload["metadata"]["feature_rules"]
for extra in factual_metadata:
    print(
        f"  repr={extra['weight_uncertainty']['representation']} "
        f"prediction interval=({extra['prediction_uncertainty']['lower_bound']:.3f}, "
        f"{extra['prediction_uncertainty']['upper_bound']:.3f})"
    )
```

The `build_rules_payload` result is a dictionary with two top-level keys:

- `core` contains the calibrated prediction (`core["prediction"]`) and the factual feature rules (`core["feature_rules"]`).
- `metadata` exposes the full uncertainty records and any derived artefacts (such as the baseline prediction) so downstream consumers can distinguish provenance data from the explanation itself.

Read the factual core from top to bottom:

1. **Weight sign** – positive weights indicate an increase in the explained quantity relative to the comparison response; negative weights indicate a decrease. Identify the class, numeric target or event first. Magnitudes use that quantity’s scale.
2. **Condition** – confirms the feature value observed in the instance (for example, `glucose >= 140`). Use this to cross-check domain constraints.
3. **Prediction** – available through the metadata, showing the calibrated contribution when the feature is perturbed; compare it to `predict` to understand marginal impact.
4. **Weight interval** – the core payload keeps only the numeric bounds; consult the metadata if you need the representation (percentile vs. probabilistic) or raw percentiles used to derive them.

<span id="22-alternative-explanations"></span>

**2.2 Alternative explanations**

Alternative explanations add scenario guidance on top of feature contributions. The payload uses the same helper:

```python
alternative_payload = alternative.build_rules_payload()
alternative_core = alternative_payload["core"]
for rule in alternative_core["feature_rules"]:
    interval = rule["prediction"]["uncertainty_interval"]
    print(
        f"{rule['condition']['feature']:>20} "
        f"| new condition={rule['condition']['operator']} {rule['condition']['value']} "
        f"| predicted value={rule['prediction']['value']:+.3f} "
        f"| interval=({interval['lower']:.3f}, {interval['upper']:.3f})"
    )

alternative_metadata = alternative_payload["metadata"]["feature_rules"]
for extra in alternative_metadata:
    print(
        f"  Stored comparison weight={extra['weight_value']:+.3f} "
        f"(repr={extra['weight_uncertainty']['representation']})"
    )
```

- `core["feature_rules"]` lists the alternative feature conditions alongside the calibrated prediction estimate and uncertainty interval for each alternative scenario.
- `metadata["feature_rules"]` retains the richer calibration context: the stored comparison weight (`weight_value`), detailed uncertainty metadata, and the alternative value used to create the scenario. Do not label the stored weight as alternative-minus-original without checking its convention.

For an explicit prediction change, subtract the original prediction from the
alternative prediction on the same scale. In the shared case, 0.522 minus 0.910
is about -0.388; do not reverse that sign by reusing a differently defined weight.

Compare alternatives using the output quantity, its reported range and relevant
domain constraints. The largest model-response difference is not automatically
the best decision or a feasible action. A wide range calls for further checking;
adding calibration data alone does not guarantee that it will become narrow.

</details>

<details><summary>Software guide: inspect telemetry and provenance</summary>

<span id="4-tie-everything-back-to-telemetry"></span>

**4. Tie everything back to telemetry**

Telemetry records which components produced the explanation; it does not prove statistical validity:

```python
telemetry = getattr(factual_batch, "telemetry", {})
print(telemetry["interval_source"])
print(telemetry["plot_source"])
print(telemetry["uncertainty"])
```

Interpretation tips:

- `interval_source` / `proba_source` show the calibration algorithms in play. Namespaced identifiers such as `registry:interval.default` identify selected plugins; `legacy:` prefixes mean a fallback was used.
- `plot_source` surfaces the renderer (for example `plot_spec.default.factual`). Investigate if a legacy fallback appears unexpectedly.
- The nested `uncertainty` dictionary mirrors the structure already discussed and is the authoritative source for machine-readable exports.
- `preprocessor` provides ADR-009 provenance so you can reproduce how categorical encoders or scalers shaped the data.


</details>

<span id="5-validate-in-notebooks-and-downstream-systems"></span>

## 3. Use the reading in your application

After you absorb the tables and plots:

1. Run the demo notebooks (`demo_under_the_hood.ipynb`, classification/regression demos) and compare their telemetry dumps to your production environment.
2. Embed the interpretation checks into dashboards—surface calibrated prediction vs. interval charts and highlight scenarios with wide rule uncertainty.
3. Share this guide with auditors and stakeholders so everyone relies on the same vocabulary when discussing factual or alternative explanations.

A readable explanation does not by itself establish a safe decision. The next
chapter evaluates held-out results; use {doc}`Software & Integration <../../sections/software-integration>`
when you need an application contract instead.

Entry-point tier: Tier 3.


## Continue the guided introduction

**Previous chapter:** {doc}`../concepts/how_explanations_are_built`.

**Next chapter:** {doc}`Evaluate held-out results <../../practitioner/check_results>`. This sequence is for readers learning CE from the beginning; you can still use this page independently as a topic guide.
