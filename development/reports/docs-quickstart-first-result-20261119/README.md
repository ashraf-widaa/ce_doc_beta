# First-result Quickstart review

Baseline: navigation candidate `1147062f0d38a0118bf0ec4d20891413461c5c3c`.
Branch: `docs/quickstart-first-result-20261119`.
Independent review project only: ashraf-widaa/ce_doc_beta / RTD ce-doc-beta.

## Educational changes and shared sources

- Quickstart opens with the shared conventional-prediction versus CE workflow
  illustration. It reflows as text, rather than shrinking diagram labels on phones.
  The same fragment is included in How CE Works.
- The user's two-paragraph predictive-task introduction defines features, target,
  observation, supervised learning, classification and regression. Its authoritative
  home is the new `foundations/concepts/predictive_tasks` page; Quickstart includes
  that exact text and the shared data-role table. Background links sit beside the
  concepts they support, without tracking parameters.
- Retains the official classification example's Iris dataset, RandomForest,
  random seeds and 90/30/30 split. It makes a complete first result from evaluation
  row 1, with public fit/calibrate/predict/explain calls, checked output, a real
  factual plot and interpretation immediately afterward.
- The downloadable `_examples/first_explanation.py` is the single executable
  source. The classification tutorial includes its common preparation and
  fit/calibrate lines; existing broader classification/alternative calls remain.
- Prediction quantities, feature conditions, weight signs and weight ranges are
  distinguished. The plot maps class 1 to versicolor and the complement to the
  other species. Full-size image and script downloads are accessible.
- Seven sidebar roots remain; the new shared foundation has one tree parent.
  No new Diabetes classification or California Housing example was introduced.

## Verification

- Strict Sphinx HTML build passed, no warnings.
- Documentation and documentation-example smoke suite: 62 passed, one wheel-install
  test excluded. The new test executes the actual script, checks its expected
  output, fitted/calibrated state, data roles, probability shape/class mapping,
  and produces a nonempty plot using the real CE renderer.
- Internal-link scan: 139 HTML pages, zero broken links.
- Browser checks: 32 page/width/theme combinations across 320, 390, 768, 1440,
  light/dark. Checks one article heading, absence of page overflow, diagram
  reflow, expected output, image loading, full-size plot and script download.
- Ruff lint of modified Python files and git diff --check passed.
- Generated plot inspected. The environment lacks Arial; Matplotlib reports
  font fallback diagnostics. No warnings were suppressed in the example.
- Library source and canonical interval-semantics page unchanged.

Environment: source CE 1.0.2; numpy 2.5.5, scikit-learn 1.9.1, matplotlib 3.11.2,
venn-abers 1.5.4, crepes 0.9.1. Local installed package metadata belongs to an
older development environment; Sphinx release/version/title overrides explicitly
label this source as 1.0.2, as in previous candidates. Outputs are verified here,
not a claim of identical output across dependency versions or a timed novice study.

## Scientific issue requiring maintainer review

The unchanged 1.0.2 source returns a multiclass upper bound above 1 for the first
Iris evaluation row in the official split. Reproduction after fitting/calibrating:

```python
probabilities, (low, high) = explainer.predict_proba(x_test[:1], uq_interval=True)
```

Observed first-class estimate: 0.7264150943; lower: -0.0; upper: 1.4528301887.
No clipping or library fix was applied. This is explicitly flagged in both
Quickstart and the classification tutorial. Quickstart explains the second row,
whose class-1 estimate is 0.9097744361 and bounds [0.9022556391, 0.9924812030].
That selected example does not establish that other multiclass outputs are
conventional bounded probability intervals. Authors should resolve the output
semantics and implementation behavior before stronger claims are made.

Review also: factual-weight comparison wording, distinction between prediction
and weight ranges, Venn-Abers bound semantics and the interpretation of the
complement shown by the multiclass plot. Existing source guarantee wording is
not strengthened by this tutorial. No causal or universal per-feature coverage
claims were added.

## Preview and next package

Local evidence and HTML: `/workspace/work/ce-quickstart-evidence-20261119`.
Serve `html` on port 8776 locally or forward that cloud port.

Next: author review of the flagged multiclass issue, then improve regression's
first-result story while keeping numeric prediction intervals and threshold-event
probabilities separate. Dataset migration is a distinct decision with verified
sources and target definitions.

Publish to a new named RTD version only; preserve earlier review versions,
latest/default and all official CE resources. No credentials are included.
