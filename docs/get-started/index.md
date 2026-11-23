# CE big picture in 60 seconds

**Calibrated Explanations (CE) helps you inspect an individual prediction.** It
uses a {term}`fitted model <Fitted model>` and separate labelled
{term}`calibration data <Calibration data>` to provide calibrated prediction
information and feature explanations with reported ranges.

## From a conventional prediction to CE

<figure>
<picture>
<source media="(max-width: 600px)" srcset="../_static/figures/ce-big-picture-mobile.svg">
<img src="../_static/figures/ce-big-picture.svg" width="1100" height="680" alt="White boxes show training data, the fitted model and a new case leading to a conventional prediction. Orange boxes add separate labelled calibration data and CE using the same fitted model and new-case features. Four output boxes distinguish prediction, its task-specific range, factual conditions with weights and ranges, and alternative conditions with predictions and ranges.">
</picture>
<figcaption>CE uses the same fitted model. The orange outputs distinguish quantities; they are not four required API calls.</figcaption>
</figure>

[Open the full-size figure](../_static/figures/ce-big-picture.svg).

**Conventional prediction:** a trained model uses a new case's
{term}`features <Feature>` to return a class, value or score.

**With CE:** keep that same model, add separate calibration data, then inspect
prediction information with task-specific ranges and factual or alternative
explanations. Calibration does not retrain the predictive model. Other ML
workflows can also include calibration and uncertainty methods.

**Go deeper:** {doc}`follow the complete CE workflow <../sections/how-ce-works>`.

## Tasks and modes: what question are you asking?

CE supports {term}`supervised learning <Supervised learning>`: models learn from
features and known {term}`targets <Target>`. A {term}`task <Predictive task>`
describes the target: **classification** predicts categories (two classes for
binary, three or more for multiclass); **regression** predicts a number.

A {term}`CE mode <CE mode>` describes the output question:

- **Class probability:** which class, and how probable? {doc}`See classification <example-classification>`.
- **Value and interval:** what numerical value and target-value interval? {doc}`See interval regression <example-interval>`.
- **Event probability:** how probable is an event such as a value at most a budget? {doc}`See probabilistic regression <example-event>`.

**Go deeper:** {doc}`tasks, modes and capabilities <../foundations/concepts/tasks_modes_capabilities>`.

## Capabilities: what can CE show you?

- **Calibrated prediction information:** the quantity for your question, with its reported range.
- **Factual explanations:** conditions holding for the case, with comparison weights and their ranges.
- **Alternative explanations:** predictions and ranges under different feature conditions.

These are model-response explanations, not causal interventions. Range meanings
and guarantees depend on the quantity, method and assumptions.

**Go deeper:** {doc}`how explanations are built <../foundations/concepts/how_explanations_are_built>`
and {doc}`what CE ranges mean <../foundations/concepts/calibrated_interval_semantics>`.

## Choose how to try CE

<div class="ce-route-grid" role="navigation" aria-label="Try CE in a browser or locally">
<a class="ce-route-card" href="expert-hub.html"><strong>Try CE in your browser</strong><span>Use built-in examples without installing Python. Prepare, calibrate and inspect one result.</span><span>Open the browser guide →</span></a>
<a class="ce-route-card" href="first-python-explanation.html"><strong>Install and run locally</strong><span>Install CE, run the Iris example and interpret its output and plot.</span><span>Open the Python guide →</span></a>
</div>

For local numerical targets, follow the {doc}`regression tutorial <quickstart_regression>`.
For package and environment options, use {doc}`installation <installation>`.
You can also {ref}`read one Iris result without running code <classification-one-case>`.

## Continue learning

- **Why was CE developed?** {doc}`CE: What & Why <../sections/what-and-why>`.
- **How do I read my result?** {doc}`Interpret explanations <../foundations/how-to/interpret_explanations>`.
- **How do I use my own data?** {doc}`CE in Practice <../sections/in-practice>`.
- **How do I integrate the library?** {doc}`Software & Integration <../sections/software-integration>`.

<!-- Entry-point tier: Tier 1. -->

```{toctree}
:hidden:
:maxdepth: 1

Classification example <example-classification>
Interval regression example <example-interval>
Event-probability example <example-event>
First explanation in Python <first-python-explanation>
Browser workflow: Expert Hub <expert-hub>
Decision practice: Decision Lab <decision-lab>
```

<!-- Preserve previous section links. -->
<span id="1-ce-in-60-seconds"></span>
<span id="2-choose-your-predictive-task-and-ce-mode"></span>
<span id="3-choose-your-browser-experience"></span>
<span id="4-explore-one-explanation"></span>
<span id="5-understand-what-you-see"></span>
<span id="6-continue-learning"></span>
<span id="choose-one-step-by-step-example"></span>
<span id="choose-your-next-step"></span>
<span id="get-started"></span>
<span id="if-the-result-differs-or-no-plot-appears"></span>
<span id="install"></span>
<span id="keep-the-data-roles-separate"></span>
<span id="predictive-tasks"></span>
<span id="quickstart"></span>
<span id="quickstart-create-and-read-your-first-explanation"></span>
<span id="read-the-plot"></span>
<span id="run-the-complete-example"></span>
<span id="task-mode-and-capability-three-different-choices"></span>
<span id="what-can-you-rely-on"></span>
<span id="what-ce-adds"></span>
<span id="what-ce-adds-to-the-workflow"></span>



<!-- Preserve headings from the preceding review candidate. -->
<span id="quick-start-the-ce-big-picture"></span>
<span id="what-changes-when-you-add-ce"></span>
<span id="choose-the-question-you-want-to-answer"></span>
<span id="what-can-an-explanation-tell-you"></span>
<span id="what-do-the-ranges-mean"></span>
<span id="after-your-first-result"></span>
<span id="go-deeper-when-you-need-it"></span>
