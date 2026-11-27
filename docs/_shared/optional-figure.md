<figure class="ce-native-figure ce-options-diagram" aria-label="Optional Calibrated Explanations capabilities and their workflow positions">
<p class="ce-figure-heading">Optional Calibrated Explanations capabilities: where they fit</p>
<div class="ce-option-card">
<p class="ce-option-stage">Step 3 · Calibration; use consistent group labels for test observations or new cases</p>
<div class="ce-option-content"><div><strong>Mondrian calibration</strong><span>Use defined calibration groups.</span></div><code>calibrate(..., bins=...)</code><p>Supply consistent group labels. These are not target labels; grouping alone does not establish fairness.</p></div>
</div>
<div class="ce-option-card">
<p class="ce-option-stage">During 5a / 5b · Explanation construction</p>
<div class="ce-option-content"><div><strong>Guarded explanations</strong><span>Check selected candidate representatives.</span></div><code>guarded_options=GuardedOptions()</code><p>Inspect retained rules and the guard audit. This is not a universal check of the original case.</p></div>
</div>
<div class="ce-option-card">
<p class="ce-option-stage">5a / 5b · Explanation rules</p>
<div class="ce-option-content"><div><strong>Conjunctions</strong><span>Combine feature conditions.</span></div><code>add_conjunctions(...)</code><p>Inspect the combined rule; do not obtain it by simply adding individual weights.</p></div>
</div>
<div class="ce-option-card">
<p class="ce-option-stage">After 5b · Generated alternatives</p>
<div class="ce-option-content"><div><strong>Alternative filtering</strong><span>Select existing alternative rules.</span></div><code>ensured_explanations()</code><p>This and other filters apply a stated selection criterion. Compare on the same output scale.</p></div>
</div>
<div class="ce-option-card">
<p class="ce-option-stage">4 / 5 · Case handling, after method-specific setup</p>
<div class="ce-option-content"><div><strong>Rejection</strong><span>Compute case status; control processing.</span></div><code>reject_policy=RejectPolicy.FLAG</code><p>Tag cases; the application chooses follow-up. A status is not a correctness guarantee.</p></div>
</div>
<p class="ce-flow-note">Dashed orange boxes are optional choices, not compulsory stages. Check supported task, mode and configuration.</p>
<figcaption>Each option has a different job. <a href="../../_static/figures/ce-optional-capabilities-transparent.png">Open the transparent image</a>.</figcaption>
</figure>
