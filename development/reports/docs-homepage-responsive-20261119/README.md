# Responsive homepage candidate

Baseline: `f4d3dca7c69acfd042b49f49b577760baacebb1d`, an unchanged source
snapshot of official CE 1.0.2 (`609d7b728b76b7bfc1e831a9ca7986689c1b43d1`).
Branch: `docs/homepage-responsive-20261119`.

## What changed

- `docs/index.md`: introduction and one Quickstart action, four Documentation
  cards, four Project & Resources cards, separate original commercial-service
  purpose/content. Explicit independent-review notice links to official docs.
- `docs/_static/ce-home.css`: scoped responsive CSS, two columns above 600 CSS
  pixels and one below; full-width mobile primary action; wrapping text,
  keyboard focus outlines and touch targets. Uses theme colors for dark mode.
- `docs/conf.py`: registers the scoped stylesheet and static directory.
- Five `docs/sections/` pages: brief destinations for the section cards, using
  existing guides. No duplicated scientific definitions, code or figures.
- Existing root toctrees remain in the sidebar, hidden from homepage body.
  Sidebar reorganization is deliberately deferred to its own work package.
- Existing release, schema, upgrade, demo, companion, research and contributor
  resources remain available. Advanced release information is in a native
  keyboard-operable disclosure so it does not precede the first learning action.

## Card routing / reuse map

| Entry | Destination | Existing shared material reused |
| --- | --- | --- |
| Quickstart | `get-started/index` | Existing quickstarts and installation; tutorial rewrite deferred |
| What & Why | `sections/what-and-why` | Foundations, task map, comparison, interpretation and semantics |
| How CE Works | `sections/how-ce-works` | Concepts, regression, alternatives, semantics and literature |
| In Practice | `sections/in-practice` | Classification/regression quickstarts, interpretation, pipelines and practitioner hub |
| Software & Integration | `sections/software-integration` | Installation, Quick API, API, pipelines, configuration, troubleshooting and upgrades |
| Project, Vision & Evolution | `sections/project-resources` | Research, replication, citation, roadmap, contribution and governance |
| Glossary | `foundations/concepts/terminology` | Existing terminology reference, explicitly described as such; unified glossary deferred |
| GitHub / License | Official external destinations | Existing authoritative source and reuse terms |

## Validation

- Strict Sphinx HTML build passes.
- Existing documentation tests: 55 passed.
- Internal-link scan covers 138 HTML pages, zero broken links.
- Browser checks: widths 320, 375, 390, 600, 768, 1024, 1440 and 1920 in light
  and dark themes; one article heading, expected card columns/order, no page
  overflow, card targets resolve, Quickstart action routes correctly, focus
  indication and disclosure interaction work. Mobile navigation checked.
- Manual review of desktop/mobile screenshots; CSS is scoped to homepage
  elements and does not restyle other guides.
- `git diff --check` passes. No library source or executable examples changed.

Build command uses the existing virtualenv with `PYTHONPATH=src`:

```sh
python -B -m sphinx -W --keep-going -D release=1.0.2 -D version=1.0 -D 'html_title=Calibrated Explanations v1.0.2' -b html docs /workspace/work/ce-homepage-responsive-evidence/html
```

The local environment contains installed metadata from an older 1.1.0dev
candidate. Version overrides make the preview label match this 1.0.2 source;
no version-resolution behavior is changed in project code.

## Limitations and follow-up

Setting the root font size directly to 200% produces page overflow in Furo.
This also reproduces on the unchanged published baseline; the diagnostic
logs are saved. It is not claimed fixed by this scoped homepage pass.
Responsive width checks do not constitute a complete accessibility audit,
physical-device test or screen-reader test.

The Quickstart destination and scientific content are retained. The requested
introductory figure, new examples and tutorial wording are separate follow-up
work; no claims about new guarantees or dataset behavior were introduced.
Comparison claims and scientific reference wording remain author-review topics.

Publication requires a securely configured `READTHEDOCS_TOKEN`; none was present
for this turn. Do not reuse the credential previously pasted into chat. Never
modify default/latest or overwrite baseline/previous review versions.

## Preview

Evidence: `/workspace/work/ce-homepage-responsive-evidence`.

```sh
python -m http.server 8774 --bind 127.0.0.1 --directory /workspace/work/ce-homepage-responsive-evidence/html
```

Open `http://127.0.0.1:8774/` on that machine or forward port 8774 from the cloud.
The downloaded HTML preview can also be served locally after extraction.
