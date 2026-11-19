# CE in Practice

What do you want to do with CE? Choose one task, run the example and use the
shared interpretation guide to understand the result.

## Choose a practical route

| Your goal | Start | Continue |
| --- | --- | --- |
| Run CE for the first time | {doc}`Quickstart <../get-started/index>` | The tutorial for your task. |
| Explain a category prediction | {doc}`Classification tutorial <../get-started/quickstart_classification>` | {doc}`Read the explanation <../foundations/how-to/interpret_explanations>`. |
| Explain a numeric prediction or threshold event | {doc}`Regression tutorial <../get-started/quickstart_regression>` | The same interpretation guide, using the meaning for your mode. |
| Use an existing model or preprocessing pipeline | {doc}`Pipeline integration <../foundations/how-to/integrate_with_pipelines>` | {doc}`API reference <../api/index>` for exact inputs and returns. |

## Build on the ordinary example

After a first explanation, use {doc}`guarded explanations <../get-started/quickstart_guarded>`
if that filtering is relevant, or explore {doc}`practitioner playbooks <../practitioner/playbooks/index>`
for more specific workflows. These are optional next choices.

The {doc}`task map <../tasks/index>` helps distinguish output modes. The
{doc}`practitioner hub <../practitioner/index>` collects advanced practical material.

One worked example does not establish validity for another dataset or deployment.
Check the {doc}`method-specific assumptions and limits <../foundations/concepts/calibrated_interval_semantics>`
when interpreting results on your data.

**Understand why an output has that meaning:** {doc}`How CE Works <how-ce-works>`.
**Configure or troubleshoot the library:** {doc}`CE Software & Integration <software-integration>`.

```{toctree}
:maxdepth: 1
:hidden:

Classification tutorial <../get-started/quickstart_classification>
Regression tutorial <../get-started/quickstart_regression>
Guarded explanations (advanced) <../get-started/quickstart_guarded>
Tasks and capabilities <../tasks/index>
Practitioner hub <../practitioner/index>
```
