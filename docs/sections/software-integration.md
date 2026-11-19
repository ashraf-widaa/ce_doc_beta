# CE Software & Integration

<!-- Preserve descriptive anchors from the previous review layout. -->
<span id="install-integrate-or-look-up-a-call"></span>
<span id="maintain-or-extend-an-integration"></span>


How do you connect CE to your model, find an exact call and maintain the
integration? This route is the technical guide; it does not require reading
the internal architecture before using the public API.

## Start with the public lifecycle

The tutorials use `WrapCalibratedExplainer`: fit the predictive model, calibrate
with separate labelled data, then predict or explain. The underlying
`CalibratedExplainer` interface is a lower-level reference, not a replacement
for following the wrapper tutorial's data roles.

| Your task | Guide | What to verify |
| --- | --- | --- |
| Install the package | {doc}`Installation <../get-started/installation>`. | Python environment and required extras. |
| Run the lifecycle end to end | {doc}`First Python explanation <../get-started/first-python-explanation>`. | Fitting/calibration roles and a real returned result. |
| Find a public method | {doc}`Quick API <../get-started/quick_api>` and {doc}`API reference <../api/index>`. | Inputs, output mode, shapes and version-specific returns. |
| Integrate preprocessing | {doc}`Pipeline integration <../foundations/how-to/integrate_with_pipelines>`. | Consistent feature representation across all data roles. |
| Configure execution or present results | {doc}`Integration and operations guides <../foundations/how-to/index>`. | Configuration authority and selected capabilities. |
| Resolve an error | {doc}`Troubleshooting <../get-started/troubleshooting>`. | Exact message, environment, versions and raw output. |

A probability-like array does not by itself establish a statistical guarantee.
Use the shared {doc}`interpretation guide <../foundations/how-to/interpret_explanations>`
for output meanings and {doc}`checking results <../practitioner/check_results>`
for held-out evaluation. Keep warnings visible while integrating.

## Maintain or extend the software

Use {doc}`release notes <../appendices/changelog_links>`,
{doc}`upgrade guides <../upgrade/index>` and {doc}`migration guides <../migration/index>`
when changing versions. For plugin work or internal implementation details,
use {doc}`plugins <../plugins>` and
{doc}`technical reference and internals <../foundations/reference/index>`.

**Learn by task:** {doc}`CE in Practice <in-practice>`.
**Understand construction:** {doc}`How CE Works <how-ce-works>`.
**Find project/research context:** {doc}`Project & Resources <project-resources>`.

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
