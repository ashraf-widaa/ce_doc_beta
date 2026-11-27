"""Build the CE capability map: where each capability applies in the workflow.

Run from the repository root: ``python scripts/docs/build_capability_map.py``.
Writes ``docs/_static/figures/ce-capability-map.svg`` (desktop) and
``ce-capability-map-narrow.svg`` (mobile). SVGs are git-ignored; add changes
with ``git add -f``.

Style follows ``ce-adds-to-workflow.svg``: white card, orange for CE operations
(solid = core, dashed = optional) and blue for the application's own step.
API names were checked against ``src/calibrated_explanations``:
``calibrate(bins=...)``, ``predict``/``predict_proba(uq_interval=True)``,
``reject_policy=``, ``explain_factual``, ``explore_alternatives``,
``guarded_options=``, ``add_conjunctions``, ``counter_explanations`` and
``ensured_explanations``.
"""

from __future__ import annotations

import html
from pathlib import Path

DEST = Path(__file__).resolve().parents[2] / "docs" / "_static" / "figures"
FONT = "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

STEPS = ["1 · Calibrate", "2 · Predict", "3 · Explain", "4 · Refine / decide"]
# (kind, name, lines, code lines); kind: core | optional | app
CORE = [
    [("core", "Calibration", [], ["calibrate()"])],
    [("core", "Prediction + uncertainty", [], ["predict / predict_proba", "(uq_interval=True)"])],
    [
        ("core", "Factual explanations", [], ["explain_factual()"]),
        ("core", "Alternative explanations", [], ["explore_alternatives()"]),
    ],
    [
        ("optional", "Conjunctions", [], [".add_conjunctions()"]),
        ("optional", "Alternative filtering", [], [".counter_explanations()", ".ensured_explanations()"]),
    ],
]
OPTIONAL = [
    ("optional", "Mondrian (grouped)", [], ["calibrate(bins=...)"]),
    ("optional", "Rejection", ["flag for review"], ["reject_policy=..."]),
    ("optional", "Guarded explanations", [], ["guarded_options=..."]),
    ("app", "Your decision policy", ["cutoffs, abstain", "not a CE call"], []),
]
STYLE = {
    "core": ("#ffedd5", "#ea580c", "", "#7c2d12"),
    "optional": ("#fff7ed", "#ea580c", ' stroke-dasharray="6 4"', "#7c2d12"),
    "app": ("#dbeafe", "#2563eb", ' stroke-dasharray="6 4"', "#1e3a8a"),
}


class Svg:
    def __init__(self, w: int, h: int, desc: str) -> None:
        self.w, self.h = w, h
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" '
            f'aria-labelledby="cm-title cm-desc" font-family="{html.escape(FONT, quote=True)}">',
            '  <title id="cm-title">Capability map: where each feature applies in the workflow</title>',
            f'  <desc id="cm-desc">{html.escape(desc)}</desc>',
            '  <defs><marker id="cm-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
            'markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#64748b"/></marker></defs>',
            f'  <rect x="0" y="0" width="{w}" height="{h}" rx="14" fill="#ffffff"/>',
        ]

    def text(self, x, y, t, size=13, weight=400, fill="#334155", anchor="middle", mono=False):
        fam = f' font-family="{html.escape(MONO, quote=True)}"' if mono else ""
        self.parts.append(
            f'  <text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}"{fam}>{html.escape(t)}</text>'
        )

    def header(self, x, y, w, h, t):
        self.parts.append(f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#334155"/>')
        self.text(x + w / 2, y + h / 2 + 6, t, 16, 700, "#ffffff")

    def box(self, x, y, w, h, item):
        kind, name, lines, code = item
        fill, stroke, dash, ink = STYLE[kind]
        self.parts.append(
            f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="2"{dash}/>'
        )
        rows = [(name, 14, 700, ink, False)] + [(t, 12, 400, "#334155", False) for t in lines]
        rows += [(t, 12, 400, "#7c2d12" if kind != "app" else "#1e3a8a", True) for t in code]
        step = 17
        top = y + h / 2 - (len(rows) - 1) * step / 2 + 5
        for i, (t, size, weight, color, mono) in enumerate(rows):
            self.text(x + w / 2, top + i * step, t, size, weight, color, mono=mono)

    def arrow(self, d):
        self.parts.append(
            f'  <path d="{d}" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#cm-arrow)"/>'
        )

    def save(self, name: str) -> None:
        (DEST / name).write_text("\n".join(self.parts) + "\n</svg>\n", encoding="utf-8", newline="\n")


DESC = (
    "Four workflow steps: 1 Calibrate, 2 Predict, 3 Explain, 4 Refine or decide. "
    "Core operations: calibration with calibrate(); prediction with uncertainty with predict or "
    "predict_proba and uq_interval=True; factual explanations with explain_factual(); alternative "
    "explanations with explore_alternatives(). Optional: conjunctions with add_conjunctions(); "
    "alternative filtering with counter_explanations() or ensured_explanations(); Mondrian (grouped) "
    "calibration with calibrate(bins=...); rejection, flagging predictions for review, with "
    "reject_policy=...; guarded explanations with guarded_options=.... The final decision policy, "
    "such as cutoffs or abstaining, belongs to your application and is not a CE call. "
    "Availability depends on task, mode, configuration and version."
)
KEY = "Solid: core · Dashed: optional · Blue: your application, not a CE call"


def desktop() -> None:
    w, h = 920, 470
    s = Svg(w, h, DESC)
    cw, gap, x0 = 202, 24, 20
    xs = [x0 + i * (cw + gap) for i in range(4)]
    for i, x in enumerate(xs):
        s.header(x, 20, cw, 44, STEPS[i])
        if i < 3:
            s.arrow(f"M{x + cw + 3} 42 H{x + cw + gap - 3}")
    s.text(x0, 92, "CORE", 12, 700, "#475569", "start")
    for i, items in enumerate(CORE):
        for j, item in enumerate(items):
            s.box(xs[i], 102 + j * 96, cw, 84, item)
    s.text(x0, 312, "OPTIONAL", 12, 700, "#475569", "start")
    for i, item in enumerate(OPTIONAL):
        s.box(xs[i], 322, cw, 84, item)
    s.text(w / 2, 434, KEY, 13, 400, "#475569")
    s.text(w / 2, 454, "Availability depends on task, mode, configuration and version.", 12, 400, "#64748b")
    s.save("ce-capability-map.svg")


def narrow() -> None:
    w, x, bw = 360, 20, 320
    blocks = []
    y = 16
    for i in range(4):
        blocks.append(("header", y, STEPS[i]))
        y += 50
        for it in CORE[i]:
            blocks.append(("box", y, it))
            y += 80
        blocks.append(("box", y, OPTIONAL[i]))
        y += 80
        if i < 3:
            blocks.append(("arrow", y - 6, None))
            y += 22
    y += 8
    key_y = y
    h = key_y + 60
    s = Svg(w, h, DESC)
    for kind, by, payload in blocks:
        if kind == "header":
            s.header(x, by, bw, 38, payload)
        elif kind == "box":
            s.box(x, by, bw, 70, payload)
        else:
            s.arrow(f"M{w / 2} {by} V{by + 22}")
    s.text(w / 2, key_y + 14, "Solid: core · Dashed: optional", 12, 400, "#475569")
    s.text(w / 2, key_y + 32, "Blue: your application, not a CE call", 12, 400, "#475569")
    s.text(w / 2, key_y + 50, "Depends on task, mode, configuration, version.", 11, 400, "#64748b")
    s.save("ce-capability-map-narrow.svg")


if __name__ == "__main__":
    desktop()
    narrow()
    print("wrote ce-capability-map.svg and ce-capability-map-narrow.svg")
