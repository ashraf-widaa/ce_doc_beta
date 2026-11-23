# Glossary

<span class="ce-glossary-page" hidden></span>

Look up a term, then follow **Learn more** for its explanation, example or API.
The glossary gives one shared definition per concept; it does not replace
{doc}`the method-specific assumptions and guarantees <../foundations/concepts/calibrated_interval_semantics>`.

- {ref}`Scientific & theoretical <scientific-and-theoretical>`: data, learning tasks, calibration, explanations and ranges.
- {ref}`Software & technical <software-and-technical>`: objects, calls, parameters and output formats.

Entries are alphabetical within each category. Use your browser’s find command
or documentation search to locate a word. Alternative names share an entry;
related concepts such as local and global explanations have separate definitions.

<span id="prediction-and-data"></span>
<span id="tasks-modes-and-statistical-quantities"></span>
<span id="explanations-and-ranges"></span>

(scientific-and-theoretical)=
## Scientific & theoretical

```{glossary}
:sorted:

Alternative explanation
    Prediction information under a different feature condition. Compare it with the original prediction on the same scale; it is not a causal intervention.

    Learn more: {doc}`Understand alternatives <../foundations/concepts/alternatives>`.

Baseline prediction
    The prediction information for the original case, used as the reference when reading factual comparisons and alternatives.

    Learn more: {doc}`Follow a prediction into an explanation <../foundations/concepts/how_explanations_are_built>`.

Binary classification
    Classification with two target categories. A numeric code such as 0 or 1 names a category; it does not turn the task into regression.

    Learn more: {doc}`Distinguish tasks and modes <../foundations/concepts/tasks_modes_capabilities>`.

Black-box model
    A model whose input-to-output behavior is difficult to inspect directly. An explanation helps inspect that behavior without establishing real-world causes.

    Learn more: {doc}`Why explanations are useful <../sections/what-and-why>`.

Brier score
    For a binary outcome, the mean squared difference between the reported probability and the observed 0-or-1 outcome. Lower is better; one score on one test split does not prove calibration validity.

    Learn more: {doc}`Choose held-out checks <../practitioner/check_results>`.

Calibrated Explanations
CE
    The open-source Python library documented here. It combines a fitted predictive model with separate labelled calibration data to provide prediction information and feature explanations with reported ranges.

    Learn more: {doc}`See the CE big picture <../get-started/index>`.

Calibration
    The procedure that uses a fitted model and separate labelled examples to construct prediction information. In this workflow it does not retrain the predictive model. The construction depends on the task and output question.

    Learn more: {doc}`Learn how CE calibrates <../foundations/concepts/calibration_background>`.

Calibration data
Calibration set
Calibration split
    Labelled cases used by the calibration procedure, kept separate from the cases used to fit the predictive model and from held-out evaluation data.

    Learn more: {doc}`Keep data roles separate <../foundations/concepts/predictive_tasks>`.

Capability
    An operation CE offers, such as calibrated prediction, factual explanation or alternative exploration. Choosing an explanation capability does not change the target the model learned.

    Learn more: {doc}`Separate task, mode and capability <../foundations/concepts/tasks_modes_capabilities>`.

CE mode
    The output question in these guides: class-probability information, a numerical value with an interval, or the probability of an event on a numerical target.

    Learn more: {doc}`Choose an output question <../foundations/concepts/tasks_modes_capabilities>`.

Classification
    A predictive task with a categorical target, such as flower species. Binary classification has two categories; multiclass classification has three or more.

    Learn more: {doc}`Learn predictive-task vocabulary <../foundations/concepts/predictive_tasks>`.

Conformal predictive system
CPS
    A conformal construction used for numerical predictive information. CE uses CPS percentile outputs for target-value intervals and CPS information with Venn–Abers calibration for event probabilities.

    Learn more: {doc}`Understand CPS and residuals <../foundations/concepts/calibration_background>`.

Conjunctive rule
Conjunction
    A rule combining more than one feature condition. Combining conditions does not establish that a real-world change is feasible or causal.

    Learn more: {doc}`Read conjunctions and alternatives <../foundations/concepts/alternatives>`.

Distribution shift
Drift
    A change between the calibration population or collection process and the cases where CE is used, for example over time or across regions. The method assumptions must be revisited; successful calls alone do not establish validity.

    Learn more: {doc}`Check assumptions and limits <../foundations/concepts/calibrated_interval_semantics>`.

Ensured explanation
    An alternative retained by the ensured filter because its reported interval is no wider than the baseline interval. The filter name does not guarantee a beneficial intervention or improved predictive error.

    Learn more: {doc}`Understand the width-based filter <../foundations/concepts/alternatives>`.

Evaluation data
Test set
    Held-out labelled cases used to check the resulting system after fitting and calibration. They have a different role from calibration data.

    Learn more: {doc}`Understand the data split <../foundations/concepts/predictive_tasks>`.

Exchangeability
    A sampling property: reordering observations leaves their joint probability law unchanged. Independent draws from the same distribution are an example; similar-looking feature distributions alone do not establish it.

    Learn more: {doc}`Read the method assumptions <../foundations/concepts/calibrated_interval_semantics>`.

Explanation envelope
    Reported uncertainty information attached to an explanation quantity, such as a feature weight. Its meaning comes from that quantity and construction; the label does not supply a new statistical guarantee.

    Learn more: {doc}`Identify which range you are reading <../foundations/concepts/calibrated_interval_semantics>`.

Factual explanation
    An explanation of the original case using conditions that hold for it, with model-response comparison weights and their reported ranges.

    Learn more: {doc}`Understand factual comparisons <../foundations/concepts/how_explanations_are_built>`.

Feature
Input feature
    An input describing a case, such as a flower measurement or an area’s median income. The target is what the model predicts from those inputs.

    Learn more: {doc}`Understand features and targets <../foundations/concepts/predictive_tasks>`.

Feature attribution
    A value used to summarize a feature’s contribution to a model response. Methods use different comparisons; CE weights are not automatically Shapley values or an additive decomposition.

    Learn more: {doc}`Understand CE weights <../foundations/concepts/how_explanations_are_built>`.

Feature importance
    A method-dependent summary of a feature’s role in predictions, often across cases. Check whether it is local or global and how it is computed; it is not automatically the same quantity as a CE weight.

    Learn more: {doc}`Distinguish model comparisons <../foundations/concepts/how_explanations_are_built>`.

Feature weight
    A comparison of calibrated model responses associated with a factual condition. Identify the explained class, numerical target or event before interpreting the sign, units and weight range.

    Learn more: {doc}`Read a weight and its range <../foundations/how-to/interpret_explanations>`.

Fitted model
Trained model
    A predictive model whose parameters have been learned from model-fitting data. CE’s calibration step uses that model rather than retraining it.

    Learn more: {doc}`Follow fitting and calibration <../foundations/concepts/predictive_tasks>`.

Global explanation
    An explanation or summary of model behavior across cases or the model as a whole. This differs from a local explanation of one case.

    Learn more: {doc}`Place CE within explainability <../sections/what-and-why>`.

Guarded explanation
    An explanation that filters candidate conditions using support checks on representative inputs. It does not certify every point in an interval or automatically test whether the original query is out of distribution.

    Learn more: {doc}`Understand guarded filtering <../foundations/concepts/guarded_explanations>`.

Interval regression
Percentile regression
    A numerical-target question returning a value and a CPS percentile interval in the target’s units. Requested percentiles select endpoints; they do not fix the interval’s numerical width.

    Learn more: {doc}`Compare value and event questions <../foundations/concepts/probabilistic_regression>`.

Labelled data
    Examples for which both the input features and target outcomes are known. CE’s calibration data needs those known outcomes.

    Learn more: {doc}`Understand supervised data <../foundations/concepts/predictive_tasks>`.

Local explanation
    An explanation of an individual prediction. CE’s factual and alternative explanations inspect a case rather than establish one explanation of the whole model.

    Learn more: {doc}`Understand the purpose of local explanations <../sections/what-and-why>`.

Multiclass classification
    Classification with three or more target categories, such as the three Iris species. Its class ordering and bounds need the documented version-specific qualifications.

    Learn more: {doc}`Read binary and multiclass outputs <../get-started/example-classification>`.

Observation
Case
Instance
    One example described by input features. A known target accompanies labelled data; an unknown query target is not supplied to a prediction or explanation call.

    Learn more: {doc}`Distinguish cases, features and targets <../foundations/concepts/predictive_tasks>`.

Prediction
    The model’s reported estimate for a case, such as a class, numerical value or probability. A prediction is distinct from the observed outcome.

    Learn more: {doc}`Follow the prediction workflow <../get-started/index>`.

Prediction interval
    A range of numerical target values, in the target’s units. Its coverage interpretation depends on the construction and sampling assumptions, not certainty for the individual case.

    Learn more: {doc}`Read target-value intervals <../foundations/concepts/calibrated_interval_semantics>`.

Predictive task
Task
    What kind of target the model is trained to predict. These guides cover classification for categories and regression for numerical quantities.

    Learn more: {doc}`Choose a task and mode <../foundations/concepts/tasks_modes_capabilities>`.

Probability
    A number on the 0-to-1 scale describing an event’s likelihood. Name the class or event before interpreting the number; a model report is not certainty about an individual outcome.

    Learn more: {doc}`Understand probabilities and calibration <../foundations/concepts/calibration_background>`.

Probability bounds
    Reported lower and upper information associated with a class or event probability. They are not target-value endpoints or a conventional confidence interval for an individual’s unknown true probability; multiclass handling needs separate qualifications.

    Learn more: {doc}`Read probability bounds <../foundations/concepts/calibrated_interval_semantics>`.

Probability calibration
    The relationship between probability reports and outcome frequencies. Calibration and classification accuracy answer different questions.

    Learn more: {doc}`Distinguish accuracy from calibration <../foundations/concepts/calibration_background>`.

Probabilistic regression
Thresholded regression
    A probability question about an event on a numerical target, such as a value at most a threshold. The result is probability information, not a target-value interval.

    Learn more: {doc}`Choose an event question <../foundations/concepts/probabilistic_regression>`.

Proper training data
Proper training set
Model-fitting data
    The labelled subset used to fit the predictive model, kept separate from calibration and evaluation data.

    Learn more: {doc}`Use the three data roles <../foundations/concepts/predictive_tasks>`.

Quantile
Percentile
    A quantile identifies a target value at a specified cumulative probability. Percentiles express the level out of 100: the 5th and 95th percentiles identify two endpoints, not a fixed numerical width.

    Learn more: {doc}`Understand quantiles and CPS <../foundations/concepts/calibration_background>`.

Regression
    A predictive task with a numerical target, such as median housing value or a disease-progression score. CE can answer value-and-interval or event-probability questions about that target.

    Learn more: {doc}`Read the two regression modes <../foundations/concepts/probabilistic_regression>`.

Reliability diagram
Reliability table
    A plotted or tabulated comparison of average reported probabilities with observed outcome frequencies within groups of held-out cases. Small groups have sampling variation; the display is an empirical check.

    Learn more: {doc}`Evaluate probability reports <../practitioner/check_results>`.

Reported range
Uncertainty interval
    A general label for lower and upper information. First identify whether it concerns a probability, a target value, a feature weight or an alternative prediction; the same visual shape does not give all ranges the same guarantee.

    Learn more: {doc}`Understand CE ranges <../foundations/concepts/calibrated_interval_semantics>`.

Rule
    A feature condition with associated explanation quantities. A factual rule has a comparison weight; an alternative rule has prediction information for a different condition. A rule is not automatically an action recommendation.

    Learn more: {doc}`Read rule records <../foundations/how-to/interpret_explanations>`.

Score
    A numerical model output used for prediction or calibration. A score is not automatically a calibrated probability; check what the model and method report.

    Learn more: {doc}`Understand scores and calibration <../foundations/concepts/calibration_background>`.

Supervised learning
    Learning a prediction rule from examples with known features and target outcomes. Classification and regression are supervised predictive tasks in these CE guides.

    Learn more: {doc}`Start with predictive tasks <../foundations/concepts/predictive_tasks>`.

Target
    The outcome the model learns to predict. Numeric category codes can name classes; they do not necessarily represent a numerical amount.

    Learn more: {doc}`Interpret target labels and units <../foundations/concepts/predictive_tasks>`.

Uncertainty
    What is not settled about an outcome or model response. CE reports different kinds of ranges; identify the quantity and method rather than interpreting every range as the same uncertainty statement.

    Learn more: {doc}`Read ranges and limitations <../foundations/concepts/calibrated_interval_semantics>`.

Venn–Abers predictor
Venn-Abers predictor
    A calibration construction used for class probabilities and, with CPS information, numerical-event probabilities. The underlying pair, merged point and multiclass bounds need their own qualifications.

    Learn more: {doc}`Understand the Venn–Abers construction <../foundations/concepts/calibration_background>`.

```

<span id="software-and-naming"></span>

(software-and-technical)=
## Software & technical

```{glossary}
:sorted:

AlternativeExplanation
    The ordinary per-case alternative explanation object. It holds rules and supports alternative filtering and plotting. The concept is an alternative explanation; the class name describes a software object.

    Learn more: {doc}`Look up explanation objects <../api/index>`.

AlternativeExplanations
    A collection type used for ordinary alternative outputs. One item describes a queried case and can contain several rules; collection length is not a rule count.

    Learn more: {doc}`Read collections and rules <../foundations/how-to/interpret_explanations>`.

CalibratedExplainer
    The lower-level CE class used with a fitted learner and calibration data. The tutorials use the public wrapper to coordinate the usual workflow.

    Learn more: {doc}`Inspect the public class reference <../api/index>`.

CalibratedExplanations
    The collection type used for ordinary factual outputs, with per-case explanation objects. Specialized options can return compatible subclasses.

    Learn more: {doc}`Read explanation collections <../foundations/how-to/interpret_explanations>`.

calibrate
    The public wrapper method that prepares CE’s calibration from separate labelled calibration data after the model is fitted. It does not replace fitting or held-out evaluation.

    Learn more: {doc}`Locate the calibration call <../get-started/quick_api>`.

explain_factual
    The public method requesting factual explanations for query features. Query targets are not inputs; fitting and calibration must already be complete.

    Learn more: {doc}`Locate factual explanation calls <../get-started/quick_api>`.

explore_alternatives
    The public method requesting alternative prediction information for query features. For an event question, keep its threshold consistent with the original prediction.

    Learn more: {doc}`Generate and read alternatives <../foundations/concepts/alternatives>`.

FactualExplanation
    The ordinary object representing a single case’s factual explanation: prediction information, conditions, weights and their ranges.

    Learn more: {doc}`Look up explanation objects <../api/index>`.

feature_names
    Human-readable names attached to feature positions for rules and plots. Names do not reorder columns or replace consistent preprocessing.

    Learn more: {doc}`Keep feature representations consistent <../foundations/how-to/integrate_with_pipelines>`.

fit
    The public wrapper method that fits its predictive learner on model-fitting data. An already fitted model uses the integration workflow rather than requiring unnecessary retraining.

    Learn more: {doc}`Follow the model lifecycle <../foundations/how-to/integrate_with_pipelines>`.

GuardedOptions
    The options object passed as guarded_options to an explanation call to enable and configure guarded candidate filtering. It is not another task or regression output mode.

    Learn more: {doc}`Configure the guard <../foundations/concepts/guarded_explanations>`.

GuardedOptions.confidence
    The guard setting whose representative-point acceptance cutoff is 1 minus confidence. It is not the predicted class probability or a target-value interval’s coverage.

    Learn more: {doc}`Read the cutoff and its limits <../foundations/concepts/guarded_explanations>`.

low_high_percentiles
    The lower and upper percentile request for interval regression. The pair (5, 95) specifies a nominal (requested) central 90% interval, not fixed numerical width or individual-case certainty.

    Learn more: {doc}`Request a value and interval <../foundations/concepts/probabilistic_regression>`.

mode (API)
    The underlying classification/regression setting reported by the software. A regression threshold-event question also depends on its threshold; this setting alone does not identify all three learning modes.

    Learn more: {doc}`Separate learning terms from Python settings <../foundations/concepts/tasks_modes_capabilities>`.

Parameter
    An input controlling a call or configuration. The applicable method signature determines its accepted name, type and default; similarly named parameters need not have the same meaning.

    Learn more: {doc}`Check exact parameter contracts <../api/index>`.

plot
    A plotting method on explanation objects or collections. The selected style determines the view; notebook, interactive and headless environments have different display and saving needs.

    Learn more: {doc}`Render or save an explanation plot <../foundations/how-to/plot_with_plotspec>`.

PlotSpec
    A structured description of a plot that a rendering adapter can turn into a figure.

    Learn more: {doc}`Understand the plotting interface <../foundations/how-to/plot_with_plotspec>`.

Plugin
    A component providing an explanation, interval or plotting implementation through CE’s extension interfaces. CE includes built-in components as well as supporting extensions.

    Learn more: {doc}`Understand plugin interfaces <../plugins>`.

predict
    The public prediction method: class labels for a classifier or numerical target values for a regressor. Its options affect returned prediction information; check the task and return contract.

    Learn more: {doc}`Choose the prediction call <../get-started/quick_api>`.

predict_proba
    The public probability method: class probabilities for classification or numerical-event probabilities for regression with a threshold. Check column meanings before selecting a probability.

    Learn more: {doc}`Choose the probability call <../get-started/quick_api>`.

Reject policy
    A setting controlling how reject handling is applied. Enabling a non-NONE policy changes relevant return handling; rejection is distinct from guarded candidate filtering.

    Learn more: {doc}`Read reject-aware workflows <../practitioner/advanced/reject-policy>`.

RejectResult
    The prediction envelope returned by reject-enabled prediction calls, carrying prediction information and policy metadata. Reject-aware explanation collections use a different return form.

    Learn more: {doc}`Interpret reject-aware return types <../practitioner/advanced/reject-policy>`.

Rules payload
    The structured result of build_rules_payload(), with core explanation quantities and metadata. Read which fields describe predictions versus weights before exporting them.

    Learn more: {doc}`Inspect records and metadata <../foundations/how-to/interpret_explanations>`.

Schema v1
Explanation schema v1
    The versioned serialization contract for explanation outputs. It describes fields and compatibility.

    Learn more: {doc}`Read the serialization contract <../schema_v1>`.

Telemetry
    Metadata recording aspects of execution and component selection. It helps diagnose or audit how a result was produced.

    Learn more: {doc}`Inspect execution metadata <../foundations/how-to/configure_telemetry>`.

threshold
    The regression argument defining an event on the numerical target. For a scalar t, the reviewed probability query asks for Y ≤ t; choose t in the target’s units.

    Learn more: {doc}`Define the event before calling CE <../foundations/concepts/probabilistic_regression>`.

to_json
    An export method for serialized explanation information. Preserve quantity labels, units, ranges and relevant metadata when passing outputs onward.

    Learn more: {doc}`Export explanations <../foundations/how-to/export_explanations>`.

to_narrative
    A method producing a textual or other supported narrative presentation of explanation information. A narrative needs the same quantity meanings and limitations as the underlying records.

    Learn more: {doc}`Generate narratives <../foundations/how-to/to_narrative>`.

uq_interval
    The prediction-call flag requesting lower/upper information alongside the prediction. It does not make probability bounds, target-value intervals and feature-weight ranges interchangeable.

    Learn more: {doc}`Read prediction returns <../get-started/quick_api>`.

WrapCalibratedExplainer
Public wrapper
    The public wrapper used in the tutorials to coordinate fitting, calibration, prediction and explanation with a compatible learner. Start here before lower-level implementation classes.

    Learn more: {doc}`Run the public workflow <../get-started/first-python-explanation>`.

```

For exact method signatures, accepted parameters and return types, use the
{doc}`API reference <../api/index>`. For older names, use the
{doc}`terminology reference <../foundations/concepts/terminology>` rather than
assuming an old name remains a supported keyword. The glossary does not settle
the outstanding scientific wording questions in the shared range guide.
