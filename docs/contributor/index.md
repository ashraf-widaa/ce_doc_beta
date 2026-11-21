# Contributor hub

Use this hub to change code or docs without breaking CE semantics.

The authoritative public source, issue tracker, tags, releases, changelog, and
published documentation belong to
[`Moffran/calibrated_explanations`](https://github.com/Moffran/calibrated_explanations).

<span id="core-path"></span>

## Choose a contribution

Documentation work needs clear explanations and verified examples; a library
change also needs the relevant API and behavior checks. Start with a small,
well-defined goal. The official contribution policy and the
{doc}`pull request guide <../foundations/governance/pr_guide>` remain authoritative;
this hub explains how to find your way through them.

## 1. Understand the workflow and relevant components

Run or read {doc}`First explanation in Python <../get-started/first-python-explanation>`
to see the public lifecycle. Then use the
{doc}`architecture overview <../foundations/concepts/architecture>` to locate the
component responsible for the behavior you want to change. The
{doc}`API reference <../api/index>` describes public contracts; internal structures
are not automatically supported public interfaces.

## 2. Read the design decision before changing its boundary

Architecture Decision Records (ADRs) explain a software decision and its
constraints. They are not substitutes for scientific method papers or API
instructions. The relevant records are maintained under `development/adrs/` in
the repository; the architecture and plugin pages provide context before you
read them. For extension work, follow {doc}`plugin-contract`, then
{doc}`extending/guides/index`. A documentation correction does not require
learning every plugin contract.

## 3. Set up and make one focused change

Use {doc}`the contributor installation option <../get-started/installation>` in
your own checkout or fork; preserve existing work. Follow the active contribution
policy for branch setup and scope. For notebook examples, use
{doc}`notebook_policy`; introduce each cell, show verified outputs where useful,
and explain the results before moving on. Never fabricate expected values.

## 4. Check behavior, wording and review requirements

Run the checks appropriate to your change from the
{doc}`pull request guide <../foundations/governance/pr_guide>` and
{doc}`test policy <../foundations/governance/test_policy>`. Compare the result with
the intended behavior: a passing build does not verify a new statistical claim.
Preserve the {doc}`semantics reference <../foundations/concepts/calibrated_interval_semantics>`;
changes to scientific meaning need author review. The maintainer-only
`development/standards/STD-004-documentation-audience-standard.md` governs
user-facing documentation depth.

For method replication or unresolved scientific questions, continue to the
{doc}`Researcher Hub <../researcher/index>` and its research directions rather
than presenting an open proposal as a supported capability.

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
