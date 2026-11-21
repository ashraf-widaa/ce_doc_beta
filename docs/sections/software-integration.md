# CE Software & Integration

<span class="ce-choice-page" hidden></span>

Use this path to add CE to a Python application and preserve the meaning of its
outputs as they move through your system. Start with the public interface;
internal architecture and plugin contracts become relevant when you need to
understand or extend the implementation.

## First, run the public workflow

Follow {doc}`First explanation in Python <../get-started/first-python-explanation>`
for installation, explained code, expected output and a plot. If you already
have an environment, {doc}`Quick API <../get-started/quick_api>` maps your question
to a call. Use {doc}`Installation <../get-started/installation>` for package options.

The public wrapper, `WrapCalibratedExplainer`, coordinates the lifecycle: use a
fitted predictive model, calibrate with separate labelled data, then predict or
explain a new case. Prediction and explanation are operations on the calibrated
system; a separate prediction call is not required before an explanation.

## Follow the software guide alongside the concepts

The practical sequence is {doc}`the complete Python example <../get-started/first-python-explanation>` →
{doc}`Quick API <../get-started/quick_api>` →
{doc}`pipeline integration <../foundations/how-to/integrate_with_pipelines>` →
{doc}`runtime configuration <../foundations/how-to/configure_runtime>` and
{doc}`troubleshooting <../get-started/troubleshooting>` as needed. Each destination
has a different job: obtain a result, find a call, connect preprocessing, then
operate the configured system. Use the shared
{doc}`calibration chapter <../foundations/concepts/calibration_background>` when you
need the mechanism; implementation documentation should not redefine its theory.

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
