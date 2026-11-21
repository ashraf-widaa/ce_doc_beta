# Researcher hub

<span class="ce-choice-page" hidden></span>

Use this hub for replication and method-focused analysis.

Begin with a concrete result in {doc}`Quick Start <../get-started/index>` if CE
is new to you. The {doc}`How CE Works path <../sections/how-ce-works>` connects
outputs to construction; this hub then guides replication and research.

## Move from a question to a reproducible study

First identify the question and reported quantity. Use the
{doc}`shared calibration chapter <../foundations/concepts/calibration_background>`
and {doc}`explanation construction <../foundations/concepts/how_explanations_are_built>`
for the conceptual and runnable background. Then select the relevant paper from
{doc}`the maintained citation list <../citing>`, check its method and assumptions,
and follow the study-specific replication instructions. This keeps tutorial
intuition, formal results and an implementation experiment distinct.

## Core path

1. Follow {doc}`replication/index`.
2. Use {doc}`../foundations/concepts/calibrated_interval_semantics` for formal
   semantics and non-guarantees.
3. Use {doc}`advanced/theory_and_literature` for papers and benchmark context.

## Connect methods to the implementation

Use {doc}`Architecture <../foundations/concepts/architecture>` to locate runtime
responsibilities and {doc}`the API reference <../api/index>` for supported
interfaces. An ADR explains an implementation decision; scientific claims need
the corresponding method, assumptions and paper. A successful reproduction is
evidence about that experiment, not a universal guarantee.

To contribute an implementation or documentation change, continue through the
{doc}`Contributor Hub <../contributor/index>` for setup and validation policy.

## Open questions

Track unresolved questions in {doc}`future_work`.


Entry-point tier: Tier 1.

```{toctree}
:maxdepth: 1
:hidden:

Replication workflow <replication/index>
Researcher advanced topics <advanced/index>
Research Directions <future_work>
```
