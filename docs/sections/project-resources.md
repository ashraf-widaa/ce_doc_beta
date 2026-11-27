# CE Project, Vision & Evolution

<span class="ce-choice-page" hidden></span>

This path connects the CE methods to their publications, software development
and contribution process. Use it to understand the project, reproduce research
or find a focused way to participate. You do not need to complete it before
trying an explanation.

**For research:** {doc}`identify the papers <../citing>` →
{doc}`follow a replication workflow <../researcher/replication/index>`.
**For software contributions:** {doc}`understand the architecture <../foundations/concepts/architecture>` →
{doc}`use the Contributor Hub <../contributor/index>`. Choose the route matching your goal.

## Choose a project route

- **Investigate or reproduce a method:** start with the research section below,
  then enter the {doc}`Researcher Hub <../researcher/index>`.
- **Understand or change the implementation:** read how CE is developed, then
  enter the {doc}`Contributor Hub <../contributor/index>`.
- **Apply CE rather than study its development:** use {doc}`CE in Practice <in-practice>`
  or {doc}`Software & Integration <software-integration>`.

Follow the relevant route; these are different goals, not successive requirements.

## Understand the research behind the software

Begin with {doc}`Citing CE <../citing>` to identify the method and software
references. The {doc}`Researcher Hub <../researcher/index>` connects papers,
replication and implementation guidance. For formal background, continue to
{doc}`Theory and literature <../researcher/advanced/theory_and_literature>`.

Keep three things distinct: a published result under stated conditions, its
implementation in a particular software version, and an open research proposal.
The {doc}`semantics reference <../foundations/concepts/calibrated_interval_semantics>`
records output meanings and limitations; the
{doc}`roadmap <../ROADMAP>` describes plans rather than guaranteed availability.
Use {doc}`release references <../appendices/changelog_links>` for released changes.

## Understand how CE is developed

Read the {doc}`architecture overview <../foundations/concepts/architecture>`
for component responsibilities and execution paths. The
{doc}`Software & Integration path <software-integration>` starts with public
interfaces and application use. Together they connect what a user calls to the
components responsible for it.

The {doc}`Contributor Hub <../contributor/index>` then introduces contribution
options, relevant contracts and Architecture Decision Records (ADRs), setup and checks.
An ADR explains a software design choice; it is not a replacement for a statistical
paper or evidence that a capability has been validated for your data.

## Participate or find support

Start with a focused contribution: an unclear explanation, a reproducible defect,
a testable implementation change or a research question. Follow the project's
{doc}`governance and support pages <../foundations/governance/index>` and existing
contribution policy. Research directions belong in the researcher route until
they become implemented and documented capabilities.

The [official repository](https://github.com/Moffran/calibrated_explanations)
is the source for official code and issues. This site is an independent review
copy; feedback on these documentation changes belongs with the review team and
[review repository](https://github.com/ashraf-widaa/ce_doc_beta). These edits have
not been adopted into official CE by appearing here.

## Which hub should you open next?

The hubs organize material by goal. They are not five separate definitions of CE
or additional courses that everyone must complete.

| Your next goal | Start with | What to do there |
| --- | --- | --- |
| Inspect the workflow in a browser | {doc}`Expert Hub guide <../get-started/expert-hub>` | Follow preparation/calibration, then read one factual and alternative result. |
| Practise interpreting advice before a decision | {doc}`Decision Lab guide <../get-started/decision-lab>` | Read probabilities, costs and explanations; decide, then reflect on feedback. |
| Apply or extend a practical workflow | {doc}`Practitioner Hub <../practitioner/index>` | Choose a goal-specific tutorial/playbook after understanding one result. |
| Understand or reproduce research | {doc}`Researcher Hub <../researcher/index>` | Select the method/paper, inspect assumptions and follow its replication environment. |
| Change documentation or software | {doc}`Contributor Hub <../contributor/index>` | Locate the responsible component/policy, make a scoped change and run its checks. |

Use the documentation guide before opening an external app or repository: it
explains what to look for and where to continue. The official CE GitHub repository
holds source, issues and policies; the separate studies repository holds paper-specific
reproduction material. Follow a study's own README and version requirements,
not an invented universal reproduction command. The researcher route links it.
The review repository holds these independent documentation candidates.

For a continuous first introduction, begin with {doc}`What & Why <what-and-why>`
and follow its shared concept pages. For a specific software task, enter the relevant
hub directly; each guide states the context and prerequisites you need.

## Shared resources

- {doc}`Glossary <../glossary/index>`: short definitions linked to fuller explanations.
- {doc}`Historical terminology <../foundations/concepts/terminology>`: naming and compatibility changes.
- [BSD-3-Clause License](https://github.com/Moffran/calibrated_explanations/blob/main/LICENSE): open-source reuse terms.
- {doc}`Documentation map <../appendices/rtd_tier_map>`: maintenance context.

Commercial support is separate from the open-source library and its license;
see the {doc}`homepage <../index>`. For a first hands-on result instead, start with
{doc}`Quick Start <../get-started/index>`.

```{toctree}
:maxdepth: 1
:hidden:

Research and reproduction <../researcher/index>
Contribute to CE <../contributor/index>
Citing calibrated-explanations <../citing>
Project roadmap <../ROADMAP>
Glossary <../glossary/index>
Naming and compatibility terms <../foundations/concepts/terminology>
Governance & support <../foundations/governance/index>
RTD tier map <../appendices/rtd_tier_map>
```

<!-- Entry-point tier: Tier 1. -->

<!-- Preserve earlier section links. -->
<span id="follow-development-or-participate"></span>
<span id="understand-the-project-and-research"></span>
