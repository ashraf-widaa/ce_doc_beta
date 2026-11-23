# Regression: a value or an event probability?

A regression model predicts a **numerical target**. CE lets you ask two different
questions about that same target. Decide which question you need before choosing
a call or interpreting a range.

## The same target, two questions

Suppose the target is median housing value. “What value, and within what interval?”
asks for target-value information. “How probable is a value at most my budget?”
asks for probability information about an event. You do not change the trained
target by changing the question.

| Question | CE mode | What you read |
| --- | --- | --- |
| What value is predicted? | Interval regression | A numerical prediction and CPS percentile endpoints, in target units. |
| How probable is a defined event? | Probabilistic regression | An event probability and its reported bounds. |

For housing measured in units of $100,000, the threshold for $300,000 is **3**.
Use the units of your own target; do not copy a threshold from another dataset.
The {doc}`interval example <../../get-started/example-interval>` and
{doc}`event example <../../get-started/example-event>` show both readings.

## Before running the snippets

Start with a fitted, calibrated **regression** explainer. `X` below is an array of
query features in the same order and representation used for fitting and
calibration. The unknown query targets are not supplied. If you need setup code,
run the {doc}`regression tutorial <../../get-started/quickstart_regression>` first.
These are lookup snippets, not a separate complete program.

## Ask for a value and its interval

`uq_interval=True` requests the lower and upper information alongside the point
prediction. The percentile pair `(5, 95)` specifies a nominal central 90%
interval. It does not mean that every individual case is covered, or that the
interval has fixed width. Read the precise conditions in
{doc}`Understanding CE ranges <calibrated_interval_semantics>`.

```python
pred, (low, high) = explainer.predict(
    X,
    uq_interval=True,
    low_high_percentiles=(5, 95),
)
```

`pred`, `low` and `high` are in the target's units. Read them together for one
query row. The CPS construction and its residuals are explained in
{doc}`calibration_background`; the numerical values depend on your fitted model,
calibration data and query.

## Ask for an event probability

Here `threshold=150` defines **Y ≤ 150**, using the target's units. It is the
question in the numeric-diabetes Python tutorial, not a housing budget. With a
regression explainer, a threshold selects the event-probability path.

```python
p, (plo, phi) = explainer.predict_proba(
    X,
    threshold=150,
    uq_interval=True,
)
```

In the reviewed return format, `p` has two columns: column 1 is the requested
event probability and column 0 its complement. `plo` and `phi` are the bounds
for the requested event. Check those labels and shapes before selecting values.
These are probability quantities, not target-value endpoints.

The same calibrated regression explainer supports both questions. CE's reviewed
event procedure uses CPS information with Venn–Abers calibration; it is not a
claim that every arbitrary CDF value has the final CE output's properties.

## Explain the same quantity you predicted

For a target-value explanation, omit the threshold from the explanation call.
For an event explanation, pass the **same threshold** to `explain_factual` and
`explore_alternatives`. This keeps prediction, factual weights and alternative
predictions on the same question and scale. The worked
{doc}`regression tutorial <../../get-started/quickstart_regression>` shows this transition.

A factual weight is a comparison of responses; an alternative is a prediction
under another condition. Neither proves what a real-world intervention would do.
Use {doc}`the shared interpretation guide <../how-to/interpret_explanations>`
for records and plots, and {doc}`the semantics reference <calibrated_interval_semantics>`
for assumptions rather than transferring one mode's guarantee to the other.

## Related pages

- {doc}`Task-level event signatures <../../tasks/probabilistic_regression>` for scalar and interval-event calls.
- {doc}`Quick API <../../get-started/quick_api>` to locate a method.
- {doc}`Checking results <../../practitioner/check_results>` to evaluate the selected quantity.

<span id="probabilistic-and-interval-regression"></span>
<span id="mode-routing"></span>
<span id="examples"></span>

<!-- Entry-point tier: Tier 3. -->
