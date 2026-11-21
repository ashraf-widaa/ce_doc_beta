# Regression quickstart

Use the same regression model to answer two questions: a numerical value with
an interval, then the probability of a threshold event. Run the cells in order
in one session. This example uses scikit-learn's numeric diabetes target, not
the Pima binary Diabetes data in the browser guide. The target measures disease
progression one year after baseline; the features are baseline measurements.

For a no-install route, use the {doc}`interval example <example-interval>` or
{doc}`event example <example-event>`. For the concepts behind these choices,
read {doc}`tasks and modes <../foundations/concepts/tasks_modes_capabilities>`.

## Prerequisites

```bash
pip install calibrated-explanations scikit-learn
```

## Interval regression semantics note

- **Calibration prerequisites**: fit on `x_proper, y_proper` and calibrate on held-out `x_cal, y_cal`.
- **Mode-specific guarantees**: percentile intervals use CPS for requested percentile bounds.
- **Assumptions**: calibration and deployment data are exchangeable or distribution-matched.
- **Explicit non-guarantees**: no guarantee under drift or fixed interval width across subpopulations.
- **Explanation-envelope limits**: feature-level intervals summarize model behavior under perturbation.
- **Formal semantics**: {doc}`../foundations/concepts/calibrated_interval_semantics`.

## Probabilistic or thresholded regression semantics note

- **Calibration prerequisites**: fit on `x_proper, y_proper` and calibrate on held-out `x_cal, y_cal`.
- **Mode-specific guarantees**: threshold queries use CPS with Venn-Abers for calibrated event probabilities.
- **Assumptions**: calibration and deployment data are exchangeable or distribution-matched.
- **Explicit non-guarantees**: no guarantee under drift, and no causal guarantee from threshold probabilities.
- **Explanation-envelope limits**: feature-level intervals summarize model behavior under perturbation.
- **Formal semantics**: {doc}`../foundations/concepts/calibrated_interval_semantics`.

## 1. Prepare the dataset

Load the numeric target and reserve evaluation rows. Split the remaining rows
into model-fitting and calibration sets. Targets are known for these datasets,
but query targets are not passed to prediction or explanation calls.


```python
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

dataset = load_diabetes()
x = dataset.data
y = dataset.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=0
)
x_proper, x_cal, y_proper, y_cal = train_test_split(
    x_train, y_train, test_size=0.25, random_state=0
)
```

This cell creates arrays without printing output: 264 proper-training rows,
89 calibration rows and 89 evaluation rows. Use the
{doc}`data-role guide <../foundations/concepts/predictive_tasks>` if needed,
then continue with the same arrays.

## 2. Fit and calibrate the explainer

Fit the random forest on the proper-training set. Calibration then uses the
separate labelled calibration set. This cell prepares the wrapper without
printing a result; it does not evaluate the resulting system.


```python
from sklearn.ensemble import RandomForestRegressor
from calibrated_explanations import WrapCalibratedExplainer

explainer = WrapCalibratedExplainer(RandomForestRegressor(random_state=0))
explainer.fit(x_proper, y_proper)
explainer.calibrate(x_cal, y_cal, feature_names=dataset.feature_names)
```

## 3. Interval and threshold predictions

### Ask for a value and its interval

Without a threshold, read `pred`, `low` and `high` in this dataset's target units.
The factual explanation compares numerical model responses; its weights are
also in target units. This is the interval-regression route.

```python
pred, (low, high) = explainer.predict(x_test[:3], uq_interval=True)
value_factual = explainer.explain_factual(x_test[:1])
value_alternatives = explainer.explore_alternatives(x_test[:1])
print("Value predictions:", pred.round(3))
print("Lower endpoints:", low.round(3))
print("Upper endpoints:", high.round(3))
```

```{literalinclude} ../_examples/guided_regression_output.txt
:language: text
:start-after: VALUE_START
:end-before: VALUE_END
```

Read corresponding positions together: the first prediction and the first pair
of endpoints describe one evaluation case. These are target values, not
probabilities. Inspect `value_factual[0]` and `value_alternatives[0]` using the
{doc}`interpretation guide <../foundations/how-to/interpret_explanations>`.

### Ask for an event probability

Now keep the regression model but change the question to `P(Y <= 150)`.
`probabilities` and `probability_interval` concern that event, not the numeric
target itself. Passing the same threshold to the explanation call makes its
weights probability differences for that event. Do not reinterpret the preceding
`value_factual` weights as probability differences.

```python
probabilities, probability_interval = explainer.predict_proba(
    x_test[:1], threshold=150, uq_interval=True
)
event_factual = explainer.explain_factual(x_test[:1], threshold=150)
print("Event probabilities:", probabilities.round(3))
print("Event lower bounds:", probability_interval[0].round(3))
print("Event upper bounds:", probability_interval[1].round(3))
```

```{literalinclude} ../_examples/guided_regression_output.txt
:language: text
:start-after: EVENT_START
:end-before: EVENT_END
```

In this reviewed interface, the probability row is `[P(Y > 150), P(Y <= 150)]`:
`0.077` is the event probability requested here; `0.923` is its complement.
The lower and upper arrays concern the requested event, giving `[0.000, 0.083]`
for this case. Their scale differs from the target-value arrays above. The output layout is version-specific; use
{doc}`Quick API <quick_api>` and the API contract before wiring it into a display.
One observed outcome cannot establish calibration or coverage.

## 4. Explore alternatives

Continue the event question with the same threshold. Each alternative describes
the event probability under a different condition; it is not an established
intervention effect. For interval-regression alternatives, use
`value_alternatives` from the value route above instead.


```python
alternatives = explainer.explore_alternatives(x_test[:2], threshold=150)
```

The cell returns a collection for two cases; it does not print a result. Compare
an alternative's event probability with the original case's event probability,
not with a numeric target-value weight. Output numbers above are captured from
the review environment and may vary with package versions; do not modify
outputs or clip bounds to force a match.

**Check before adapting:** {doc}`Checking results on your data <../practitioner/check_results>`.
**Connect to software:** {doc}`Software & Integration <../sections/software-integration>`.

Next steps:
- {doc}`../foundations/concepts/probabilistic_regression`
- {doc}`../foundations/how-to/interpret_explanations`
- {doc}`../citing`

Entry-point tier: Tier 2.
