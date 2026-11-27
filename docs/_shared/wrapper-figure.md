<figure class="ce-native-figure ce-core-diagram" id="ce-wrapper-workflow" aria-label="Core CE wrapper workflow">
<p class="ce-figure-heading">One wrapper, from fitting to explanation</p>
<div class="ce-flow-node ce-ml-node ce-wrap-step"><strong>1 · Wrap the predictive model</strong><code>WrapCalibratedExplainer(model)</code></div>
<p class="ce-flow-phase">ML model</p>
<div class="ce-flow-row">
<div class="ce-flow-node ce-ml-node"><strong>Training data</strong><span>Features + known targets</span></div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ml-node"><strong>2 · Fit the predictive model</strong><code>fit(X_train, y_train)</code></div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ml-node"><strong>Fitted predictive model</strong><span>Reuse this model below</span></div>
</div>
<p class="ce-flow-phase">CE calibration</p>
<div class="ce-flow-row">
<div class="ce-flow-inputs">
<div class="ce-flow-node ce-ml-node"><strong>Same fitted model</strong><span>From step 2</span></div>
<div class="ce-flow-node ce-ce-node"><strong>Calibration data</strong><span>Separate features + known targets</span></div>
</div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ce-node"><strong>3 · Prepare CE calibration</strong><code>calibrate(X_cal, y_cal)</code></div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ce-node"><strong>Prepared resources</strong><span>Fitted model + CE calibration information</span></div>
</div>
<p class="ce-flow-note">Already fitted? Skip step 2. CE calibration does not retrain the predictive model.</p>
<p class="ce-flow-phase">Prediction</p>
<div class="ce-flow-row">
<div class="ce-flow-inputs">
<div class="ce-flow-node ce-ml-node"><strong>Test data / New case</strong><span>Features only; target not supplied</span></div>
<div class="ce-flow-node ce-ce-node"><strong>Prepared resources</strong><span>Reuse step 3</span></div>
</div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ce-node"><strong>4 · Obtain prediction information</strong><code>predict / predict_proba</code><code>uq_interval=True</code></div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ce-node"><strong>Prediction information</strong><span>Quantity and reported range depend on the task and output question</span></div>
</div>
<p class="ce-flow-phase">Explanation · two complementary choices</p>
<div class="ce-explanation-row">
<div class="ce-flow-node ce-ce-node"><strong>5a · Factual explanation</strong><code>explain_factual(X_case)</code><span>Conditions + comparison weights + ranges</span></div>
<div class="ce-flow-node ce-ce-node"><strong>5b · Alternative explanations</strong><code>explore_alternatives(X_case)</code><span>Other conditions + predictions + ranges</span></div>
</div>
<p class="ce-flow-note">The same wrapper coordinates steps 2–5. Explanation calls obtain prediction information internally; a separate step-4 call is not required.</p>
<div class="ce-flow-key"><span><i class="ce-ml-key" aria-hidden="true"></i>Basic ML / inputs</span><span><i class="ce-ce-key" aria-hidden="true"></i>Added by CE</span></div>
<figcaption>Conceptual flow, with separate inputs and prepared resources. <a href="../_static/figures/ce-wrapper-workflow-transparent.png">Open the transparent image</a>.</figcaption>
</figure>
