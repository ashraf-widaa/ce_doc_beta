# Check results on your data

<span class="ce-course-step" hidden></span>

An explanation that runs successfully is not an evaluation. Use independent
held-out outcomes to check the quantity your application actually uses.
This page is an evaluation guide, not a claim that one metric proves validity.

## Keep evaluation separate

Decide the task, model, calibration procedure and event definitions before using
the final evaluation set. Preserve fitting/calibration/evaluation roles, record
versions and random seeds, and check preprocessing consistency. A query used in
a tutorial is not itself evidence of performance on another population.

## Choose checks for the output

| Output | Useful checks | Important distinction |
| --- | --- | --- |
| Class probabilities | Brier score or log loss, reliability plots with sample counts, class balance and task-relevant discrimination metrics. | Good classification accuracy does not establish probability calibration. |
| Numeric intervals | Empirical coverage and interval width on held-out outcomes; inspect both together. | A wide interval can cover often while being unhelpful; aggregate coverage can hide subgroup differences. |
| Threshold-event probabilities | Define the event in target units, form its observed binary outcome, then assess the reported probability for that event. | A numeric target interval is not a substitute for evaluating the event probability. |
| Explanation ranges and alternatives | Check which quantity is compared, sensitivity to appropriate configuration changes, feature plausibility and relevant application constraints. | Prediction metrics do not certify causal explanation correctness or per-feature coverage. |

Report sample sizes and uncertainty in empirical estimates. Small groups can
produce unstable-looking metrics. If you define groups or thresholds after
inspecting results, say so; exploratory checks and final evaluation serve
different purposes.

## Complete the shared lab with held-out checks

Continue the Iris session from {doc}`the explanation chapter <../foundations/concepts/how_explanations_are_built>`,
or run the {download}`complete shared lab <../_examples/learning_lab.py>` first.
Only now use `y_test`, the held-out observed targets, to assess predictions.
It was not an input to the preceding query or explanation calls.

**Accuracy** is the fraction of predicted labels matching the observed labels.
**Log loss** evaluates probability assigned to observed classes; lower is better
when comparing predictions on the same evaluation task and data. It is not an
error percentage or a standalone test of calibration. The last lines also check
for the reviewed source's known out-of-range multiclass bounds.

```{literalinclude} ../_examples/learning_lab.py
:language: python
:start-after: checking:start
:end-before: checking:end
```

Verified output from the review environment:

```{literalinclude} ../_examples/learning_lab_output.txt
:language: text
:start-after: CHECKING_START
:end-before: CHECKING_END
```

Accuracy 0.933 means about 93.3% of these 30 held-out labels matched, not that
every probability or interval is valid. Log loss 0.212 is a loss value, not
21.2% misclassification. The final count is one **case/class bound entry** outside
`[0, 1]`, not one proven calibration failure or a diagnostic of causal correctness.
The element-wise `|` in the code means “lower below zero or upper above one”.

That diagnostic matters even when the label metric looks good. Keep the raw
outputs and seek maintainer review before relying on uninterpretable bounds;
do not clip them or choose only examples that hide the issue. This small teaching
split is not a benchmark, deployment validation or a proof of any statistical
guarantee. Results can vary by version and case selection.

## Inspect failures instead of hiding them

Retain warnings and raw outputs. Record unexpected bounds, missing classes,
empty alternatives and unsupported feature conditions. Do not clip reported
ranges, silently remove difficult cases or suppress warnings to make a report
look plausible. The versioned {doc}`classification tutorial <../get-started/quickstart_classification>`
records a known multiclass bound issue requiring maintainer review.

## Decide whether the application is ready

Ask whether the calibration population resembles the intended use, whether
costs and decision thresholds are appropriate, and how failures or drift will
be detected. Appropriate oversight, privacy, fairness and operational checks
depend on the application; a tutorial or teaching game does not complete them.

Continue to the {doc}`practitioner playbooks <playbooks/index>` for specific
workflows. Use {doc}`statistical background <../foundations/concepts/calibration_background>`
for the concepts and {doc}`canonical semantics <../foundations/concepts/calibrated_interval_semantics>`
for the actual method-specific assumptions and limits.

## Finish the guided introduction

**Previous chapter:** {doc}`Interpret calibrated explanations <../foundations/how-to/interpret_explanations>`.

## Choose where to continue

You have now followed data → task/question → calibration → explanation → held-out
checks using one example. The {doc}`Practitioner Hub <index>` offers goal-specific
guides for applying it. Use the {doc}`Researcher Hub <../researcher/index>` for
papers and replication, or the {doc}`Contributor Hub <../contributor/index>` to
understand components, contracts and a contribution workflow. None requires
copying the definitions into a second tutorial.
