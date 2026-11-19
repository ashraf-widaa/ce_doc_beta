# Glossary

Short definitions support every reading route. Follow a topic link for depth;
the source-version semantics page owns formal guarantees and non-guarantees.
Use your browser's find command to locate a term.

## Prediction and data

- **Observation / case:** one example described by input features.
- **Feature:** an input describing a case.
- **Target:** the outcome the model is trained to predict.
- **Calibration data:** separate labelled data used by the calibration procedure.
- **Evaluation data:** held-out outcomes used to check results after fitting and calibration.

Read the shared {doc}`predictive tasks and data roles <../foundations/concepts/predictive_tasks>`.

## Tasks, modes and statistical quantities

- **Classification:** prediction of a categorical target.
- **Regression:** prediction concerning a numeric target.
- **CE mode:** the output question: class-probability information, numeric prediction interval or numeric-event probability.
- **Capability:** an operation such as prediction, factual explanation or alternative explanation.
- **Probability calibration:** the relationship between probability reports and outcome frequencies.
- **Prediction interval:** an interval for the numeric target, read in its units under the method's conditions.
- **Exchangeability:** symmetry of a joint distribution under reordering; an assumption used by relevant statistical constructions.

Continue with the {doc}`task/mode map <../foundations/concepts/tasks_modes_capabilities>`
or {doc}`calibration and statistical background <../foundations/concepts/calibration_background>`.

## Explanations and ranges

- **Factual explanation:** conditions holding for the query, with reported feature weights and ranges.
- **Alternative explanation:** prediction information under a different feature condition.
- **Feature weight:** a quantity comparing model responses; its units depend on the explained output.
- **Reported range:** a generic description that needs its quantity identified: probability, target value or feature weight.

Read {doc}`how explanations are built <../foundations/concepts/how_explanations_are_built>`
and the {doc}`canonical interval semantics <../foundations/concepts/calibrated_interval_semantics>`.

## Software and naming

- **Public wrapper:** `WrapCalibratedExplainer`, the public fit/calibrate/predict/explain interface used by tutorials.
- **Parameter:** an input controlling a call; its name, type and default belong in the API reference.

Use {doc}`Quick API <../get-started/quick_api>` and the
{doc}`parameter reference <../foundations/concepts/parameter-reference>` for exact names.
For historical naming changes and compatibility terms, keep using the existing
{doc}`terminology reference <../foundations/concepts/terminology>`.
