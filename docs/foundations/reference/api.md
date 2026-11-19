# API reference

Core modules are documented automatically via Sphinx autosummary.





## Parameter aliases and configuration

`calibrated_explanations.api.params.reject_removed_aliases` rejects removed
aliases (for example `alpha`/`alphas`, `n_jobs`) and raises
`ConfigurationError` with canonical replacements.

`calibrated_explanations.api.config.ExplainerConfig` and the accompanying
builder expose the public typed configuration surface. Construct a configured
wrapper with `WrapCalibratedExplainer.from_config(config)`; the removed private
`_from_config` helper is not part of the v1 API.

```{toctree}
:maxdepth: 1

../../_autosummary/calibrated_explanations.core.CalibratedExplainer
../../_autosummary/calibrated_explanations.core.WrapCalibratedExplainer
../../_autosummary/calibrated_explanations.explanations.CalibratedExplanations
../../_autosummary/calibrated_explanations.explanations.AlternativeExplanations
../../_autosummary/calibrated_explanations.explanations.CalibratedExplanation
../../_autosummary/calibrated_explanations.explanations.FactualExplanation
../../_autosummary/calibrated_explanations.explanations.AlternativeExplanation
../../_autosummary/calibrated_explanations.explanations.FastExplanation
../../_autosummary/calibrated_explanations.utils.helper
../../_autosummary/calibrated_explanations.core.exceptions
../../_autosummary/calibrated_explanations.core.validation
../../_autosummary/calibrated_explanations.api.params
../../_autosummary/calibrated_explanations.api.config
```
