<figure class="ce-native-figure ce-quickstart-workflow" aria-label="Numbered workflow using one Calibrated Explanations wrapper">
<div class="ce-flow-node ce-ml-node ce-wrap-step"><strong>1 · Wrap the predictive model</strong><code>WrapCalibratedExplainer(model)</code></div>
<p class="ce-flow-phase">Same wrapper · Machine learning model</p>
<div class="ce-flow-row">
<div class="ce-flow-node ce-ml-node"><strong>Training data</strong><span>Features + known targets</span></div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ml-node"><strong>2 · Fit predictive model</strong><code>fit(X_train, y_train)</code></div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ml-node"><strong>Fitted predictive model</strong></div>
</div>
<p class="ce-flow-phase ce-stage-transition">↓ Calibration</p>
<div class="ce-flow-row">
<div class="ce-flow-node ce-ce-node"><strong>Calibration data</strong><span>Features + known targets</span></div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ce-node"><strong>3 · Prepare calibration</strong><code>calibrate(X_cal, y_cal)</code></div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ce-node"><strong>Fitted model + calibration information</strong></div>
</div>
<p class="ce-flow-phase ce-stage-transition">↓ Prediction</p>
<div class="ce-query-row">
<div class="ce-flow-node ce-ml-node"><strong>Test Data / New Case</strong></div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ce-node"><strong>4 · Predict</strong><code>predict / predict_proba</code><code>uq_interval=True</code><span>Include the reported range</span></div>
</div>
<p class="ce-flow-phase ce-stage-transition">↓ Explanation · two complementary choices</p>
<div class="ce-explanation-row">
<div class="ce-flow-node ce-ce-node"><strong>5a · Factual explanation</strong><code>explain_factual(X_case)</code><span>Conditions + comparison weights + ranges</span></div>
<div class="ce-flow-node ce-ce-node"><strong>5b · Alternative explanations</strong><code>explore_alternatives(X_case)</code><span>Other conditions + predictions + ranges</span></div>
</div>
<p class="ce-flow-note">5a and 5b are choices; explanation calls obtain prediction information internally.</p>
<div class="ce-flow-key"><span><i class="ce-ml-key" aria-hidden="true"></i>Machine learning / inputs</span><span><i class="ce-ce-key" aria-hidden="true"></i>Added by Calibrated Explanations</span></div>
<figcaption>One wrapper connects training, calibration, prediction and explanation. The fitted model from step 2 is used during calibration; the prepared resources from step 3 are reused for prediction and explanation.</figcaption>
</figure>
