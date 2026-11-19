# Check results on your data

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
