(calibrated-explanations-documentation)=

# Calibrated Explanations

<div class="ce-home-review">Independent review documentation · Based on CE 1.0.2. <a href="https://calibrated-explanations.readthedocs.io/en/stable/">Visit the official documentation</a>.</div>

<div class="ce-home-intro">
<p class="ce-home-lead">Understand predictions with Calibrated Explanations.</p>
<p>Calibrated Explanations (CE) works with a trained machine-learning model and separate calibration data to provide calibrated prediction information and feature explanations. It supports classification and regression; the meaning of its reported ranges depends on the task and method.</p>
<div class="ce-home-actions"><a class="ce-home-primary" href="get-started/index.html">Start with Quick Start <span aria-hidden="true">→</span></a><a class="ce-home-secondary" href="sections/what-and-why.html">New to CE? Understand the ideas</a></div>
<p>Read a result without running code, then choose the browser or Python route.</p>
</div>

## Documentation

Choose one route for your goal. Quick Start gives you a first result; the four
routes below help you understand, apply or integrate it at the depth you need.

<div class="ce-home-grid" role="navigation" aria-label="Documentation sections">
<a class="ce-home-card" href="sections/what-and-why.html"><span class="ce-home-card-title">CE: What &amp; Why</span><span class="ce-home-card-description">Learn why CE was developed, what it adds to a prediction, and when its explanations help.</span><span class="ce-home-card-action">Understand CE <span aria-hidden="true">→</span></span></a>
<a class="ce-home-card" href="sections/how-ce-works.html"><span class="ce-home-card-title">How CE Works</span><span class="ce-home-card-description">Learn the construction: data roles, calibration, explanation weights and task-specific assumptions.</span><span class="ce-home-card-action">Explore the method <span aria-hidden="true">→</span></span></a>
<a class="ce-home-card" href="sections/in-practice.html"><span class="ce-home-card-title">CE in Practice</span><span class="ce-home-card-description">Run a worked example, interpret its output, then adapt and evaluate the workflow.</span><span class="ce-home-card-action">Try an example <span aria-hidden="true">→</span></span></a>
<a class="ce-home-card" href="sections/software-integration.html"><span class="ce-home-card-title">CE Software &amp; Integration</span><span class="ce-home-card-description">Install CE, connect your model and preprocessing, then configure and maintain an integration.</span><span class="ce-home-card-action">Use the library <span aria-hidden="true">→</span></span></a>
</div>

Each route links to the same shared concept and interpretation pages. You can
switch routes when your question changes; you do not need to complete them all.
For a continuous concept tutorial, use the {ref}`shared reading map <guided-reading-route>`.
Already familiar with SHAP or LIME? {doc}`Compare the questions and outputs <compare>`.

## Project & Resources

Find the research, terminology and open-source project.

<div class="ce-home-grid ce-home-resources" role="navigation" aria-label="Project and resources">
<a class="ce-home-card" href="sections/project-resources.html"><span class="ce-home-card-title">CE Project, Vision &amp; Evolution</span><span class="ce-home-card-description">Connect the research, software architecture and development process; find a way to contribute.</span><span class="ce-home-card-action">Explore the project <span aria-hidden="true">→</span></span></a>
<a class="ce-home-card" href="glossary/index.html"><span class="ce-home-card-title">Glossary</span><span class="ce-home-card-description">Shared scientific and software terms, with links for depth.</span><span class="ce-home-card-action">Find a definition <span aria-hidden="true">→</span></span></a>
<a class="ce-home-card" href="https://github.com/Moffran/calibrated_explanations"><span class="ce-home-card-title">GitHub Repository</span><span class="ce-home-card-description">Official source code, issues and releases.</span><span class="ce-home-card-action">Visit GitHub <span aria-hidden="true">→</span></span></a>
<a class="ce-home-card" href="https://github.com/Moffran/calibrated_explanations/blob/main/LICENSE"><span class="ce-home-card-title">BSD-3-Clause License</span><span class="ce-home-card-description">The open-source library’s license and reuse terms.</span><span class="ce-home-card-action">Read the license <span aria-hidden="true">→</span></span></a>
</div>

<details class="ce-home-details"><summary>Version information and more resources</summary>

The public API, plugin trust model, and visualization extension contract are
stable as of `1.0.0`; only patch-level defect fixes will be accepted against
these contracts going forward. This notice describes the official release line;
this website is an independent documentation review copy.
Before adoption, review the {doc}`v1.0.0 upgrade checklist <upgrade/v1.0.0-upgrade-checklist>`,
{doc}`Explanation Schema v1 freeze <schema_v1>` and
[release notes](https://github.com/Moffran/calibrated_explanations/blob/main/CHANGELOG.md).
For published package setup, use {doc}`installation <get-started/installation>`
and [PyPI](https://pypi.org/project/calibrated-explanations/).

Try the [interactive web demo](https://calibrated-explanations-demo.ju.se/)
without installing the library. The demo is illustrative; supported APIs,
behavior, assumptions and guarantees are documented in the versioned references.
For simulated learning scenarios, [explore Decision Labs](https://games.grejna.ai/).

<span id="companion-projects"></span>

Use {doc}`plugins` for companion extensions and
{doc}`researcher/replication/index` to reproduce studies in their version-specific
environments. Direct routes remain available for {doc}`practitioners <practitioner/index>`,
{doc}`researchers <researcher/index>` and {doc}`contributors <contributor/index>`.
The {doc}`documentation map <appendices/rtd_tier_map>` supports maintainers.
The {doc}`shared foundations <foundations/index>` support every learning route.

</details>

## Commercial Services

Calibrated Explanations is an independent, BSD-licensed open-source project.
For optional commercial integration, operational deployment or pilot discussions,
[visit Grejna AB](https://grejna.ai/?utm_source=ce_docs&utm_medium=referral&utm_campaign=ce_ecosystem).
These services are separate from the open-source library and its license.







<!-- Entry-point tier: Tier 1. -->

```{toctree}
:maxdepth: 1
:hidden:

Home <self>
Quick Start <get-started/index>
CE: What & Why <sections/what-and-why>
How CE Works <sections/how-ce-works>
CE in Practice <sections/in-practice>
CE Software & Integration <sections/software-integration>
Project & Resources <sections/project-resources>
```
