(ce-optional-capability-map)=
# Optional capabilities: when and how to use them

Start with one ordinary result from {doc}`Quick Start </get-started/index>`,
then use the {ref}`numbered wrapper workflow <ce-wrapper-workflow-map>` to place each option.
Follow one housing case through it: a fitted model estimates an area’s median
housing value; Calibrated Explanations (CE) uses separate labelled calibration cases and can explain the
result. You may ask either for a **value and interval** or for the **probability
of a value at most a budget**. Keep that question fixed when reading an explanation.

The options below address different needs within this same flow. They are not
extra predictive tasks or settings everyone must enable.

```{include} ../../_shared/capability-stage-map.md
```

The stages correspond to the {ref}`shared wrapper figure <ce-wrapper-workflow-map>`
(calibration at step 3, prediction at step 4, explanations at steps 5a/5b). Each
column introduces an operation and its software entry point. **Rejection** concerns cases;
**alternative filtering** selects rules; **guarded explanations** check
candidates during explanation construction. They are different operations.

For the complete concept-to-function map, use
{ref}`Optional capabilities in Quick API <optional-capability-api-map>`.
The walkthrough below explains when and why these options may be useful.

**Combining conditions:** the figure also shows conjunctions, which combine
feature conditions into a rule. See {doc}`interpreting explanations </foundations/how-to/interpret_explanations>`
for the rule context. The walkthrough below follows calibration groups, guarding,
alternative selection and rejection through one housing example.

## At calibration: should regions be treated separately?

In step 3 of the core workflow, find **Calibration data** entering **Prepare calibration**. The calibration procedure
uses these cases’ known outcomes to construct prediction information.

Suppose your application defines Region A and Region B. With
{term}`Mondrian calibration <Mondrian calibration>`, also called conditional
calibration, you supply or derive a group label for each calibration case and
query. For a new area assigned to Region A, the selected construction uses Region A’s
calibration cases rather than treating all regions as one calibration group. You still use the fitted predictive model and the same housing target;
the group-specific calibration can change the reported prediction information
and its range.

Use this option when the grouping is relevant to your application and the
method’s conditions are appropriate. The available calibration cases within each
group matter; defining regions alone does not establish fairness or guarantee improved results.

**Learn next:** {doc}`supply group labels and check the conditional setup </foundations/how-to/conditional_calibration>`.
For a numerical target, keep the selected {doc}`value or event question </foundations/concepts/probabilistic_regression>`.

## While building explanations: are candidate conditions supported?

Return to the shared wrapper workflow’s **factual and alternative explanation outputs**.
To construct them, CE considers feature conditions. A **candidate** is a condition
being considered for a rule, before it appears in the returned explanation.

For the housing case, changing an income condition while leaving the other
features fixed might create a combination poorly represented in the calibration
data. {term}`Guarded explanations <Guarded explanation>` check selected test
copies of the case, with feature values replaced by representatives of candidate
conditions. The configured guard rule decides which candidates to retain.

Read the returned rules alongside the **audit**, which reports counts of tested
and removed candidates. Passing checks at representatives does not certify every
value in a numerical interval, or automatically check whether the original
area’s full feature combination is supported by the calibration data. Guarding is a check during explanation construction, not a general
certificate for the prediction.

**Learn next:** {doc}`understand the guard, supported configuration and audit </foundations/concepts/guarded_explanations>`.

## After generating alternatives: which ones should I inspect?

Look at the **Alternative explanations** output in the shared wrapper workflow. One case can have several rules,
each reporting a prediction under a different condition. You can inspect them
all or select a subset for a stated purpose, whether or not you used a guard.

{term}`Alternative filtering <Alternative filtering>` selects from those existing
rules. For example, an **ensured** filter keeps alternatives whose reported
prediction interval is no wider than the original prediction interval. Width
here means the difference between the reported upper and lower values. For a
value question, compare target-value interval widths; for an event question,
compare probability-bound widths. Keep the quantity and scale the same.

Other criteria also need their mode: crossing a probability comparison boundary
is a different question from obtaining a lower numerical house-value prediction.
Filtering helps organize what you inspect. It does not prove that changing an
area’s income would cause the alternative outcome, or that a narrower reported
range improves predictive accuracy.

**Learn next:** {doc}`choose an alternative filter and read its mode-specific criterion </foundations/concepts/alternatives>`.

## When using the prediction: should some cases be flagged or set aside?

Return to **Prediction information** in the shared wrapper workflow. Your application may
need to treat some cases differently rather than use every result in the same way.
{term}`Rejection <Rejection>` identifies cases under a supported, task-specific
rejection procedure. A **reject policy** controls how that status affects handling—for example,
tagging cases or selecting cases for explanation. Your application decides the
follow-up action.

For the housing example, the reviewed regression rejection procedure requires
a defined event threshold, such as the budget used for the event-probability
question. A wide house-value interval alone is not that procedure. Classification
has its own construction and interpretation; do not transfer the regression setup
or its assumptions unchanged to another task.

The distinction is the item being handled: alternative filters select explanation
rules; rejection concerns queried cases. A case can have a model prediction while
also receiving a rejection status under the configured procedure.

**Learn next:** {doc}`configure rejection for your task and interpret the returned status </practitioner/advanced/reject-policy>`.

Choose only the options your problem needs. Their supported combinations and
statistical conditions depend on the task, mode, configuration and software
version. The browser guide and Python guides identify their own available controls.
For the meaning of each range, keep the shared
{doc}`range guide </foundations/concepts/calibrated_interval_semantics>` nearby.


## Continue from the option you need

Follow the detailed guide linked beside that option for its setup and limits.
For the calls, use the {ref}`shared Quick API map <optional-capability-api-map>`.
To return to the core method, use {doc}`How CE Works </sections/how-ce-works>`;
to adapt a complete example, use {doc}`CE in Practice </sections/in-practice>`.
