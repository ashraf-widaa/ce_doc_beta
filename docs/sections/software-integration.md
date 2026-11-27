# Software Architecture & Integration

<span id="ce-software-integration"></span>

<span class="ce-choice-page" hidden></span>

Use this path to add CE to a Python application and preserve the meaning of its
outputs as they move through your system. Start with the public interface;
internal architecture and plugin contracts become relevant when you need to
understand or extend the implementation.

## Choose your software goal

- **Integrate CE into an application:** start with
  {doc}`one Python example <../get-started/first-python-explanation>`, use
  {doc}`Quick API <../get-started/quick_api>` to select calls, then follow
  {doc}`pipeline integration <../foundations/how-to/integrate_with_pipelines>`.
- **Understand or extend the codebase:** start with
  {doc}`architecture and execution flow <../foundations/concepts/architecture>`,
  then use the {doc}`Contributor Hub <../contributor/index>` for design records,
  extension contracts and the contribution process. You can skip the first-run
  material below if you already know the public workflow.

These are different goals, not two compulsory stages. The statistical definitions
remain in {doc}`How CE Works <how-ce-works>` and its shared chapters.

## First, run the public workflow

Follow {doc}`First explanation in Python <../get-started/first-python-explanation>`
for installation, explained code, expected output and a plot. If you already
have an environment, {doc}`Quick API <../get-started/quick_api>` maps your question
to a call. Use {doc}`Installation <../get-started/installation>` for package options.

The public wrapper, `WrapCalibratedExplainer`, coordinates the lifecycle: use a
fitted predictive model, calibrate with separate labelled data, then predict or
explain a new case. Prediction and explanation use the fitted model with CE calibration; a separate prediction call is not required before an explanation.

(ce-wrapper-workflow-map)=
## Follow the numbered wrapper workflow

The figure maps each activity to its software entry point. It distinguishes
what is known in the data from what is supplied to a call: test targets are
known but withheld for evaluation; a new case's target may be unknown.

```{include} ../_shared/wrapper-figure.md
```

For exact calls and output questions, use {doc}`Quick API <../get-started/quick_api>`.
Optional functions have a separate {ref}`concept-to-software map <optional-capability-api-map>`;
start with ordinary calls before choosing an option.

## Follow the integration sequence

| Stage | Use this guide | What you should achieve |
| --- | --- | --- |
| Install and run | {doc}`Installation <../get-started/installation>` and {doc}`First explanation in Python <../get-started/first-python-explanation>` | A working environment and one interpreted result. |
| Select the interface | {doc}`Quick API <../get-started/quick_api>` | Identify the call, inputs and returned quantity. |
| Connect preprocessing | {doc}`Pipeline integration <../foundations/how-to/integrate_with_pipelines>` | Consistent feature transformations across data roles. |
| Pass results onward | {doc}`Export explanations <../foundations/how-to/export_explanations>` | Preserve quantities, units and reported ranges. |
| Configure and maintain | {doc}`Runtime configuration <../foundations/how-to/configure_runtime>` and {doc}`Troubleshooting <../get-started/troubleshooting>` | Understand configuration and investigate failures. |

Read the following sections alongside those guides. The shared
{doc}`calibration chapter <../foundations/concepts/calibration_background>` explains
the statistical mechanism when you need it; this route concentrates on using it in software.

## Connect your model and preprocessing

Keep feature order, types and transformations consistent across fitting,
calibration and queries. Follow
{doc}`Integrate with pipelines <../foundations/how-to/integrate_with_pipelines>`
for preprocessing rather than applying unrelated transformations in different
parts of the workflow.

Before integrating a method, check its inputs and return values in the
{doc}`API reference <../api/index>`. The lower-level `CalibratedExplainer` reference
is useful for implementation detail; it does not replace the wrapper tutorial's
data roles or the version-specific public contract.

## Preserve the meaning of returned results

Name the output mode, quantity and units before displaying or exporting it.
A target-value interval must not be labelled as probability bounds; a factual
weight must not be displayed as the case's predicted probability. Preserve the
reported ranges and warnings rather than clipping values to fit a display.

Use {doc}`Interpret calibrated explanations <../foundations/how-to/interpret_explanations>`
for the objects and plots. The
{doc}`integration and operations guides <../foundations/how-to/index>` connect
those results to export, configuration and runtime behavior. A correctly shaped
array does not by itself establish statistical validity; evaluate using
{doc}`Checking results <../practitioner/check_results>` and the
{doc}`mode-specific conditions <../foundations/concepts/calibrated_interval_semantics>`.

## Find the exact interface or output contract

| What you need now | Shared reference |
| --- | --- |
| Class, method, inputs and returns | {doc}`API reference <../api/index>` |
| Parameter meaning and default | {doc}`Parameter reference <../foundations/concepts/parameter-reference>` |
| Saved output structure | {doc}`Explanation schema <../schema_v1>` |
| Exception and validation behavior | {doc}`Errors and validation <../foundations/concepts/error_handling>` |

Use the reference for an exact contract after the worked example has shown what
the returned quantity means. The schema describes structure; it does not establish
statistical validity or prescribe an application decision.

## Handle errors and version changes

When a call fails, keep the exact message and record your environment and package
version. {doc}`Troubleshooting <../get-started/troubleshooting>` is the first stop;
the API contract explains accepted parameters and returns.

Before upgrading, use the {doc}`upgrade guides <../upgrade/index>`,
{doc}`migration guides <../migration/index>` and
{doc}`release references <../appendices/changelog_links>`. A version change can
affect interfaces or interpretation; do not assume an older screenshot defines
the current contract.

## Understand or extend the implementation

The {doc}`architecture overview <../foundations/concepts/architecture>` explains
components and execution paths before internal details. For extension work,
continue to {doc}`plugins <../plugins>`, the
{doc}`technical reference <../foundations/reference/index>` and the
{doc}`Contributor Hub <../contributor/index>` for contracts, relevant design
records and checks. Architecture Decision Records explain design choices;
scientific guarantees still need their method and assumptions.

**Need the statistical construction?** Follow {doc}`How CE Works <how-ce-works>`.
**Need another worked task?** Return to {doc}`CE in Practice <in-practice>`.

```{toctree}
:maxdepth: 1
:hidden:

Installation <../get-started/installation>
Quick API <../get-started/quick_api>
API Reference <../api/index>
Integration and operations guides <../foundations/how-to/index>
Environment troubleshooting <../get-started/troubleshooting>
Upgrade guides <../upgrade/index>
Migration guides <../migration/index>
Release notes <../appendices/changelog_links>
Plugins <../plugins>
Technical reference and internals <../foundations/reference/index>
```

<!-- Entry-point tier: Tier 1. -->

<!-- Preserve earlier section links. -->
<span id="choose-how-far-into-the-software-to-go"></span>
<span id="install-integrate-or-look-up-a-call"></span>
<span id="maintain-or-extend-an-integration"></span>
<span id="maintain-or-extend-the-software"></span>
<span id="start-with-the-public-lifecycle"></span>

<!-- Preserve section links from earlier review versions. -->
<span id="follow-the-software-guide-alongside-the-concepts"></span>
