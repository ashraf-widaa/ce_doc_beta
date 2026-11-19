# Calibration and statistical background

Why can a confident-looking prediction still need calibration? This page
introduces the statistical ideas; it does not replace the version-specific
{doc}`guarantees and limits <calibrated_interval_semantics>`.

## Accuracy and calibration answer different questions

Classification accuracy checks how often predicted labels match observed labels.
Probability calibration concerns how probability estimates relate to outcome
frequencies. A hypothetical group of predictions near 0.8 illustrates the idea:
we would compare the positive-outcome frequency in that group with 0.8. This is
an explanatory example, not a measurement from CE or a browser application.

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

## Why separate calibration data matters

A fitted model has already used its fitting data. A calibration procedure uses
additional labelled cases to relate model outputs to observed outcomes or
construct a predictive distribution. An evaluation set has a different job:
checking the resulting system after fitting and calibration decisions.

In the {doc}`first Python example <../../get-started/first-python-explanation>`,
the separate data roles are:

```{include} predictive_tasks.md
:start-after: <!-- data-roles:start -->
:end-before: <!-- data-roles:end -->
```

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

## Regression: predictive distributions and quantiles

A conformal predictive system (CPS) uses calibration information to construct
predictive information for a numeric target. A useful background concept is a
predictive cumulative distribution function, {math}`F_x(y)`: it describes cumulative
probability up to target value {math}`y` for a query with features {math}`x`.

For a CDF, a quantile can be defined as

```{math}
Q_\gamma(x)=\inf\{y:F_x(y)\ge\gamma\}.
```

A lower and upper percentile describe a target-value interval. For example,
5th/95th percentile settings describe a nominal central 90% interval. This
explains the settings; it is not a new theorem about CE's finite-sample or
individual-case coverage. Formal interpretation depends on the construction,
sampling conditions and source version.

An event question instead evaluates an event such as {math}`Y\le t` or
{math}`a<Y\le b`. CE's event-probability procedure is described separately in
{doc}`probabilistic_regression`. Do not replace that procedure with a claim that
an arbitrary numeric interval is an event-probability confidence interval.

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

## From understanding to checking

Use {doc}`Checking results on your data <../../practitioner/check_results>` for
held-out evaluation questions. Return to {doc}`How CE Works <../../sections/how-ce-works>`
for the learning route, or inspect the
{doc}`explanation construction <how_explanations_are_built>` next.
