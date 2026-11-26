"""Regenerate CE lifecycle and task maps with consistent data-role terminology.

Run from any directory: python scripts/docs/generate_workflow_figures.py
SVGs have transparent canvases, white ML/input boxes and orange CE boxes.
These are conceptual figures, not a specification of an API call sequence.
"""

from __future__ import annotations

from pathlib import Path
import html

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / "docs/_static/figures"


class Diagram:
    def __init__(self, w, h, title, desc):
        self.inbox = False
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{html.escape(title)}</title><desc id="desc">{html.escape(desc)}</desc><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#64748b"/></marker></defs>'
        ]

    def text(self, x, y, t, size=19, bold=False, anchor="middle", color="#334155"):
        if not self.inbox:
            # White pill keeps free-standing labels legible on transparent canvases
            # in both light and dark themes.
            bw = min(1080, len(t) * size * 0.57 + 18)
            left = x - 9 if anchor == "start" else x - bw / 2
            self.parts.append(
                f'<rect x="{left}" y="{y - size}" width="{bw}" height="{size + 9}" rx="5" fill="#ffffff"/>'
            )
        self.parts.append(
            f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}">{html.escape(t)}</text>'
        )

    def box(self, x, y, w, h, title, lines=(), ce=False):
        self.parts.append(
            f'<g class="node"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{"#ffedd5" if ce else "#ffffff"}" stroke="{"#c2410c" if ce else "#64748b"}" stroke-width="2"/>'
        )
        self.inbox = True
        n = len(lines)
        first = y + (h - (24 + n * 24)) / 2 + 21
        self.text(x + w / 2, first, title, 21, True, color="#9a3412" if ce else "#1e293b")
        for i, t in enumerate(lines):
            self.text(x + w / 2, first + (i + 1) * 24, t, 18)
        self.parts.append("</g>")
        self.inbox = False

    def arrow(self, path, dashed=False):
        dash = 'stroke-dasharray="7 5"' if dashed else ""
        self.parts.append(
            f'<path d="{path}" fill="none" stroke="#64748b" stroke-width="2.5" stroke-linejoin="round" {dash} marker-end="url(#arrow)"/>'
        )

    def head(self, y, t, w):
        self.box(12, y, w - 24, 48, t)

    def save(self, name):
        (DEST / name).write_text(
            "\n".join(self.parts) + "\n</svg>\n", encoding="utf-8", newline="\n"
        )


MODES = {
    "classification": (
        "Classification: binary or multiclass",
        "Fit a classifier",
        "Venn–Abers construction",
        ["Class probabilities + bounds", "Check the named class."],
        [
            "Factual: probability differences",
            "Alternatives: class probabilities",
            "Each with a reported range",
        ],
    ),
    "interval": (
        "Regression: value and interval",
        "Fit a regressor",
        "Conformal predictive system",
        ["Value + target-value interval", "Read in the target’s units."],
        [
            "Factual: target-unit differences",
            "Alternatives: numerical values",
            "Each with a reported range",
        ],
    ),
    "event": (
        "Regression: event probability",
        "Fit a regressor",
        "CPS scores + Venn–Abers",
        ["Event probability + bounds", "For example: P(Y ≤ t)."],
        [
            "Factual: probability differences",
            "Alternatives: event probabilities",
            "Each with a reported range",
        ],
    ),
}


def workflow(stem, m=False, slug=None):
    w = 360 if m else 1100
    h = 1900 if m else 1110
    title = MODES[slug][0] if slug else "From model development to a new CE case"
    desc = "Prepare the fitted predictive model using training features and targets. Separate labelled calibration data configure CE around that same model. Evaluate by querying held-out test features and comparing outputs with held-out targets; test targets do not enter prediction or explanation. At inference, reuse the same fitted model and CE calibration state with new-case features; no query target is needed. Calibration state and reference data remain part of the CE system. White denotes conventional inputs and activities; orange denotes CE additions. Arrows show information flow, not required API calls. Range meanings and guarantees depend on the selected method and its conditions."
    d = Diagram(w, h, title, desc)
    fit = MODES[slug][1] if slug else "Fit the predictive model"
    method = MODES[slug][2] if slug else "Configure CE"
    pred = (
        MODES[slug][3] if slug else ["Probability or numerical value", "With a mode-specific range"]
    )
    expl = (
        MODES[slug][4]
        if slug
        else ["Factual: weights + ranges", "Alternatives: predictions + ranges"]
    )
    if m:
        d.head(12, "1 · Prepare — development", w)
        # Information flow precedes filled boxes.
        for p in [
            "M180 157V187",
            "M180 413V443",
            "M180 775V805",
            "M180 1383V1413",
            "M180 1525V1555",
        ]:
            d.arrow(p)
        d.arrow("M338 237H350V499H338")
        d.arrow("M22 854H9V1080H22")
        d.box(22, 80, 316, 77, "Training data", ["Features + known targets"])
        d.box(22, 187, 316, 98, fit, ["Produces the fitted model"])
        d.box(
            22,
            315,
            316,
            98,
            "Calibration data",
            ["Separate features + targets", "Used with the fitted model"],
            True,
        )
        d.box(
            22,
            443,
            316,
            112,
            method,
            ["Same fitted model + CE state", "Includes calibration references"],
            True,
        )
        d.head(600, "2 · Evaluate — held-out test", w)
        d.box(
            22,
            672,
            316,
            103,
            "Test features → same system",
            ["Predict or explain test cases", "No test targets in these calls"],
        )
        d.box(22, 805, 316, 98, "Test outputs", ["Retain the results for checking"], True)
        d.box(22, 940, 316, 63, "Test targets", ["Kept for evaluation only"])
        d.arrow("M180 1003V1033")
        d.box(
            22,
            1033,
            316,
            97,
            "Check results",
            ["Compare outputs with targets", "Keep fitting/calibration separate"],
        )
        d.head(1210, "3 · Use — a new case", w)
        d.box(
            22,
            1285,
            316,
            98,
            "New-case features",
            ["Target not required", "Choose the output question"],
        )
        d.box(
            22,
            1413,
            316,
            112,
            "Reuse the same CE system",
            ["Fitted model + calibration state", "Predictive model stays fixed"],
            True,
        )
        d.box(22, 1555, 316, 112, "Prediction information", pred, True)
        d.arrow("M337 1470H350V1747H337")
        d.box(22, 1697, 316, 112, "Explanations", expl, True)
        d.text(180, 1840, "Ranges have method-specific meanings.", 16)
        d.text(180, 1865, "White: ML / data · Orange: CE additions", 16)
    else:
        d.head(12, "1 · Prepare the system — development", w)
        for p in ["M335 128H375", "M545 185V250", "M335 305H375", "M710 305H750"]:
            d.arrow(p)
        d.box(25, 75, 310, 110, "Training data", ["Features + known targets"])
        d.box(375, 75, 335, 110, fit, ["Produces the fitted model"])
        d.box(
            750,
            250,
            325,
            110,
            "Configured CE system",
            ["Keep this fitted model", "Reuse CE state for queries"],
            True,
        )
        d.box(25, 250, 310, 110, "Calibration data", ["Separate features + targets"], True)
        d.box(
            375,
            250,
            335,
            110,
            method,
            ["Fitted model + CE state", "Includes calibration references"],
            True,
        )
        d.text(907, 117, "CE adds calibration state", 18, True)
        d.text(907, 146, "without retraining this model.", 18)
        d.head(405, "2 · Evaluate the system — held-out test data", w)
        for p in ["M335 520H375", "M710 520H750", "M907 575V612", "M335 665H750"]:
            d.arrow(p)
        d.box(25, 465, 310, 110, "Test features", ["Query inputs only"])
        d.box(
            375,
            465,
            335,
            110,
            "Query the same CE system",
            ["Predict or explain", "No test targets passed in"],
            True,
        )
        d.box(750, 465, 325, 110, "Test outputs", ["Results for evaluation"], True)
        d.box(25, 615, 310, 100, "Test targets", ["Known outcomes; kept aside"])
        d.box(750, 615, 325, 100, "Check results", ["Compare outputs with targets"])
        d.head(760, "3 · Use the system — inference with a new case", w)
        for p in ["M335 888H375", "M710 870H750", "M710 905H730V1010H750"]:
            d.arrow(p)
        d.box(
            25,
            835,
            310,
            110,
            "New-case features",
            ["Target not required", "Choose the output question"],
        )
        d.box(
            375,
            835,
            335,
            110,
            "Reuse the same CE system",
            ["Fitted model + calibration state", "Predictive model stays fixed"],
            True,
        )
        d.box(750, 825, 325, 110, "Prediction information", pred, True)
        d.box(750, 960, 325, 110, "Explanations", expl, True)
        d.arrow("M180 945V980")
        d.box(
            25,
            980,
            685,
            90,
            "Without CE (conventional route)",
            ["The same fitted model returns a class, value or score."],
        )
        d.text(
            550,
            1095,
            "White: ML / data · Orange: CE additions · Arrows: information flow, not required API calls",
            17,
        )
    d.save(stem + ("-mobile" if m else "") + ".svg")


for m in (False, True):
    for stem in ["ce-big-picture", "ce-reference-workflow", "ce-how-workflow"]:
        workflow(stem, m)
    for slug in MODES:
        workflow("ce-mode-" + slug, m, slug)


def task_map(m=False):
    w = 360 if m else 1100
    h = 1660 if m else 1030
    d = Diagram(
        w,
        h,
        "CE tasks, output questions and explanation capabilities",
        "A predictive task depends on the target: classification includes binary and multiclass; regression has a numerical target. Classification asks about class probabilities. A fitted regressor supports numerical-value intervals or event-probability questions. Factual explanations compare responses under feature conditions; alternatives report predictions under other conditions. Output scales and range meanings depend on the selected question. These are conceptual routes, not three unrelated predictive tasks or a guarantee that every extension supports every configuration.",
    )
    if m:
        d.head(12, "Task → question → explanation", w)
        d.box(22, 85, 316, 90, "Classification", ["Categorical target", "Binary or multiclass"])
        d.arrow("M180 175V205")
        d.box(
            22,
            205,
            316,
            112,
            "Class-probability question",
            ["Which class, and how probable?", "Class probabilities + bounds"],
            True,
        )
        d.box(22, 365, 316, 90, "Regression", ["Numerical target", "The same fitted regressor"])
        d.arrow("M180 455V485")
        d.box(
            22,
            485,
            316,
            112,
            "Value-and-interval question",
            ["What value, with what interval?", "Prediction in target units"],
            True,
        )
        d.text(180, 635, "OR ask about an event", 18, True)
        d.box(
            22,
            675,
            316,
            112,
            "Event-probability question",
            ["How probable is Y ≤ t?", "Probability + bounds"],
            True,
        )
        d.head(855, "For the selected output question", w)
        d.box(
            22,
            935,
            316,
            130,
            "Factual explanation",
            [
                "Conditions holding for this case",
                "Compare model responses",
                "Weight + its reported range",
            ],
            True,
        )
        d.box(
            22,
            1105,
            316,
            130,
            "Alternative explanation",
            [
                "Consider another condition",
                "Read its prediction + range",
                "No causal effect is established",
            ],
            True,
        )
        d.box(
            22,
            1285,
            316,
            112,
            "Keep the scale consistent",
            ["Class / event: probability scale", "Value: numerical target units"],
        )
        d.box(
            22,
            1440,
            316,
            130,
            "Read the method’s conditions",
            [
                "Probability bounds differ from",
                "target-value prediction intervals.",
                "Weight ranges are distinct.",
            ],
        )
        d.text(180, 1620, "Optional extensions need a support check.", 16)
    else:
        d.head(12, "Task: what kind of target does the model learn?", w)
        d.box(
            25,
            95,
            325,
            105,
            "Classification",
            ["Categorical target", "Binary (2) or multiclass (3+)"],
        )
        d.box(
            390,
            95,
            685,
            105,
            "Regression",
            ["Numerical target · the same fitted regressor can answer either question"],
        )
        for p in ["M187 200V290", "M732 200V245H552V290", "M732 245H912V290"]:
            d.arrow(p)

        d.box(
            25,
            290,
            325,
            135,
            "Classification",
            ["Which class, and how probable?", "Class probabilities + bounds"],
            True,
        )
        d.box(
            390,
            290,
            325,
            135,
            "Interval regression",
            ["What value, with what interval?", "Value + interval in target units"],
            True,
        )
        d.box(
            750,
            290,
            325,
            135,
            "Probabilistic regression",
            ["How probable is Y ≤ t?", "Event probability + bounds"],
            True,
        )
        d.text(
            550, 475, "Mode: choose the output quantity before interpreting its range.", 20, True
        )
        d.head(515, "Capabilities: explain the response for your chosen question", w)
        d.box(
            25,
            605,
            510,
            150,
            "Factual explanation",
            [
                "Conditions holding for the case",
                "Compare model responses",
                "Report weights with their ranges",
            ],
            True,
        )
        d.box(
            565,
            605,
            510,
            150,
            "Alternative explanation",
            [
                "Consider another feature condition",
                "Report the resulting prediction and range",
                "A model comparison, not a causal effect",
            ],
            True,
        )
        d.box(
            25,
            805,
            1050,
            95,
            "Factual weights use the selected scale",
            [
                "Class / event → probability differences · Numerical value → differences in target units"
            ],
        )
        d.text(
            550,
            945,
            "A probability bound, target-value interval and weight range are different quantities.",
            19,
        )
        d.text(
            550,
            980,
            "Optional extensions have task-, mode- and configuration-specific support and conditions.",
            18,
        )
    d.save("ce-tasks-capabilities" + ("-mobile" if m else "") + ".svg")


def options_map(m=False):
    rows = [
        ("At calibration", "Mondrian calibration", "Use defined calibration groups."),
        ("During explanation building", "Guarding", "Check candidate representatives."),
        ("When combining conditions", "Conjunctions", "Combine feature conditions in rules."),
        (
            "After alternative generation",
            "Alternative filtering",
            "Select rules by a stated criterion.",
        ),
        ("For case handling", "Rejection / defer handling", "Flag cases under a configured rule."),
    ]
    w = 360 if m else 1100
    h = 1260 if m else 770
    d = Diagram(
        w,
        h,
        "Optional CE features have different jobs",
        "Mondrian calibration uses group information at calibration and query time. Guarding checks selected candidate representatives during explanation construction. Conjunctions combine feature conditions. Alternative filters select generated alternative rules. Rejection handles queried cases under a configured criterion, with setup requirements. These features are not five required stages; verify support and conditions for the task, mode and software version. Guarding is not universal query out-of-distribution detection or case rejection.",
    )
    d.head(12, "Optional CE features", w)
    for i, (stage, name, job) in enumerate(rows):
        if m:
            y = 90 + i * 216
            d.box(22, y, 316, 58, stage)
            d.arrow(f"M180 {y + 58}V{y + 82}", True)
            d.box(
                22,
                y + 82,
                316,
                102,
                name,
                ["Combine feature conditions", "into rules."] if name == "Conjunctions" else [job],
                True,
            )
        else:
            y = 95 + i * 119
            d.box(25, y, 435, 93, stage)
            d.arrow(f"M460 {y + 46}H510", True)
            d.box(510, y, 565, 93, name, [job], True)
    d.text(w / 2, h - 65, "These are options, not mandatory stages.", 17, True)
    d.text(w / 2, h - 36, "Check support, prerequisites and conditions.", 17)
    d.save("ce-optional-features" + ("-mobile" if m else "") + ".svg")


for m in (False, True):
    task_map(m)
    options_map(m)


def comparison(m=False):
    """Compare a basic conventional ML workflow with the same workflow plus CE.

    Verified against the implementation: ``fit`` trains only the learner;
    ``calibrate`` requires that fitted learner and does not refit it; ``predict``
    and ``explain_*`` take features only; without calibration ``predict``
    returns ``learner.predict``.
    """
    w = 360 if m else 1100
    h = 2440 if m else 1350
    d = Diagram(
        w,
        h,
        "What CE adds to a basic conventional ML workflow",
        "Two lanes share the same fitted predictive model. Conventional ML: training data fit the model; at inference, new-case features go to that model, which returns a class, numerical value or score. With CE: the same fitted model, not retrained, plus separate labelled calibration data configure a CE system; at inference, the same new-case features go to that system, which returns prediction information with a mode-specific range, and factual or alternative explanations with ranges. Held-out evaluation is separate: test features obtain outputs from the model or CE system; test targets are used only to check those outputs and never enter prediction or explanation. White marks conventional parts, orange marks CE additions. Conventional systems can also use other calibration or explanation tools; this compares CE with a basic model-only workflow. Arrows show information flow, not API calls.",
    )
    ce_outputs = ("Prediction information", ["Probability or numerical value", "with a mode-specific range"])
    if m:
        x, bw = 22, 316
        d.box(12, 12, w - 24, 48, "Conventional ML")
        d.text(180, 95, "Preparation · once", 17, True)
        for p in ["M180 185V210", "M180 420V445", "M180 525V550"]:
            d.arrow(p)
        d.box(x, 105, bw, 80, "Training data", ["Features + known targets"])
        d.box(x, 210, bw, 80, "Fitted predictive model", ["Learns from training data"])
        d.text(180, 325, "Inference · each new case", 17, True)
        d.box(x, 340, bw, 80, "New-case features", ["Target not needed"])
        d.box(x, 445, bw, 80, "Same fitted model", ["From preparation"])
        d.box(x, 550, bw, 90, "Model output", ["Class, numerical value", "or score"])
        d.text(180, 672, "Other tools can add calibration", 15)
        d.text(180, 697, "or explanations to this lane.", 15)

        d.box(12, 730, w - 24, 48, "With CE", ce=True)
        d.text(180, 812, "Preparation · once", 17, True)
        for p in ["M180 1020V1050", "M180 1275V1300", "M180 1380V1405"]:
            d.arrow(p)
        d.arrow("M22 865H10V1095H22")
        d.arrow("M338 1340H350V1585H338")
        d.box(x, 825, bw, 80, "Same fitted model", ["Reused, not retrained"])
        d.box(x, 930, bw, 90, "Calibration data", ["Separate labelled cases:", "features + targets"], True)
        d.box(x, 1050, bw, 90, "Configured CE system", ["Model + calibration state"], True)
        d.text(180, 1180, "Inference · each new case", 17, True)
        d.box(x, 1195, bw, 80, "Same new-case features", ["Target not needed"])
        d.box(x, 1300, bw, 80, "Same CE system", ["Model + calibration state"], True)
        d.box(x, 1405, bw, 90, *ce_outputs, True)
        d.box(
            x,
            1525,
            bw,
            120,
            "Explanations",
            ["Factual: weights + ranges", "Alternatives: predictions", "for other conditions + ranges"],
            True,
        )

        d.box(12, 1690, w - 24, 48, "Held-out evaluation")
        for p in ["M180 1840V1865", "M180 1955V1980", "M180 2060V2085"]:
            d.arrow(p)
        d.arrow("M180 2195V2165")
        d.box(x, 1760, bw, 80, "Test features", ["Query inputs only"])
        d.box(x, 1865, bw, 90, "Same model or CE system", ["Predict or explain"])
        d.box(x, 1980, bw, 80, "Test outputs", ["Kept for checking"])
        d.box(x, 2085, bw, 80, "Check results", ["Compare outputs with targets"])
        d.box(x, 2195, bw, 90, "Test targets", ["Known outcomes, kept aside", "Used only in the check"])
        d.text(180, 2320, "Test targets never enter", 16, True)
        d.text(180, 2345, "prediction or explanation.", 16, True)
        d.text(180, 2385, "White: conventional ML", 15)
        d.text(180, 2410, "Orange: what CE adds", 15)
    else:
        ax, bx, lw, half = 25, 575, 500, 240
        d.box(ax, 12, lw, 52, "Conventional ML")
        d.box(bx, 12, lw, 52, "With CE", ce=True)

        # Preparation band
        d.parts.append('<path d="M25 82H1075" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 6"/>')
        d.text(550, 100, "PREPARATION · done once, before use", 18, True)
        for p in ["M275 205V235", "M695 325V355", "M955 325V355"]:
            d.arrow(p)
        d.arrow("M525 280H575", dashed=True)
        d.box(ax, 115, lw, 90, "Training data", ["Features + known targets"])
        d.box(ax, 235, lw, 90, "Fitted predictive model", ["Learns from the training data"])
        d.text(825, 150, "CE starts from the model you already have,", 17)
        d.text(825, 178, "plus separate labelled calibration data.", 17)
        d.box(bx, 235, half, 90, "Same fitted model", ["Reused, not retrained"])
        d.box(835, 235, half, 90, "Calibration data", ["Separate labelled cases:", "features + targets"], True)
        d.box(bx, 355, lw, 90, "Configured CE system", ["Same model + calibration state"], True)

        # Inference band
        d.parts.append('<path d="M25 482H1075" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 6"/>')
        d.text(550, 500, "INFERENCE · repeated for each new case", 18, True)
        for p in ["M275 600V630", "M275 720V750", "M825 600V630", "M825 720V750"]:
            d.arrow(p)
        # Explanations come from the CE system, not from the prediction box.
        d.arrow("M575 690H555V927H575")
        # Reuse connectors: preparation results are the same objects used at inference.
        d.arrow("M25 280H12V675H25", dashed=True)
        d.arrow("M1075 400H1088V675H1075", dashed=True)
        d.box(ax, 520, lw, 80, "New-case features", ["The case's target is not needed"])
        d.box(bx, 520, lw, 80, "Same new-case features", ["The case's target is not needed"])
        d.box(ax, 630, lw, 90, "Same fitted model", ["Unchanged from preparation"])
        d.box(bx, 630, lw, 90, "Same configured CE system", ["Model + calibration state, reused"], True)
        d.box(ax, 750, lw, 90, "Model output", ["Class, numerical value or score"])
        d.box(bx, 750, lw, 90, *ce_outputs, True)
        d.box(
            bx,
            870,
            lw,
            115,
            "Explanations",
            ["Factual: feature weights with ranges", "Alternatives: predictions with ranges", "under other feature conditions"],
            True,
        )
        d.text(275, 905, "A basic model reports no range or explanation", 16)
        d.text(275, 931, "by itself; other tools can add them.", 16)

        # Evaluation band
        d.parts.append('<path d="M25 1018H1075" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 6"/>')
        d.text(550, 1036, "HELD-OUT EVALUATION · before relying on either lane", 18, True)
        for p in ["M245 1100H285", "M555 1100H595", "M815 1100H855"]:
            d.arrow(p)
        d.arrow("M965 1190V1145")
        d.box(25, 1055, 220, 90, "Test features", ["Query inputs only"])
        d.box(285, 1055, 270, 90, "Same fitted model", ["or same CE system"])
        d.box(595, 1055, 220, 90, "Test outputs", ["Predictions or", "explanations"])
        d.box(855, 1055, 220, 90, "Check results", ["Compare outputs", "with test targets"])
        d.box(855, 1190, 220, 90, "Test targets", ["Known outcomes,", "kept aside"])
        d.text(430, 1225, "Test targets go only to the check.", 18, True)
        d.text(430, 1253, "They never enter prediction or explanation.", 18, True)
        d.text(
            550,
            1318,
            "White: conventional ML and data · Orange: what CE adds · Arrows: information flow, not API calls",
            16,
        )
    d.save("ce-adds-comparison" + ("-mobile" if m else "") + ".svg")


for m in (False, True):
    comparison(m)
