# Quickstart: understand CE and explore it in your browser

<!-- Preserve descriptive anchors from the previous review layout. -->
<span id="quickstart-create-and-read-your-first-explanation"></span>


<span id="get-started"></span><span id="quickstart"></span>

No Python or CE installation is needed for this first learning route. Start
with the big picture, choose a question, then explore one browser experience.
For a complete local example instead, use {doc}`First explanation in Python <first-python-explanation>`.

## 1. CE in 60 Seconds

A supervised model uses the features of a case to predict a target: a class or
a number. CE works with that trained model and separate labelled calibration
data to provide task-specific prediction information and explanations of the
model's response. This is a short orientation; allow more time to explore the exercises.

```{include} ../_shared/ce-workflow.md
```

CE need not retrain an already fitted model. Keep calibration data separate
from the rows used to fit it.

<details class="ce-home-details"><summary>Predictive tasks: features, targets and observations</summary>

```{include} ../foundations/concepts/predictive_tasks.md
:start-after: <!-- predictive-tasks:start -->
:end-before: <!-- predictive-tasks:end -->
```

For background, see [supervised learning](https://developers.google.com/machine-learning/intro-to-ml/supervised).
The shared {doc}`data-role page <../foundations/concepts/predictive_tasks>`
explains fitting, calibration and evaluation data.

</details>

## 2. Choose your predictive task and CE mode

There are **two predictive tasks** here, classification and regression.
Regression supports two different output questions:

```{include} ../_shared/task-mode-map.md
:start-after: <!-- task-mode-map:start -->
:end-before: <!-- task-mode-map:end -->
```

A **capability** is an operation, not another task. A factual explanation
reports conditions holding for a case with feature weights and ranges. An
alternative reports what the model would predict under a different condition.
Neither establishes a causal effect or guarantees a feasible action.

Use the {doc}`full task/mode/capability map <../foundations/concepts/tasks_modes_capabilities>`
for depth. Browser support must be checked separately from library support.

## 3. Choose your browser experience

<div class="ce-route-grid" role="navigation" aria-label="Choose a browser learning route">
<a class="ce-route-card" href="expert-hub.html"><strong>Expert Hub</strong><span>Inspect a dataset, prepare/calibrate and compare factual and alternative outputs.</span><span>Diabetes classification · Housing value and event questions</span><span>Follow the technical guide →</span></a>
<a class="ce-route-card" href="decision-lab.html"><strong>Decision Lab</strong><span>Inspect model support before making a simulated decision.</span><span>Guided Mission Control · Precision Works</span><span>Follow the decision guide →</span></a>
</div>

Choose one route; you do not need to finish both. Both apps are under active development.

## 4. Explore one explanation

**Technical route:** open [Expert Hub](https://calibrated-explanations-demo.ju.se/expert),
choose **Diabetes (Binary Classification)**, then **Next: Prepare & Calibrate →
Prepare Random Forest + Calibrate**. Wait for **Calibrated**, select **Next:
Explain**, then row **0** under **Test Set Instances**. Inspect **Factual** and
**Alternatives (n)**. Follow the {doc}`verified guide <expert-hub>` for screenshots,
regression mode controls and current interface qualifications.

**Decision route:** open the [guided Mission Control WHY exercise](https://games.grejna.ai/learn/mission/l4?from=explanations-alternatives).
Read the mission costs, **CHANCE OF SUCCESS** and **COULD BE ANYWHERE IN**.
Inspect **WHY?** before choosing **GO** or **STOP**, then reflect on feedback.
The {doc}`Decision Lab guide <decision-lab>` covers the verified exercise and
numeric/event options. Its level-4 exercise does not expose every capability.

If an application is unavailable, the guides retain dated real captures to
inspect. For an executable alternative, use the optional Python route below.

## 5. Understand what you see

Start with one result rather than every setting. In the Diabetes browser example,
the output is a probability for the positive class. In California Housing,
first decide whether you asked for a housing value or for the probability of
an event on that value. That choice determines the scale you should read.


Read **the output quantity → its units → its range → a feature condition →
a weight or alternative prediction**. These are different quantities.

A captured Expert Hub Diabetes case reported probability 0.7448 and bounds
[0.7273, 0.7959]. Its `plas < 147.50` alternative reported
0.2719 [0.2487, 0.2811]. Those values came from the browser trial; they are not
the expected output of a different Python case or a clinical recommendation.

For a numeric prediction, read the interval in target units. For a threshold
event, identify the event first and read its probability bounds on a probability
scale. A feature-weight range does not inherit a universal per-feature coverage
guarantee. Use the shared {doc}`interpretation guide <../foundations/how-to/interpret_explanations>`
and {doc}`canonical semantics <../foundations/concepts/calibrated_interval_semantics>`
for detail. One game outcome or tutorial case does not validate a deployment.

**Pause and check:** can you name the predicted quantity, its units and one
feature condition? Can you distinguish that condition's weight from an
alternative prediction? If not, keep the result open and use the
{doc}`interpretation guide <../foundations/how-to/interpret_explanations>`.
For the calculation behind a weight, continue to
{doc}`How explanations are built <../foundations/concepts/how_explanations_are_built>`;
for what a range does and does not establish, use the canonical semantics linked
above. These are deeper explanations of the same result, not new exercises.

## 6. Continue learning

| Your next question | Continue with |
| --- | --- |
| Why use CE? | {doc}`CE: What & Why <../sections/what-and-why>`. |
| How are calibration and explanations constructed? | {doc}`How CE Works <../sections/how-ce-works>`. |
| Can I run a complete example? | {doc}`First explanation in Python <first-python-explanation>`. |
| How do I install the library? | {doc}`Installation <installation>`; optional for the browser route. |
| What about another task? | {doc}`Classification <quickstart_classification>` or {doc}`regression and event probabilities <quickstart_regression>`. |
| How do I assess my own results? | {doc}`Practitioner Hub <../practitioner/index>` and {doc}`check results <../practitioner/check_results>`. |
| Where are exact calls and settings? | {doc}`Quick API <quick_api>` and {doc}`Software & Integration <../sections/software-integration>`. |

The earlier local workflow is retained in full at {doc}`first-python-explanation`,
including its code, output, plot and multiclass limitation. No installation is
required until you choose that route.

Entry-point tier: Tier 1.

```{toctree}
:hidden:
:maxdepth: 1

Expert Hub: technical exploration <expert-hub>
Decision Lab: learn through decisions <decision-lab>
First explanation in Python <first-python-explanation>
Choose your task <../getting_started_60s>
```

<!-- Legacy headings bridge to the retained Python tutorial. -->
<span id="what-ce-adds"></span>
<span id="predictive-tasks"></span>
<span id="install"></span>
<span id="keep-the-data-roles-separate"></span>
<span id="run-the-complete-example"></span>
<span id="read-the-plot"></span>
<span id="if-the-result-differs-or-no-plot-appears"></span>
<span id="choose-your-next-step"></span>
