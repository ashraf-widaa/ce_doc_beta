# How CE Works

<span class="ce-choice-page" hidden></span>

<!-- Preserve descriptive anchors from the previous review layout. -->
<span id="choose-an-output-to-understand"></span>
<span id="follow-the-workflow"></span>


How does CE turn a trained model and calibration data into prediction information
and an explanation? This route moves from the workflow to mechanisms and their
statistical conditions. You can stop at the depth needed for your question.

## Start here

If features, targets or separate data roles are new, first read
{doc}`Predictive tasks and data roles <../foundations/concepts/predictive_tasks>`.
Otherwise, begin with the workflow below. You will learn what CE constructs,
read code and output from one Iris session, and distinguish the quantities it reports.

## Follow the same model through the workflow

Follow the same fitted predictive model through calibration, prediction and
explanation. One public wrapper coordinates the software calls; it does not
introduce a second predictive model. Keep the data roles separate.

```{include} ../_shared/wrapper-figure.md
```

```{include} ../_shared/wrapper-lifecycle.md
```

The method construction comes next; the diagram is not a claim that every range
has the same guarantee or that a separate prediction call must precede an
explanation. Read a held-out test observation using its features first, then
use its known target only for evaluation.

For the inputs to these stages, read the shared
{doc}`data-role definitions <../foundations/concepts/predictive_tasks>`.
For the calls, use {doc}`Quick API <../get-started/quick_api>`. A completed workflow
alone does not verify the statistical assumptions: guarantees remain mode-specific
as described in the {doc}`semantics reference <../foundations/concepts/calibrated_interval_semantics>`.

## Follow the workflow for your question

The same structure produces different quantities in the three modes. Each
example below starts with a mode-specific figure, then offers browser and local
Python routes. Read the figure together with its assumptions note.

- {doc}`Classification: class-probability information <../get-started/example-classification>`.
- {doc}`Interval regression: value and target-value interval <../get-started/example-interval>`.
- {doc}`Probabilistic regression: event probability and bounds <../get-started/example-event>`.

## Place optional features by their job

Once the core workflow is familiar, attach each option to the activity it changes.
The arrows below identify that relationship; they do not make the options a
sequence that every application must run.

```{include} ../_shared/optional-figure.md
```

The concept and software names match the shared glossary and the
{ref}`Quick API option map <optional-capability-api-map>`. The numbers refer to
the wrapper workflow above. Read the appropriate detailed guide before enabling
an option; grouping is not a fairness guarantee, and guarding is not a universal
certificate that a case or hypothetical change is realistic.

- **Mondrian calibration:** supply consistent group information at calibration
  and query time; see {doc}`conditional calibration <../foundations/how-to/conditional_calibration>`.
- **Guarding:** check selected representatives of candidate conditions while
  building explanations; see {doc}`guarded explanations <../foundations/concepts/guarded_explanations>`.
- **Conjunctions:** combine feature conditions in rules; see
  {doc}`interpreting explanations <../foundations/how-to/interpret_explanations>`.
- **Alternative filtering:** select already generated alternative rules by a
  stated criterion; see {doc}`alternatives <../foundations/concepts/alternatives>`.
- **Rejection:** flag cases for separate handling under the configured rule;
  follow the {doc}`rejection guide <../practitioner/advanced/reject-policy>`. Setup and support must be checked before use.

These operations do not establish real-world causal effects or a universal
prediction guarantee. The shared {doc}`task and mode guide <../foundations/concepts/tasks_modes_capabilities>`
keeps the output quantities distinct.

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

## Continue through the shared chapters

Read these in order for a method tutorial, or enter at the question you have now:

1. {doc}`Tasks, modes and capabilities <../foundations/concepts/tasks_modes_capabilities>` — choose the prediction question before the operation.
2. {doc}`Calibration and statistical background <../foundations/concepts/calibration_background>` — understand the methods, then run calibration.
3. {doc}`How explanations are built <../foundations/concepts/how_explanations_are_built>` — connect comparisons to weights and alternatives.
4. {doc}`Interpret explanations <../foundations/how-to/interpret_explanations>` — read the same case's rules and plot.

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
