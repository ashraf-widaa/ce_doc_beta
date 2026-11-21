# First explanation in Python

<span class="ce-course-step" hidden></span>

<span id="get-started"></span>
<span id="quickstart"></span>

See what CE adds to a prediction, run one complete example and read its plot.
You need basic Python knowledge and Python 3.10 or later. The example uses
Iris data included with scikit-learn; no account or separate dataset download
is needed.

For the no-install learning route, use {doc}`Quickstart <index>`.

Start at **1. Install**, then run the cells in order. You will see a real class
prediction and learn how to read its factual plot. If the terms or workflow are
new, open the short background below first.

<details><summary>Before you run: the CE workflow, features and target</summary>

<span id="what-ce-adds"></span>

**What CE adds**

```{include} ../_shared/ce-workflow.md
```

The figure shows the additional stages, not a claim that a conventional ML
model cannot be calibrated or used with other explanation methods.

<span id="predictive-tasks"></span>

**Predictive tasks**

```{include} ../foundations/concepts/predictive_tasks.md
:start-after: <!-- predictive-tasks:start -->
:end-before: <!-- predictive-tasks:end -->
```

Here, each observation is one Iris flower. Its four features are sepal length,
sepal width, petal length and petal width, measured in centimetres. The target
is the species: **setosa**, **versicolor** or **virginica**. This is classification.
For optional background, see [supervised learning](https://developers.google.com/machine-learning/intro-to-ml/supervised).


</details>

## 1. Install

Run this in the environment used by your script or notebook:

```bash
python -m pip install "calibrated-explanations[viz]" scikit-learn
```

The `viz` extra supplies plotting dependencies. In a notebook, use a kernel
from that same environment. See {doc}`installation` if setup fails.

## 2. Keep the data roles separate

```{include} ../foundations/concepts/predictive_tasks.md
:start-after: <!-- data-roles:start -->
:end-before: <!-- data-roles:end -->
```

The code uses 90 model-fitting rows, 30 calibration rows and 30 evaluation rows.
These are the existing classification tutorial's splits. Learn more in
{doc}`the shared data-role explanation <../foundations/concepts/predictive_tasks>`
or the general guide to [dividing datasets](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets).

Calibration is not another model-fitting step. For general probability-calibration
background, see [scikit-learn's calibration guide](https://scikit-learn.org/stable/modules/calibration.html).
For CE-specific assumptions and range meanings, use the
{doc}`semantics reference <../foundations/concepts/calibrated_interval_semantics>`.

## 3. Run the complete example

Run the following cells in order in one Python session, or save the complete
script as `first_explanation.py` and run `python first_explanation.py`. You can also
{download}`download the script <../_examples/first_explanation.py>`.
The selected case is the second evaluation row, `x_test[1:2]`; no target value
is supplied to explain it. Other cases can expose the multiclass range limitation
described under **If the result differs** below.

### Prepare the labelled examples

Load Iris and create the three data roles described above. This cell creates
arrays; it does not print a result. The 30 evaluation rows remain outside fitting
and calibration.

```{literalinclude} ../_examples/first_explanation.py
:language: python
:lines: 1-19
```

### Fit the model, then calibrate

The wrapper fits the random forest on `x_proper, y_proper`, then builds CE's
calibration using `x_cal, y_cal`. Feature names label the explanation; they do not
change the feature order. This cell prepares the explainer without printing output.

```{literalinclude} ../_examples/first_explanation.py
:language: python
:lines: 21-23
```

### Predict and explain one held-out flower

`case` contains one row's features. Select the largest reported class probability,
map its column to the species name, and request a factual explanation. The final
print statements let you check both the split and the returned quantities.

```{literalinclude} ../_examples/first_explanation.py
:language: python
:lines: 25-36
```

Verified output from the review environment:

```{literalinclude} ../_examples/first_explanation_output.txt
:language: text
```

The three probabilities follow `dataset.target_names`: setosa, versicolor,
virginica. The largest reported probability belongs to versicolor. Numeric
values can vary with software versions; these values were checked in the
review environment. Do not suppress warnings or clip bounds to force a match.

## 4. Read the plot

Display the factual explanation from the same session:

```{literalinclude} ../_examples/first_explanation.py
:language: python
:lines: 38
```

This cell produces a figure rather than a text result. In a script, a supported
Matplotlib window should open; close it to finish. In a notebook the plot
normally appears beneath the cell. Here is the generated plot for this case:

```{figure} assets/first-explanation.png
:alt: CE factual explanation for the Iris versicolor case, with prediction information above four feature conditions and their weights and ranges.
:width: 100%

Factual explanation generated by the example. Select the plot for a larger view.
```

[Download the full-size plot](assets/first-explanation.png).

Read the figure in this order:

1. **Prediction information:** the example reports versicolor with probability
   about `0.910` and returned bounds `[0.902, 0.992]`. These are prediction
   quantities; they are not feature weights or a confidence interval for the
   individual's true class probability. In the figure, `y=1` means versicolor;
   `y!=1` means either of the other species.
2. **Feature conditions:** each label describes a condition that holds for this
   flower, such as `petal width (cm) > 0.65`.
3. **Feature weights:** positive weights here describe a higher model probability
   for the explained class relative to CE's substituted feature scenarios;
   negative weights describe a lower probability. They are not causal effects
   or Shapley values.
4. **Weight ranges:** read the range alongside the weight. For example, a positive
   point weight can have a range that crosses zero. These ranges do not inherit
   a universal per-feature coverage guarantee.

The shared {doc}`interpretation guide <../foundations/how-to/interpret_explanations>`
explains rules, records and plots in more detail. Different quantities require
{doc}`different semantics and assumptions <../foundations/concepts/calibrated_interval_semantics>`.
A single example does not evaluate your model or establish deployment validity.

## If the result differs or no plot appears

- **Import or environment error:** follow {doc}`troubleshooting` and check that
  installation and execution use the same Python environment.
- **No figure:** confirm that the `viz` extra and a notebook or desktop plotting
  backend are available. A headless server needs a saved image instead of a GUI.
- **Unexpected ranges:** the baseline can return multiclass bounds outside
  `[0, 1]` for some cases. This worked case is not evidence that all multiclass
  bounds are conventional probability intervals. Keep the raw output and seek
  maintainer review; do not clip it. See the
  {doc}`documented review limitation <quickstart_classification>`.

## Continue the guided introduction

**Understand the plot:** {doc}`../foundations/how-to/interpret_explanations`.

**Next chapter:** {doc}`Check results on held-out data <../practitioner/check_results>`. This complete plotted example is an alternative to running the shared chapter cells. You do not need to repeat both.


<span id="choose-your-next-step"></span>

## Other directions after the example

| Your goal | Continue with |
| --- | --- |
| Explore more classification calls and alternatives | {doc}`Classification tutorial <quickstart_classification>`. |
| Predict a numeric target or ask about a threshold | {doc}`Regression tutorial <quickstart_regression>`. |
| Use an existing model and preprocessing | {doc}`Pipeline integration <../foundations/how-to/integrate_with_pipelines>`. |
| Understand the mechanisms and assumptions | {doc}`How CE Works <../sections/how-ce-works>`. |
| Find a method or parameter | {doc}`Quick API <quick_api>` or {doc}`API reference <../api/index>`. |

<!-- Entry-point tier: Tier 1. -->
