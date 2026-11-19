# Quickstart

<span id="get-started"></span>

Start here to try CE with a small, reproducible example. You do not need to
read every concept or reference page before running a tutorial.

## Choose your first example

A classification model predicts a category; a regression model predicts a
numeric target. Choose the tutorial that matches your question:

| Your question | Start here |
| --- | --- |
| How do I explain a category prediction? | {doc}`Classification tutorial <quickstart_classification>`. |
| How do I explain a numeric prediction or ask about a threshold? | {doc}`Regression tutorial <quickstart_regression>`. It distinguishes numeric intervals from event probabilities. |
| I want to understand the ideas before coding | {doc}`CE: What & Why <../sections/what-and-why>`. |

## Follow one example through to interpretation

1. {doc}`Install the library <installation>` in the Python environment you will use.
2. Run your chosen tutorial in order. Keep model-fitting, calibration and
   evaluation data separate, as shown in its split.
3. Read the shared {doc}`interpretation guide <../foundations/how-to/interpret_explanations>`
   alongside the returned predictions and explanations. Reported ranges describe
   different quantities depending on the task and method.
4. To use your own model, continue to {doc}`pipeline integration <../foundations/how-to/integrate_with_pipelines>`.

For a browser-based introduction, try the [interactive demo](https://calibrated-explanations-demo.ju.se/).
It is illustrative; use the versioned references for supported behavior and
{doc}`method-specific assumptions and limits <../foundations/concepts/calibrated_interval_semantics>`.

## Continue at the depth you need

- **Understand the mechanism:** {doc}`How CE Works <../sections/how-ce-works>`.
- **Find more practical tasks:** {doc}`CE in Practice <../sections/in-practice>`.
- **Look up a call or solve a setup problem:** {doc}`CE Software & Integration <../sections/software-integration>`.
- **Filter explanations after the ordinary tutorial:** {doc}`guarded explanations <quickstart_guarded>`.

Entry-point tier: Tier 1.

## Related pages

- {doc}`Quick API <quick_api>`.
- {doc}`Environment troubleshooting <troubleshooting>`.

```{toctree}
:maxdepth: 1
:hidden:

Choose your task <../getting_started_60s>
```
