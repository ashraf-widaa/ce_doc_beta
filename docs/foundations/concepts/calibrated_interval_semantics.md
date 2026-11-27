---
tocdepth: 2
---

# Understanding CE ranges

CE can return several pairs of lower and upper values. **Before interpreting a
range, identify what it describes:** a class probability, a numerical target,
an event probability or a feature weight. A similar-looking bar does not make
these the same quantity.

This is what **interval semantics** means here: what the returned numbers
represent, and which assumptions and statistical statements apply to them.
You can read one mode below without first learning the software internals.

## Read the range before the guarantee

| What you asked CE | What the range describes | Where to begin |
| --- | --- | --- |
| How probable is this class? | Probability information for a named class. | Mode 1: classification below. |
| What numerical value is predicted? | Target values, in units such as dollars or a disease-progression score. | Mode 2: interval regression below. |
| How probable is a numerical event? | Probability information for an event such as a value at most a budget. | Mode 3: probabilistic regression below. |
| What does this feature condition contribute? | A factual model-response comparison, with its own weight range. | Feature weights below. |

An **alternative** reports the prediction under another feature condition.
Its range belongs to that alternative prediction, not to a factual weight.
The {doc}`task and mode guide <tasks_modes_capabilities>` explains how to choose
the output question. The examples below illustrate quantities; they do not add
a statistical guarantee.

## How to use each mode section

Read its question and example first. Then open the detailed source-version
statements if you need the formal prerequisites, assumptions and limitations.
Read those together: a guarantee quoted without its conditions is incomplete.

Keep the distinction between a **reported point estimate** and a **reported
range**. The estimate is one number; the lower and upper values come from the
applicable construction. Neither the visual width nor the endpoints alone tells
you that an individual outcome is certain or that an assumption has been checked.

<span id="scope"></span>

## Mode 1: Classification (Venn-Abers)

**Question:** how probable is a named class for this case? The model's target is
a category, whether there are two classes (binary) or more (multiclass).

In the shared Iris example, CE reports versicolor probability about **0.910**, with
bounds **[0.902, 0.992]**. Read the species name before the numbers: the bounds
refer to that class's probability information. They are not possible flower
measurements and are not a conventional confidence interval containing the
individual flower's unknown “true probability”.

CE uses **Venn–Abers** constructions. In the binary construction, hypothetical
labels lead to a pair of probability values; a reported point probability is
derived from the construction. A property of the pair must not be transferred
unchanged to a merged point or to multiclass handling. The
{doc}`calibration page <calibration_background>` explains the mechanism.
Exact merged-probability and multiclass validity wording remains for author review.

For multiclass outputs, check the class order and the return shapes before
selecting a bound. The source version can return bounds outside [0, 1] on some
cases. Retain the raw output and the
{doc}`documented limitation <../../get-started/quickstart_classification>`;
do not clip it or assume this well-behaved example validates all cases.

<details><summary>Detailed classification statements retained from the source version</summary>

### Calibration prerequisites
- Fit on a proper training split.
- Calibrate on a held-out calibration split.

### Mode-specific guarantees
- Outputs are calibrated class probabilities with interval bounds from Venn-Abers.

### Assumptions
- Calibration and deployment samples are exchangeable or distribution-matched.

### Explicit non-guarantees
- No guarantee under distribution drift or regime shift.
- No guarantee that class probability intervals transfer unchanged across domains.

### Explanation-envelope and feature-level limits
- Rule-level and feature-level intervals are explanation artifacts tied to calibrated
  perturbation behavior.
- They are not causal guarantees.

</details>

## Mode 2: Percentile or interval regression (CPS)

**Question:** what numerical value is predicted, and what target-value interval
is reported? A **prediction interval** concerns the numerical target, in its units.

For example, the browser housing guide records **0.5170**, with interval
**[0.3087, 0.7948]** in units of $100,000. That is a point prediction of $51,700
and interval endpoints $30,870 and $79,480. These are monetary values, not
probabilities. The {doc}`housing example <../../get-started/example-interval>`
explains the captured result and its source.

CE's interval-regression path uses a **conformal predictive system (CPS)**.
Requested percentiles select endpoints of the predictive information. For example,
5th and 95th percentiles specify a *nominal* central 90% interval. This describes
the requested settings; it is not a promise of exact finite-sample coverage for
each case or every subgroup. The precise coverage statement depends on the
construction and sampling assumptions and remains an author-review topic.

A percentile request does not fix the interval's numerical width. Different
cases can receive different endpoints and widths. To run this question and read
the returned values, use the {doc}`regression guide <probabilistic_regression>`.

<details><summary>Detailed interval-regression statements retained from the source version</summary>

### Calibration prerequisites
- Fit on a proper training split.
- Calibrate with CPS on a held-out calibration split.

### Mode-specific guarantees
- Percentile intervals are CPS-based predictive intervals for requested percentiles.

### Assumptions
- Exchangeability or calibration-deployment distribution match.

### Explicit non-guarantees
- No guarantee that requested percentiles remain calibrated after drift.
- No guarantee of fixed interval width across subpopulations.

### Explanation-envelope and feature-level limits
- Feature-level interval effects describe model behavior under perturbation.
- They do not guarantee intervention outcomes in the real world.

</details>

## Mode 3: Probabilistic or thresholded regression (CPS + Venn-Abers)

**Question:** how probable is a specified event on a numerical target? The model
still predicts a number, but your question now asks about a probability.

For housing in units of $100,000, threshold **3** defines the event **Y ≤ 3**:
median housing value at most $300,000. Its probability and bounds have no dollar
unit. A probability near 1 is not a house value near $100,000, and its bounds
are not an interval of possible house prices.

The reviewed implementation uses CPS information with Venn–Abers calibration
for this event question. It is not the same output as the value-and-interval
question above. Define the event before calling CE and keep the threshold
consistent when requesting its factual and alternative explanations.

The {doc}`value-versus-event guide <probabilistic_regression>` shows the calls.
For a worked result, use the {doc}`event example <../../get-started/example-event>`.
Exact probability validity statements should be read with the source-version
conditions and the outstanding author-review qualifications.

<details><summary>Detailed event-probability statements retained from the source version</summary>

### Calibration prerequisites
- Fit regression model on a proper training split.
- Build threshold event probabilities through CPS outputs calibrated with Venn-Abers.

### Mode-specific guarantees
- Returns calibrated event probabilities for threshold queries such as `P(y <= t)`
  or interval events.

### Assumptions
- Exchangeability or deployment match to calibration distribution.

### Explicit non-guarantees
- No guarantee for threshold probability calibration under drift.
- No guarantee that threshold semantics imply causal actionability.

### Explanation-envelope and feature-level limits
- Feature-level probability shifts and envelopes describe model response patterns.
- They are not guarantees of controlled intervention effects.

</details>

## Feature weights are a different quantity

A factual explanation compares model responses under feature conditions. In the
same Iris case, a factual weight of **+0.388**, with range **[0.240, 0.433]**,
is on the explained class-probability comparison scale. It is not another 0.388
probability that the flower is versicolor.

A range crossing zero does not settle the comparison's direction. A range wholly
on one side of zero still does not establish a causal effect or a formal
per-feature coverage guarantee. The construction of a prediction range cannot
simply be reused as a theorem about every feature-weight range.

An alternative instead reports a prediction under another condition. Compare
that prediction with the original on the same scale. Read the
{doc}`explanation-construction page <how_explanations_are_built>` and
{doc}`interpretation guide <../how-to/interpret_explanations>` for the same case.

## Cross-mode non-guarantees

All three modes need a fixed fitted model, separate labelled calibration data
and the applicable sampling conditions. After changing the predictive model,
return to the calibration workflow rather than assuming the old calibration
still applies. **Exchangeability** means that reordering observations does
not change their joint probability law. Independent cases drawn from the same
distribution are an important example; the term does not merely mean that two
datasets look similar.

A changed population, time period or data-collection process can matter. A
successful calibration call does not test those conditions. An empirical check
on held-out cases is useful evidence, but does not prove a formal guarantee for
every future case. See {doc}`Checking results <../../practitioner/check_results>`.

<details><summary>Cross-mode statements retained from the source version</summary>

- Calibration guarantees are conditional on calibration assumptions.
- No unconditional guarantee under dataset shift, temporal drift, or adversarial change.
- Explanation-level intervals should not be promoted as formal per-feature coverage
  guarantees unless explicitly proven for that claim.

</details>

## Scientific wording still requiring author review

This independent candidate preserves the detailed source-version statements
above. It does not resolve the exact validity wording for merged Venn–Abers
probabilities, multiclass bounds, CPS finite-sample coverage or feature ranges.
The source's “exchangeable or distribution-matched” phrasing should not be read
as a claim that matching marginal feature distributions proves exchangeability.
For construction and papers, use {doc}`calibration_background`.

## Continue with the same result

- **Read a rule or plot:** {doc}`Interpret calibrated explanations <../how-to/interpret_explanations>`.
- **Choose a call:** {doc}`Quick API <../../get-started/quick_api>`.
- **Evaluate on your data:** {doc}`Checking results <../../practitioner/check_results>`.
- **Understand the workflow:** {doc}`How CE Works <../../sections/how-ce-works>`.

## Related standards and ADRs

<details><summary>Maintainer references behind these documentation statements</summary>

- `development/standards/STD-004-documentation-audience-standard.md` (maintainer-only docs set)
- `development/standards/STD-002-code-documentation-standard.md` (maintainer-only docs set)
- `development/adrs/ADR-021-calibrated-interval-semantics.md` (maintainer-only docs set)
- `development/adrs/ADR-012-documentation-and-gallery-build-policy.md` (maintainer-only docs set)
- `development/adrs/ADR-026-explanation-plugin-semantics.md` (maintainer-only docs set)

</details>

<span id="calibrated-interval-semantics"></span>

<!-- Entry-point tier: Tier 3. -->
