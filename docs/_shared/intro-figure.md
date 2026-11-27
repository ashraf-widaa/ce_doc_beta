<figure class="ce-native-figure ce-intro-diagram" aria-label="The basic Calibrated Explanations workflow">
<div class="ce-intro-row">
<div class="ce-flow-node ce-ml-node"><strong>Fitted model</strong><span>Already trained on labelled examples</span></div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ce-node"><strong>Calibration</strong><span>Use separate labelled data with the fitted model</span></div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ce-node"><strong>Prediction</strong><span>Report the requested quantity and its range</span></div>
<span class="ce-flow-arrow" aria-hidden="true">→</span>
<div class="ce-flow-node ce-ce-node"><strong>Explanation</strong><span>Inspect factual conditions or compare alternatives</span></div>
</div>
<figcaption>Calibrated Explanations adds calibration and explanation capabilities around the same fitted model. Calibration is prepared before use; explanations can obtain prediction information internally.</figcaption>
</figure>
