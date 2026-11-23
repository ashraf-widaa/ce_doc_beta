# Classification: read a prediction

<span class="ce-choice-page" hidden></span>

A classifier predicts a category. The Diabetes example has two classes
(**binary**); the Iris example has three species (**multiclass**).

**Goal:** read one prediction and its reported range, then inspect the feature
conditions and alternative predictions that help explain the model's response.

## Choose where to run it

Choose one environment. The browser and Python examples use different datasets;
follow the selected guide's labels, units and setup. You can also read the captured
results below without running either route.

<div class="ce-route-grid" role="navigation" aria-label="Ways to run this example">
<a class="ce-route-card" href="expert-hub.html#expert-classification"><strong>Browser: binary Diabetes</strong><span>Explore preparation, calibration and one result without Python.</span><span>Open the browser guide →</span></a>
<a class="ce-route-card" href="first-python-explanation.html"><strong>Python: multiclass Iris</strong><span>Install CE and run the same flower case explained below.</span><span>Open the Python example →</span></a>
</div>

## Read the binary result

A captured Diabetes case reports **positive probability 0.7448**, with bounds
**[0.7273, 0.7959]**. Read “positive” first: this identifies the class whose
probability is displayed. This is an educational model output, not a diagnosis.

Here, `plas` is the dataset’s glucose feature. The factual condition
`plas > 139.50` has weight **+0.517**, range
**[0.510, 0.538]**. That weight is a model-response difference; it is not another
patient probability. The alternative `plas < 147.50` reports probability
**0.2719**, bounds **[0.2487, 0.2811]**. It describes the model under a different
condition, not the effect of a medical intervention.

These are dated results from the {doc}`browser guide <expert-hub>`; your session
can differ. Keep its screenshot open while identifying the three quantities.

(classification-one-case)=
## Follow one Iris case without code

The local example predicts a flower's **species** from four measurements. The
possible targets are setosa, versicolor and virginica. We inspect the second
held-out case, using its features without supplying its known species to CE.
The same fitted model and row are used in the Python example and shared chapters.

**First, read the prediction.** The raw random forest puts all its reported
probability on versicolor. After calibration, CE reports the following values:

```{literalinclude} ../_examples/learning_lab_output.txt
:language: text
:start-after: CALIBRATION_START
:end-before: CALIBRATION_END
```

The CE columns follow the three species in the order listed above. Versicolor
has the largest probability, about 0.910. The reported bounds [0.902, 0.992]
belong to that class probability. They are not feature weights or a conventional
confidence interval containing this flower's unknown “true probability”. A raw
score of 1.000 is not certainty; this single comparison also does not establish
that calibration improves predictive scores.

**Next, inspect a factual condition and an alternative.** These are actual
outputs for the same flower:

```{literalinclude} ../_examples/learning_lab_output.txt
:language: text
:start-after: EXPLANATION_START
:end-before: EXPLANATION_END
```

The factual condition `sepal length (cm) > 5.55` holds for this flower. Its weight
+0.388 is a comparison of calibrated model responses; its range [0.240, 0.433]
belongs to that weight. It is not a 0.388 probability of the species.

The alternative changes the condition to `sepal length (cm) < 5.55` and reports
probability 0.522. Compare that **prediction** with the original 0.910; do not
mistake it for another feature weight. These comparisons describe the model,
not the real-world effect of changing a flower's measurements.

**Read the plot after naming the quantities.** Prediction information appears
above the feature conditions and their weight ranges:

```{figure} assets/learning-lab-factual.png
:alt: Verified factual explanation for the same Iris case: versicolor probability and bounds above four feature conditions with their comparison weights and ranges.
:width: 100%

The same flower's factual explanation, generated from the shared example.
```

[Open the plot at full size](assets/learning-lab-factual.png). Here `y=1` means
versicolor, while `y!=1` combines the other species. With uncertainty displayed,
the solid portion of a feature bar need not end at its point weight; use the
{doc}`shared plot-reading guide <../foundations/how-to/interpret_explanations>`
for that rendering convention.

**What can you conclude?** You can identify the selected class, distinguish its
bounds from a weight range, and compare one alternative prediction with the
original. You cannot infer a causal effect or validate all multiclass ranges
from this one case. The baseline can return bounds outside [0, 1] on other cases;
see the {doc}`documented classification limitation <quickstart_classification>`.

To reproduce the prediction and plot, follow {doc}`First explanation in Python <first-python-explanation>`.
Once CE is installed, the {download}`shared example script <../_examples/learning_lab.py>`
generates both printed blocks above, including the alternative. Save it as
`learning_lab.py` and run `python learning_lab.py` in that environment.
To understand its construction first, follow {doc}`How CE Works <../sections/how-ce-works>`.
For further calls after reproducing this case, use the {doc}`classification tutorial <quickstart_classification>`.

<span id="read-the-multiclass-result"></span>

## Check your understanding

Can you name the predicted quantity, its units and the class or event if applicable?
Can you distinguish the prediction range, a factual weight and an alternative
prediction? If not, use {doc}`Interpret calibrated explanations <../foundations/how-to/interpret_explanations>`
with the result still open. You do not need to learn every API field to read one case.

<details><summary>Go deeper: how this mode produces its outputs</summary>

<span id="see-the-mode-specific-workflow"></span>

**Mode-specific workflow**

<figure>
<picture>
<source media="(max-width: 600px)" srcset="../_static/figures/ce-mode-classification-mobile.svg">
<img src="../_static/figures/ce-mode-classification.svg" width="1000" height="570" alt="Classification: fitted model and separate labelled calibration data, method-specific calibration, new-case features, prediction information and factual or alternative explanations.">
</picture>
</figure>

[Open the full-size figure](../_static/figures/ce-mode-classification.svg).

The arrows show information flow, not a required sequence of API calls.
Prediction and explanation operate on the same calibrated system; the
explanation call can obtain its own prediction. Read the result in this mode's
units and keep the prediction range separate from a feature-weight range.
For exact assumptions and limitations, use
{doc}`calibrated interval semantics <../foundations/concepts/calibrated_interval_semantics>`.


</details>

## Semantics for this example

- **Mode:** Classification (Venn–Abers).
- **Calibration prerequisites:** a fitted model and separate labelled calibration data.
- **Guarantees:** use the method-specific statements in {doc}`calibrated interval semantics <../foundations/concepts/calibrated_interval_semantics>`.
- **Assumptions:** check the mode’s sampling conditions and calibration/deployment relationship there.
- **Non-guarantees:** no individual-case certainty or unconditional protection under drift.
- **Feature-level limits:** weight ranges are not causal or universal per-feature coverage guarantees.


## Continue from this result

**Try another question:** return to {doc}`the big picture <index>`.
**Understand the construction:** {doc}`How CE Works <../sections/how-ce-works>`.
**Adapt to your data:** {doc}`Checking results <../practitioner/check_results>`.
**Find the exact call:** {doc}`Quick API <quick_api>`.

<!-- Entry-point tier: Tier 2. -->

<!-- Preserve previous section links. -->
<span id="binary-and-multiclass-the-same-task-different-class-sets"></span>
<span id="continue-from-the-result"></span>
<span id="read-your-result"></span>

<span id="classification-explain-a-class-prediction"></span>
