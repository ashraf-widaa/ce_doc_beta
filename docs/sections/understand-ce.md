# Learn Calibrated Explanations

Learn why Calibrated Explanations (CE) was developed, how its methods work, and
how to read the resulting predictions and explanations. This tutorial uses the
existing shared pages: one definition per topic, with code and captured outputs
where they help explain the idea.

Read in order the first time, or enter at your current question. You can read
the outputs without installing Python. When you run the concept chapters, keep
the same Iris session rather than repeating its setup. Numerical-target examples
show how value questions differ from event questions.

Prefer a result first? Use {doc}`Quick Start <../get-started/quickstart>` and return
here for the reasoning. The {doc}`Use CE guide <in-practice>` applies these ideas
to examples, your own data and software workflows.

(ce-what-why)=
## Part 1: what Calibrated Explanations is for

Begin with {doc}`What & Why <what-and-why>`, then distinguish data roles and
{doc}`tasks, modes and capabilities <../foundations/concepts/tasks_modes_capabilities>`.
A task describes the target, a mode the output question, and a capability an operation.

(how-ce-works)=
## Part 2: how the method works

Follow the {doc}`workflow overview <how-ce-works>` before the calibration and
explanation chapters. Keep this chain in mind:
**task → output question → method → reported quantity and range → assumptions**.
The overview also locates core and optional capabilities; the options are not
additional stages that everyone must enable.

## Read the shared chapters

```{include} ../_shared/guided-reading-map.md
```

## Connect theory to practice

Each chapter explains its concepts before the code, provides output to interpret,
and links to the next topic. Selected chapters offer a short check with an answer.
For a procedure on your own data, use {doc}`Use CE <in-practice>`; for exact calls
or architecture, use {doc}`Software Architecture & Integration <software-integration>`.

For formal statements, use {doc}`range meanings, assumptions and limits
<../foundations/concepts/calibrated_interval_semantics>`. Do not transfer one
mode's guarantee to another output or to a teaching game. The
{doc}`glossary <../glossary/index>` provides short shared definitions.

```{toctree}
:hidden:
:maxdepth: 2

CE: What & Why <what-and-why>
How CE Works <how-ce-works>
```
