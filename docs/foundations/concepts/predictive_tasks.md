# Predictive tasks and data roles

<span class="ce-course-step" hidden></span>

This chapter introduces features, targets and data roles, then prepares one small
example that continues through calibration, explanation and evaluation.

## Predictive tasks

<!-- predictive-tasks:start -->
Calibrated Explanations (CE) works with machine-learning models that perform
**predictive tasks**. A predictive task specifies the outcome we want a model
to estimate from the information available about a case. The available
information is represented by **input features**. The outcome the model learns
to predict is called the **target**.

In **supervised learning**, the model is trained on examples for which both
the features and the target are known. Each example is an **observation**.
After training, the model uses the features of a new observation to predict
its unknown target. If the target is a category, the task is **classification**.
If it is a numerical quantity, the task is **regression**.
<!-- predictive-tasks:end -->

For general background, see [supervised learning](https://developers.google.com/machine-learning/intro-to-ml/supervised).
The existing {doc}`classification tutorial <../../get-started/quickstart_classification>`
uses Iris flower measurements to predict a species. The
{doc}`regression tutorial <../../get-started/quickstart_regression>` uses a
numeric target; threshold queries ask a different question about that target.

## Data roles in CE

Here, **proper training** means the model-fitting subset, kept separate from
calibration. The code names it `x_proper, y_proper`.

<!-- data-roles:start -->
| Data | Role in this example |
| --- | --- |
| Model-fitting data | Features and known targets used to fit the predictive model. |
| Calibration data | Separate features and known targets used by CE's calibration procedure. |
| Evaluation data | Held-out observations reserved for checking results after fitting and calibration. |

A query is the case you ask CE to predict or explain. The tutorial queries one
evaluation case using its features, without giving its target to the prediction
or explanation call.
<!-- data-roles:end -->

A three-way split is used in the tutorials. It is an introductory workflow,
not an instruction that these proportions suit every dataset. For general
background, see [dividing datasets](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets).
CE's additional calibration set must remain explicit. Method-specific sampling
assumptions and non-guarantees are in {doc}`calibrated_interval_semantics`.


## Work with one dataset before choosing a method

We will use **Iris** throughout the guided introduction: each flower is an
observation, its measurements are features, and its species is the target. This
keeps the context fixed as we move from data to calibration and explanation.
The separate regression tutorials demonstrate numerical targets afterward.

In Python, `x` is a **feature matrix**: rows are observations and columns are
features. `y` is a target array with one entry per row. The letters are conventional
names, not special CE API keywords. Iris measurements are in centimetres; the
species names are categories.

### Prepare a session and inspect the data

Use Python 3.10 or later and the environment described in
{doc}`Installation <../../get-started/installation>`. This lab does not plot, so
it needs the base package and scikit-learn:

```bash
python -m pip install calibrated-explanations scikit-learn
```

Run the installation command in a terminal. Run the Python cell below in a script
or notebook using that environment. Continue using the same session in later chapters so its
arrays remain available. You can also
{download}`download the complete shared lab <../../_examples/learning_lab.py>`
and run it as a script. The source is reused by the later chapters; no custom
wrapper or unintroduced dataset is required.

```{literalinclude} ../../_examples/learning_lab.py
:language: python
:start-after: data:start
:end-before: data:end
```

Verified output from the review environment:

```{literalinclude} ../../_examples/learning_lab_output.txt
:language: text
:start-after: DATA_START
:end-before: DATA_END
```

Read `(150, 4)` as 150 flowers described by four measurements. The three species
are the target categories. The row counts describe separate data roles, not
three different predictive tasks. The first split reserves 30 evaluation rows. The second takes 30 calibration
rows from the remaining 120, leaving 90 for fitting. `random_state=0` makes the
random partition repeatable; `stratify` approximately preserves species proportions.
Neither establishes the statistical assumptions needed for CE.

### Why hold data aside?

Fitting learns the predictive model from the proper training set. Calibration
uses other labelled cases to construct prediction information. Evaluation uses
held-out outcomes to assess the resulting system. A query may be an evaluation
row, but its target is not passed into its prediction or explanation.

Using evaluation information to choose the model or settings can make the final
check optimistic; this is **data leakage**. Learned preprocessing must also
respect the data roles. We use a simple split here to make those roles visible,
not to claim that one fixed proportion suits every dataset.



<span id="choose-the-next-activity"></span>

## Continue the guided introduction

**Previous chapter:** {doc}`../../sections/what-and-why`.

**Next chapter:** {doc}`Tasks, modes and capabilities <tasks_modes_capabilities>`. This sequence is for readers learning CE from the beginning; you can still use this page independently as a topic guide.

<!-- Entry-point tier: Tier 3. -->
