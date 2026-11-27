<figure class="ce-native-figure ce-core-diagram" id="ce-wrapper-workflow" aria-label="Core Calibrated Explanations wrapper workflow">
<p class="ce-figure-heading">Calibrated Explanations: one wrapper</p>
<div class="ce-flow-node ce-ml-node ce-wrap-step"><strong>1 · Wrap the predictive model</strong><code>WrapCalibratedExplainer(model)</code></div>
<p class="ce-flow-phase">Machine learning model</p>
<div class="ce-flow-row">
<div class="ce-flow-node ce-ml-node"><strong>Training data</strong><span>Features + known targets</span></div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ml-node"><strong>2 · Fit the predictive model</strong><code>fit(X_train, y_train)</code></div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ml-node"><strong>Fitted predictive model</strong><span>Reuse this model below</span></div>
</div>
<p class="ce-flow-phase">Calibration</p>
<div class="ce-flow-row">
<div class="ce-flow-inputs">
<div class="ce-flow-node ce-ml-node"><strong>Same fitted model</strong><span>From step 2</span></div>
<div class="ce-flow-node ce-ce-node"><strong>Calibration data</strong><span>Separate features + known targets</span></div>
</div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ce-node"><strong>3 · Calibration</strong><code>calibrate(X_cal, y_cal)</code></div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ce-node"><strong>Prepared resources</strong><span>Fitted model + calibration information</span></div>
</div>
<p class="ce-flow-note">Already fitted? Skip step 2. Calibrated Explanations calibration does not retrain the predictive model.</p>
<p class="ce-flow-phase">Prediction</p>
<div class="ce-flow-row">
<div class="ce-flow-inputs">
<div class="ce-case-data">
<div class="ce-flow-node ce-ml-node"><strong>Test data</strong><span>Features + known targets</span><span>Targets kept aside for evaluation</span></div>
<div class="ce-flow-node ce-ml-node"><strong>New case</strong><span>Features available; target may be unknown</span></div>
<p class="ce-flow-note ce-case-features"><strong>Features only →</strong><br>Targets do not enter prediction or explanation calls.</p>
</div>
<div class="ce-flow-node ce-ce-node"><strong>Prepared resources</strong><span>Reuse step 3</span></div>
</div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ce-node"><strong>4 · Obtain prediction information</strong><code>predict / predict_proba</code><code>uq_interval=True</code><span>Include the reported range</span></div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ce-node"><strong>Prediction information</strong><span>Quantity and reported range depend on the task and output question</span></div>
</div>
<p class="ce-flow-phase">Explanation · two complementary choices</p>
<div class="ce-explanation-row">
<div class="ce-flow-node ce-ce-node"><strong>5a · Factual explanation</strong><code>explain_factual(X_case)</code><span>Conditions + comparison weights + ranges</span></div>
<div class="ce-flow-node ce-ce-node"><strong>5b · Alternative explanations</strong><code>explore_alternatives(X_case)</code><span>Other conditions + predictions + ranges</span></div>
</div>
<p class="ce-flow-note">The same wrapper coordinates steps 2–5. Explanation calls obtain prediction information internally; a separate step-4 call is not required.</p>
<div class="ce-flow-key"><span><i class="ce-ml-key" aria-hidden="true"></i>Machine learning / inputs</span><span><i class="ce-ce-key" aria-hidden="true"></i>Added by Calibrated Explanations</span></div>
<figcaption>Conceptual flow, with separate inputs and prepared resources. <a href="../_static/figures/ce-wrapper-workflow-transparent.png">Open the transparent image</a>.</figcaption>
</figure>
