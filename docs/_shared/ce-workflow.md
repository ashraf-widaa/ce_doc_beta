<figure class="ce-workflow" aria-label="Preparing a CE system and using it with a new case">
<div class="ce-workflow-grid">
<div class="ce-workflow-lane"><p class="ce-workflow-heading">Prepare and evaluate</p><ol><li>Fit the predictive model using training features and known targets.</li><li>Configure CE with that fitted model and separate labelled calibration data.</li><li>Query held-out test features; use their targets only to check the outputs.</li></ol></div>
<div class="ce-workflow-lane"><p class="ce-workflow-heading">Use with a new case (inference)</p><ol><li>Supply the new case’s features; its target is not required.</li><li>Reuse the same fitted model and CE calibration state, without refitting.</li><li>Read prediction information and factual or alternative explanations with their mode-specific ranges.</li></ol></div>
</div>
<figcaption>Model-only use returns a class, value or score. CE adds calibration state and explanations around the same fitted model. Calibration may fit calibrators; it does not refit that predictive model. Range meanings and conditions depend on the selected method.</figcaption>
</figure>
