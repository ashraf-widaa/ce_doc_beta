# Contributor hub

Use this hub to change code or docs without breaking CE semantics.

The authoritative public source, issue tracker, tags, releases, changelog, and
published documentation belong to
[`Moffran/calibrated_explanations`](https://github.com/Moffran/calibrated_explanations).

## Core path

1. Read {doc}`plugin-contract`.
2. Use {doc}`extending/guides/index` for implementation workflows.
3. Run checks from {doc}`../foundations/governance/pr_guide` and
   {doc}`../foundations/governance/test_policy`.
4. Use `development/standards/STD-004-documentation-audience-standard.md` (maintainer-only docs set) for docs
   structure and semantics-layer requirements.

Contributor-facing semantics references:
- {doc}`../foundations/concepts/calibrated_interval_semantics`
- `development/adrs/ADR-021-calibrated-interval-semantics.md` (maintainer-only docs set)
- `development/adrs/ADR-026-explanation-plugin-semantics.md` (maintainer-only docs set)


Entry-point tier: Tier 1.

## Related pages

- {doc}`Migration guides <../migration/index>`.

```{toctree}
:maxdepth: 1
:hidden:

CE-First Calibrated Explanations Guide (OSS) <../get-started/ce_first_agent_guide>
AI Agent Setup Guide for `calibrated_explanations` <../get-started/copilot-setup>
Plugin contract <plugin-contract>
Notebook Policy for `calibrated_explanations` <notebook_policy>
Performance Harness <performance_harness>
Reject Policy Usage <reject_policy_usage>
Advanced plugin wiring and configuration <extending/plugin-advanced-contract>
Extending guides <extending/guides/index>
Advanced contributor tooling <extending/advanced>
Agent skill catalogue <agent_skills>
```
