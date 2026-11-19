# Learn through a decision

Use this route to ask what a prediction contributes to a decision with costs
and consequences. Decision Lab and Expert Hub have different learning goals;
you do not need to complete both.

The [Decision Lab](https://games.grejna.ai/) hosts teaching games. Its current
lessons and selected scenarios were inspected on 19 November 2026. The games
identify CE-E model services; this is not evidence that every scenario exposes
every feature or has the same guarantees as the CE Python library.

## First choice: a guided classification decision

Open [Explanations and alternatives need interpretation](https://games.grejna.ai/learn/explanations-alternatives),
then the level-4 **Open guided exercise**, or
[open that guided Mission Control exercise directly](https://games.grejna.ai/learn/mission/l4?from=explanations-alternatives).
Guided practice does not require campaign upgrade purchases.

1. Read **MISSION FILE**, including success reward and failure costs.
2. Inspect **CHANCE OF SUCCESS** and **COULD BE ANYWHERE IN**.
3. Form a provisional **GO** or **STOP** choice before acting.
4. Open the action button **WHY?** (shortcut **W**), distinct from the small
   learning-note icon. Compare feature conditions, signed contributions and
   their own ranges with the overall assessment.
5. Make your own **GO** or **STOP** choice, then inspect the feedback and score.

```{figure} browser_assets/mission-why.png
:alt: Actual guided Mission Control screen with a mission file, success probability and range, WHY conditions and GO STOP actions.
:width: 100%

Compare the overall assessment with the conditions supporting it before choosing. The screenshot is a real captured practice case; your case can differ.
```

One tested mission displayed 38%, range 36–39%, and the tested launch succeeded.
That single outcome does not show that calibration failed: low-probability
outcomes can happen. The next mission had different conditions and an assessment
of 92%, range 92–95%. Do not treat a single success as deployment validation.

Ask: would you choose the same action at both ends of the reported range?
What relevant evidence is missing? Does a WHY contribution describe the model,
or establish a real-world cause?

Guided level 5 is linked for alternatives, but was not completed in this review.
Level 4's WHY exercise is not a verified alternative-explanation walkthrough.
For that capability, use the tested {doc}`Expert Hub route <expert-hub>`.

## Numeric decisions: Precision Works

Open [Precision Works](https://games.grejna.ai/games/precision-works).
It is labelled **preview** and concerns **realized batch mean hardness in HRC**,
not the quality of every individual part.

1. Select **Enter factory**, then **Characterisation batch**.
2. Keep the preset recipe and select **Assess recipe**.
3. Read **Median prediction** and the conformal interval. One captured trial
   showed 57.2 HRC with a 90% interval 56.2–58.6 HRC.
4. Open **Why?**, then **What could we change?**. Compare a model alternative
   with the costs and constraints of a concrete recipe change.
5. Decide whether to **Run batch**, then inspect realized outcome and financial
   feedback. Changes can alter costs and operating conditions; no single batch
   establishes calibration or an intervention guarantee.

```{figure} browser_assets/precision-forecast.png
:alt: Actual Precision Works recipe controls and process advisor showing numeric hardness prediction and HRC interval.
:width: 100%

Read the target and units first: the interval concerns batch mean hardness. Individual-part quality costs are a separate quantity.
```

In the tested alternative panel, `Furnace temperature > 860` reported
58.8 HRC (57.8–60.2), while the UI separately suggested a concrete setting
change and its cost. The condition and the executable action are not identical.

## Ask an event question instead

The same game offers other contracts:

| Contract | Event / quantity | Observed selected-recipe result |
| --- | --- | --- |
| Heavy-duty shafts / LIMIT | Probability that batch mean Y > 58 HRC | 14%, bounds 0–17%. |
| Aerospace precision lot / TOLERANCE | Probability that 58 < batch mean Y ≤ 62 HRC | 13%, bounds 0–14%. |

These are probabilistic-regression questions. A two-ended event is not the same
as asking for a numeric prediction interval. Both prediction displays worked;
the event-specific explanation panels were not fully tested in this review.
For a tested event factual/alternative route, use {doc}`Expert Hub <expert-hub>`.

## Other scenarios and limits

Uncertain Acres and Port Authority are linked from the current home page.
Their entry screens were inspected, but no full advisor/decision cycle was
completed here. Do not infer their CE modes from another game's support.

These are simulated learning environments. Their stated long-run assumptions,
preview status and limitations remain relevant even when an action succeeds.

**Continue:** {doc}`Quickstart <index>` to change route;
{doc}`explanation construction <../foundations/concepts/how_explanations_are_built>`
for mechanisms; {doc}`checking results <../practitioner/check_results>` for
independent evaluation; {doc}`first Python explanation <first-python-explanation>`
for the library workflow.
