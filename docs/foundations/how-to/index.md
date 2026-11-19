# How-to guides

Choose a guide for the operation you need. These recipes support existing
workflows; they do not need to be read in sequence.

- **Connect a model:** {doc}`integrate_with_pipelines`.
- **Configure execution:** {doc}`configure_runtime`, {doc}`safe-defaults` and {doc}`tune_runtime_performance`.
- **Present results:** {doc}`plot_with_plotspec`, {doc}`to_narrative` and {doc}`export_explanations`.
- **Inspect provenance:** {doc}`configure_telemetry`.
- **Use conditional calibration:** {doc}`conditional_calibration`.

For the meaning of an output, use the shared {doc}`interpretation guide <interpret_explanations>`.

## Related pages

- {doc}`Read CE explanations <interpret_explanations>`.

```{toctree}
:maxdepth: 1

Integrate with scikit-learn pipelines <integrate_with_pipelines>
Export explanations <export_explanations>
Configure telemetry <configure_telemetry>
Tune runtime performance (opt-in) <tune_runtime_performance>
Plot explanations with PlotSpec <plot_with_plotspec>
Configure runtime behaviour (ConfigManager) <configure_runtime>
Configure Conditional Calibration <conditional_calibration>
Safe defaults for production deployments <safe-defaults>
Generate narratives with `to_narrative` <to_narrative>
```
