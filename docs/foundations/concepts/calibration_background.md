# Calibration and statistical background

<span class="ce-course-step" hidden></span>

Why can a confident-looking prediction still need calibration? This page
introduces the statistical ideas; it does not replace the version-specific
{doc}`guarantees and limits <calibrated_interval_semantics>`.

## Choose the background you need

For a first example, you mainly need to distinguish a probability range from a
numeric prediction interval and keep training, calibration and evaluation data
separate. The sections below explain why. The equations are optional background;
they are not prerequisites for following the Quick Start.

If supervised learning is new to you, start with
[Google's introduction to supervised learning](https://developers.google.com/machine-learning/intro-to-ml/supervised),
then return to CE's {doc}`predictive tasks and data roles <predictive_tasks>`.
External resources explain general concepts; CE's own output meanings and
limitations remain in the linked internal guides.

## Accuracy and calibration answer different questions

Classification accuracy checks how often predicted labels match observed labels.
Probability calibration concerns how probability estimates relate to outcome
frequencies. A hypothetical group of predictions near 0.8 illustrates the idea:
we would compare the positive-outcome frequency in that group with 0.8. This is
an explanatory example, not a measurement from CE or a browser application.

<details><summary>Go deeper: the ideal calibration equation and its limits</summary>

An ideal population definition for a binary outcome is

```{math}
\Pr(Y=1\mid \widehat p(X)=p)=p.
```

Here, {math}`Y=1` is the chosen positive class and {math}`\widehat p(X)` is a reported
probability. In practice we have finite samples, often grouped into bins, so
observed frequencies have sampling variation. This ideal definition is **not**
a theorem that every CE merged probability satisfies this equality on every
dataset. See [scikit-learn's probability calibration guide](https://scikit-learn.org/stable/modules/calibration.html)
for general background and the CE semantics reference for method-specific claims.

</details>

## Why separate calibration data matters

A fitted model has already used its fitting data. A calibration procedure uses
additional labelled cases to relate model outputs to observed outcomes or
construct a predictive distribution. An evaluation set has a different job:
checking the resulting system after fitting and calibration decisions.

The shared lab has already reserved proper training, calibration and evaluation
rows. We now use the calibration rows; the evaluation outcomes remain for the
final check. The {doc}`data-role chapter <predictive_tasks>` owns the full definitions
and split code, so you do not need to prepare a second dataset here.

Keep preprocessing and model selection from leaking evaluation information into
that workflow. The introductory three-way split is a teaching pattern, not a
universal choice of proportions. Small or unrepresentative calibration data can
limit usefulness even when the calls succeed.

## Classification: Venn–Abers probability information

CE uses Venn–Abers constructions for classification. The reported probability
and the returned pair/bounds need their own interpretation; they are not a
confidence interval certifying an individual's true probability. Multiclass
handling also needs its version-specific qualifications. Do not infer validity
from endpoints merely lying between zero and one.

The {doc}`semantics reference <calibrated_interval_semantics>` states the source
version's claims. The {doc}`Python tutorial <../../get-started/quickstart_classification>`
records a reviewed multiclass output limitation. Its presence is not permission
to clip values or silently reinterpret them.

## How the binary Venn–Abers construction works

Start with two objects: the fitted classifier supplies scores; the calibrator
uses scores and known outcomes from separate calibration cases. Fitting a
calibration mapping does not retrain the predictive classifier.

A classifier produces a **score** for a class. Calibration relates scores to
known outcomes from the calibration cases. Venn–Abers uses **isotonic regression**:
a non-decreasing mapping, so increasing the score cannot decrease the fitted
mapping's value. Here “regression” names the calibration mapping; the predictive
task remains classification. It is not retraining the classifier.

The binary construction considers two possible labels for the new scored case:
0 and 1. It performs the corresponding isotonic constructions and obtains a pair
of probability values. The new case's true label is not known or required; the
two labels are hypothetical parts of the algorithm. CE also reports a point
probability derived from the underlying construction.

This explains why there is more than one reported number. It does **not** make
the pair a conventional confidence interval for the individual's unknown true
probability, or transfer a property of the pair unchanged to a merged point.
Multiclass processing adds class-wise handling and normalization; its returned
bounds need their own qualifications. See the
[original Venn–Abers paper](https://arxiv.org/abs/1211.0025) for the construction
and the internal semantics page for CE-specific interpretation.

## See calibration in the shared Python example

Continue the Iris arrays from {doc}`predictive_tasks`. `RandomForestClassifier`
is the predictive learner: a random forest combines predictions from multiple
decision trees. It is one compatible model, not a requirement to prefer random
forests when using CE. `WrapCalibratedExplainer` coordinates fitting and
calibration. `case` contains one row's features; `class_index` identifies the
column selected by the largest reported class probability. `case = x_test[1:2]`
keeps one row in a two-dimensional array; `argmax()` finds the largest probability
column, and `target_names` maps that column to a species name. In this multiclass
return, `[0, class_index]` selects row zero and that class’s bound. The raw-model row
is shown deliberately as a calibration comparison, not as the default CE result.

```{literalinclude} ../../_examples/learning_lab.py
:language: python
:start-after: calibration:start
:end-before: calibration:end
```

Verified output from the review environment:

```{literalinclude} ../../_examples/learning_lab_output.txt
:language: text
:start-after: CALIBRATION_START
:end-before: CALIBRATION_END
```

The raw model reports 1.000 for versicolor in this captured case; CE reports 0.910
with bounds [0.902, 0.992]. Both rows use the class order setosa, versicolor,
virginica. A raw value of 1.000 is a model report, not certainty about the world.
The change itself does not prove CE is better calibrated: that requires held-out
checks across cases. These are version-specific observed values, not a guarantee
that another query will have well-behaved multiclass bounds. The existing
multiclass limitation remains in the classification tutorial.

The assertions check that fitting and calibration completed. They do not test
exchangeability, distribution shift or the validity of a statistical claim.


## Regression: predictive distributions and quantiles

A conformal predictive system (CPS) uses calibration information to construct
predictive information for a numeric target. A useful background concept is a
**cumulative distribution function (CDF)**: it accumulates probability up to a
chosen target value. A query supplies the features; moving along the target
scale changes the cumulative probability.

A **quantile** is a location on that distribution at a specified cumulative
probability. Percentiles express those locations out of 100. The 5th and 95th
percentiles therefore mark two target values, rather than two class probabilities.

<details><summary>Go deeper: quantile notation</summary>

Write the predictive CDF as {math}`F_x(y)` for query features {math}`x` and target
value {math}`y`. For a CDF, a quantile can be defined as

```{math}
Q_\gamma(x)=\inf\{y:F_x(y)\ge\gamma\}.
```

</details>

A lower and upper percentile describe a target-value interval. For example,
5th/95th percentile settings describe a nominal central 90% interval. This
explains the settings; it is not a new theorem about CE's finite-sample or
individual-case coverage. Formal interpretation depends on the construction,
sampling conditions and source version.

An event question instead evaluates an event such as {math}`Y\le t` or
{math}`a<Y\le b`. CE's event-probability procedure is described separately in
{doc}`probabilistic_regression`. Do not replace that procedure with a claim that
an arbitrary numeric interval is an event-probability confidence interval.

## How residuals connect a regressor to CPS

A **residual** is an observed target minus its model prediction. For calibration
case i, write it as {math}`r_i=y_i-\hat f(x_i)`, where {math}`\hat f` is the fixed
fitted regressor. Positive residuals mean underprediction for those cases;
negative residuals mean overprediction. This is an explanation of the sign,
not a claim that a future case will have the same error.

CE's interval-regression implementation computes calibration residuals and fits
a CPS using them; optional difficulty estimates and groups affect the construction.
Conceptually, comparing a candidate target with the calibration information gives
predictive distribution information for a new case. Percentiles select locations
on that distribution. The exact endpoint, tie and sampling conventions matter;
a histogram of errors alone is not a complete specification or proof of CPS validity.
For the original construction and conditions, see
[Vovk et al., Nonparametric predictive distributions based on conformal prediction](https://doi.org/10.1007/s10994-018-5755-8).

This is why numerical interval endpoints have the target's units. Follow the
{doc}`existing regression tutorial <../../get-started/quickstart_regression>` to
run the value question, inspect its printed endpoints and read them together.

## Why an event question needs a different reading

For a threshold t, define a binary event: did the numerical outcome satisfy
{math}`Y\le t`? The target is still numerical, but the requested result is now a
probability. The reviewed implementation uses split-CPS scores with Venn–Abers
calibration for event probabilities. Do not replace that procedure with an
assumption that any fitted CDF value is already the final CE output.

In the regression tutorial, `threshold=150` requests `P(Y <= 150)`. Its output
shows both that probability and its complement, then bounds for the requested
event. Return to {doc}`probabilistic_regression` when choosing between these
questions. The method and its assumptions, not the visual shape of a bar,
determine which validity statement may apply.


## Exchangeability, coverage and changing populations

Exchangeability expresses symmetry of the joint distribution under reordering
of observations. Independent, identically distributed cases provide an important
sufficient example; exchangeability is not identical to independence.

Coverage statements generally concern repeated cases under a specified method
and assumptions. They do not mean that every particular case or subgroup receives
the same guarantee. Distribution shift, dependent sampling, subgroup differences
and changing data collection can matter. Successful calibration calls alone do
not establish the required conditions.

Consult the {doc}`canonical assumptions and non-guarantees <calibrated_interval_semantics>`
and the linked {doc}`research literature <../../researcher/advanced/theory_and_literature>`
for the actual CE statements. Exact merged-probability and multiclass wording
remain author-review topics in this independent documentation work.

<span id="from-understanding-to-checking"></span>

## Continue the guided introduction

**Previous chapter:** {doc}`tasks_modes_capabilities`.

**Next chapter:** {doc}`From predictions to explanations <how_explanations_are_built>`. This sequence is for readers learning CE from the beginning; you can still use this page independently as a topic guide.

<!-- Entry-point tier: Tier 3. -->
