# Practitioner hub

<span class="ce-choice-page" hidden></span>

Choose a practical task, interpret its result and check it before adapting
advanced workflows. Browser and Python routes are both available from
{doc}`CE in Practice <../sections/in-practice>`.

## Core path

1. Run {doc}`../get-started/quickstart_classification` or
   {doc}`../get-started/quickstart_regression`.
2. Read {doc}`../foundations/how-to/interpret_explanations`.
3. Choose API style in {doc}`task_api_comparison`.
4. Apply production workflows in {doc}`playbooks/index`.

Semantics and non-guarantees are documented in
{doc}`../foundations/concepts/calibrated_interval_semantics`.

## Check your result before extending

Use {doc}`check_results` for held-out probability, interval and event checks.
An explanation or teaching game is not a deployment evaluation.

## Follow a route by learning goal

These are optional routes through shared pages, not six compulsory steps. Start
with the question you have now. Read the linked concept, try the procedure, then
check what the result establishes. The same page can support several goals.

<div class="ce-mode-grid" role="list" aria-label="Learning routes by goal">
<div class="ce-mode-card" role="listitem"><h3>Calibration</h3><p><a href="../foundations/concepts/calibration_background.html">Understand calibration</a> → <a href="../get-started/quickstart_classification.html">run the classification example</a> → <a href="../foundations/concepts/calibrated_interval_semantics.html">check method-specific conditions</a>.</p></div>
<div class="ce-mode-card" role="listitem"><h3>Ranges and intervals</h3><p><a href="../foundations/how-to/interpret_explanations.html">Identify the quantity and range</a> → <a href="playbooks/decision-policies.html">consider decision policies</a> → <a href="check_results.html">evaluate held-out results</a>.</p></div>
<div class="ce-mode-card" role="listitem"><h3>Alternatives</h3><p><a href="../foundations/concepts/alternatives.html">Understand alternative explanations</a> → <a href="playbooks/ensured-explanations.html">explore ensured filtering</a> → <a href="../foundations/concepts/guarded_explanations.html">read about guarded support filters</a>.</p></div>
<div class="ce-mode-card" role="listitem"><h3>Subgroups</h3><p><a href="../foundations/concepts/calibrated_interval_semantics.html">Check group-specific conditions</a> → <a href="../foundations/how-to/conditional_calibration.html">configure conditional calibration</a> → <a href="playbooks/mondrian-calibration.html">follow the Mondrian playbook</a> → <a href="check_results.html">review groups and drift</a>.</p></div>
<div class="ce-mode-card" role="listitem"><h3>Rejecting cases</h3><p><a href="playbooks/decision-policies.html">Understand the decision policy</a> → <a href="advanced/reject-policy.html">use the reject guide</a> → <a href="../researcher/advanced/difficulty_normalized_reject.html">read the difficulty-reject research</a>.</p></div>
<div class="ce-mode-card" role="listitem"><h3>Evidence and review</h3><p><a href="../foundations/how-to/interpret_explanations.html">Interpret the records</a> → <a href="../foundations/how-to/export_explanations.html">export explanations</a> → <a href="../foundations/how-to/safe-defaults.html">review operational defaults</a> → <a href="../foundations/governance/index.html">find governance policies</a>.</p></div>
</div>

Existing evaluation and governance pages cover the corresponding topics; this
map does not claim automatic monitoring, recalibration or regulatory compliance.
Advanced filtering and reject methods have their own prerequisites and limitations.

## Optional tools

Use {doc}`advanced/index` only when you need performance, telemetry, or plugin
extensions.


Entry-point tier: Tier 1.

```{toctree}
:maxdepth: 1
:hidden:

Check results on your data <check_results>
Task API Comparison <task_api_comparison>
Practitioner playbooks <playbooks/index>
Practitioner advanced topics <advanced/index>
Narrative Template Customization <narrative_templates>
```
