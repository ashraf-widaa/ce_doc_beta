# Predictive tasks and data roles

What is a model predicting, and which data can be used at each stage?
These definitions support Quickstart, conceptual introductions and practical guides.

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

## Choose the next activity

- **Run the example:** {doc}`Quickstart <../../get-started/index>`.
- **Follow the whole workflow:** {doc}`How CE Works <../../sections/how-ce-works>`.
- **Interpret results:** {doc}`../how-to/interpret_explanations`.
