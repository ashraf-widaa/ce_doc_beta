# Calibrated interval semantics

This page is the semantics source for user-facing documentation. Start by naming
the quantity that has a range, then read the corresponding mode below. Similar
looking endpoints do not imply the same statistical statement.

## Read the range before the guarantee

- **Class probability:** classification reports probability information for a
  class. Its bounds are not target-value prediction intervals or conventional
  confidence intervals for an individual's unknown probability.
- **Numerical target:** interval regression reports a prediction interval in the
  target's units. Coverage concerns the specified method and sampling conditions;
  it is not certainty about the particular case you are viewing.
- **Event probability:** probabilistic regression asks about an event such as
  `Y <= t`. Its probability bounds are not a range of possible target values.
- **Feature weight:** an explanation range concerns a model-response comparison.
  It does not automatically inherit a prediction-coverage guarantee.

The sections below retain the source version's mode-specific statements.
Exact validity wording for merged probabilities, multiclass bounds and finite-sample
coverage remains a scientific-author review topic; this reading guide does not
resolve it or strengthen those statements.

For a concrete example, use the {doc}`Quick Start <../../get-started/index>`.
For general background before the conditions, read
{doc}`Calibration and statistical background <calibration_background>`.

## How to use each mode section

First check the calibration prerequisites. Then read its guarantee together with
the assumptions and non-guarantees, rather than quoting the guarantee alone.
Finally check the feature-level limits before describing an explanation range.
Successful API calls or one correct prediction do not verify these assumptions.

## Scope

Calibrated Explanations has three distinct semantics modes:

1. Classification with Venn-Abers probability intervals.
2. Percentile/interval regression without thresholds using CPS percentile intervals.
3. Probabilistic or thresholded regression using CPS with Venn-Abers event probabilities.

Do not merge these into one guarantee statement.

## Mode 1: Classification (Venn-Abers)

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

## Mode 2: Percentile or interval regression (CPS)

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

## Mode 3: Probabilistic or thresholded regression (CPS + Venn-Abers)

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

## Cross-mode non-guarantees

- Calibration guarantees are conditional on calibration assumptions.
- No unconditional guarantee under dataset shift, temporal drift, or adversarial change.
- Explanation-level intervals should not be promoted as formal per-feature coverage
  guarantees unless explicitly proven for that claim.

## Continue with the same result

Use {doc}`Interpret calibrated explanations <../how-to/interpret_explanations>`
to read a particular rule or plot, {doc}`Quick API <../../get-started/quick_api>`
to find a call, or {doc}`Checking results <../../practitioner/check_results>` to
plan held-out evaluation. The {doc}`How CE Works route <../../sections/how-ce-works>`
connects construction and calibration without requiring the software internals.

## Related standards and ADRs

- `development/standards/STD-004-documentation-audience-standard.md` (maintainer-only docs set)
- `development/standards/STD-002-code-documentation-standard.md` (maintainer-only docs set)
- `development/adrs/ADR-021-calibrated-interval-semantics.md` (maintainer-only docs set)
- `development/adrs/ADR-012-documentation-and-gallery-build-policy.md` (maintainer-only docs set)
- `development/adrs/ADR-026-explanation-plugin-semantics.md` (maintainer-only docs set)

Entry-point tier: Tier 3.
