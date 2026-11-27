# How CE Works

<span class="ce-choice-page" hidden></span>

<!-- Preserve descriptive anchors from the previous review layout. -->
<span id="choose-an-output-to-understand"></span>
<span id="follow-the-workflow"></span>


How does CE turn a trained model and calibration data into prediction information
and an explanation? This route moves from the workflow to mechanisms and their
statistical conditions. You can stop at the depth needed for your question.

## Start here

**Your reading route:** this overview →
{doc}`calibration background <../foundations/concepts/calibration_background>` →
{doc}`explanation construction <../foundations/concepts/how_explanations_are_built>` →
{doc}`reading a result <../foundations/how-to/interpret_explanations>`.


If features, targets or separate data roles are new, first read
{doc}`Predictive tasks and data roles <../foundations/concepts/predictive_tasks>`.
Otherwise, begin with the workflow below. You will learn what CE constructs,
read code and output from one Iris session, and distinguish the quantities it reports.

## Follow the same model through the workflow

Start with a fitted predictive model. Calibration uses separate labelled cases
to construct prediction information for your question; explanations compare
responses under feature conditions. The model itself stays fixed.

```{include} ../_shared/intro-figure.md
```

Training data fit the model; calibration data have a separate role. A test case
has a known target kept aside for evaluation. A new case's target may be unknown.
Both supply only features to prediction and explanation calls. For a guided
introduction to those roles, use {doc}`Predictive tasks <../foundations/concepts/predictive_tasks>`.
For the corresponding software calls, use the
{ref}`numbered wrapper workflow <ce-wrapper-workflow-map>`.

## Follow the workflow for your question

The same structure produces different quantities in the three modes. Each
example below starts with a mode-specific figure, then offers browser and local
Python routes. Read the figure together with its assumptions note.

- {doc}`Classification: class-probability information <../get-started/example-classification>`.
- {doc}`Interval regression: value and target-value interval <../get-started/example-interval>`.
- {doc}`Probabilistic regression: event probability and bounds <../get-started/example-event>`.

## Use optional features when you have a specific need

After reading an ordinary result, visit the shared
{doc}`optional-capability overview <../foundations/concepts/optional_capabilities>`.
It places grouping, guarding, conjunctions, alternative filtering and rejection
within the core workflow, with the same terms used by the software guides.
You do not need to enable them to follow the core pages below.

## From calibration to a prediction

The fitted model supplies responses for new features. CE uses separate labelled
calibration examples to construct prediction information for the chosen question.
Classification uses Venn–Abers constructions. Numerical interval regression uses
a conformal predictive system (CPS); threshold-event probabilities use CPS scores
with Venn–Abers calibration. These methods do not make every returned range mean
the same thing.

Begin with the {doc}`calibration background <../foundations/concepts/calibration_background>`
for intuition and statistical definitions. Then read the applicable mode in the
{doc}`semantics reference <../foundations/concepts/calibrated_interval_semantics>`
for the source version's conditions and limits. The model must be fixed before
calibration; query targets are not inputs to prediction or explanation.

## From a prediction to an explanation

A factual explanation compares the calibrated response with responses obtained
under feature conditions. In a simple difference, the original response minus a
comparison response gives a weight. Its units depend on the explained quantity:
probability differences for a class or event, target-unit differences for numerical
regression. Exact construction and aggregation matter; this is not a universal
formula for every explanation type.

An alternative instead reports the model's prediction under another condition.
It is not the same quantity as a factual weight. Follow the
{doc}`worked explanation construction <../foundations/concepts/how_explanations_are_built>`
and then {doc}`read the resulting rules and plot <../foundations/how-to/interpret_explanations>`.
Neither type establishes the causal effect of changing the real-world case.

## What the method's assumptions do

Calibration depends on the data and method's sampling conditions. A successful
call does not check that future cases satisfy them, and one correct result does
not establish calibration or coverage. Use the mode-specific semantics to
separate the output definition from its guarantee, and
{doc}`Checking results <../practitioner/check_results>` to plan held-out evaluation.
That is the bridge from understanding the construction to applying it.

## Continue through the shared concept pages

**Next:** {doc}`Calibration and statistical background <../foundations/concepts/calibration_background>`.
Then follow its next-page link to explanation construction and interpretation.

If you want the whole sequence before starting, use the
{ref}`shared reading map <guided-reading-route>`. If you already have a result,
you can enter directly at {doc}`interpretation <../foundations/how-to/interpret_explanations>`.

For numerical targets, continue to
{doc}`Regression: values and events <../foundations/concepts/probabilistic_regression>`.
Use {doc}`Range meanings and assumptions <../foundations/concepts/calibrated_interval_semantics>`
for the precise conditions behind a reported range. These are shared references,
not a second course to repeat after Quick Start.

## Keep the quantities separate

Class-probability bounds concern a probability. A numeric prediction interval
concerns target values in their units. A threshold-event probability concerns a
defined event on that target. Feature-weight ranges concern model-response
comparisons. A similar-looking bar does not make them interchangeable.

The {doc}`regression-mode guide <../foundations/concepts/probabilistic_regression>`
shows how the same model can answer value and event questions. The
{doc}`explanation-construction page <../foundations/concepts/how_explanations_are_built>`
separates baseline predictions, factual weights and alternative predictions.

## Go deeper without restarting

Use {doc}`shared foundations <../foundations/index>` as a topic collection,
and {doc}`theory and literature <../researcher/advanced/theory_and_literature>`
for papers. Statistical claims need their method, assumptions and version;
this introduction does not strengthen the canonical guarantees or resolve
open author-review issues.

**See it happen:** {doc}`browser Quickstart <../get-started/index>`.
**Run a task:** {doc}`CE in Practice <in-practice>`.
**Integrate an implementation:** {doc}`Software & Integration <software-integration>`.

```{toctree}
:maxdepth: 1
:hidden:

Tasks, modes and capabilities <../foundations/concepts/tasks_modes_capabilities>
Calibration and statistical background <../foundations/concepts/calibration_background>
How explanations are built <../foundations/concepts/how_explanations_are_built>
Read CE explanations <../foundations/how-to/interpret_explanations>
Regression: values and events <../foundations/concepts/probabilistic_regression>
Range meanings and assumptions <../foundations/concepts/calibrated_interval_semantics>
More shared topics <../foundations/index>
```

<!-- Entry-point tier: Tier 1. -->

<span id="read-the-workflow-at-three-depths"></span>
<span id="choose-what-to-understand-next"></span>

<!-- Preserve section links from earlier review versions. -->
<span id="read-this-path-as-a-tutorial"></span>
<span id="find-the-explanation-you-need"></span>
<span id="continue-through-the-shared-chapters"></span>
