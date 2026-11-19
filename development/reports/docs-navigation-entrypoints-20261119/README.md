# Navigation and entry-point review

Baseline: responsive homepage candidate `68bf1943fd28926cab9919c7cc431c1139f6c02d`.
Branch: `docs/navigation-entrypoints-20261119`.
Repository: `ashraf-widaa/ce_doc_beta` only. Official CE is read-only.

## Reader-visible changes

- Sidebar: 24 top-level destinations become seven: Home, Quickstart, What & Why,
  How CE Works, In Practice, Software & Integration, Project & Resources.
- Shared pages have one sidebar home. Previous access routes remain contextual
  links, so someone entering via research or practical guidance can still reach
  the same calibration, plotting, telemetry, interpretation or API page.
- Advanced collections expand within their section rather than appearing as
  independent top-level routes. The current branch expands using Furo's existing
  navigation behavior. Right sidebar contains current-page headings only.
- Section overviews now explain where to start and offer choices by question.
  Quickstart introduces task choice and connects setup, example, interpretation
  and integration. The tutorial code is retained for the next work package.
- Software groups setup, API, operations, help, upgrades and internals. Research,
  citation, roadmap and contributions are grouped under Project & Resources.
- Touch targets and focus indicators improved for sidebar links and switches.
  Mobile menu, scrolling and theme behavior retained.
- Existing page URLs retained. Shared foundations and reference collections remain
  accessible; the accompanying PAGE_MAP.md records ownership and reuse for all
  123 tree destinations. Existing heading anchors for Get started and Concepts &
  architecture are retained explicitly.

## Validation

- Documentation tests: 56 passed, including a new invariant test for unique
  sidebar ownership, reachability and absence of navigation cycles.
- Strict Sphinx HTML build: passed; no warnings.
- Internal-link check: 138 pages, zero broken links.
- Browser checks: 64 page/width/theme combinations across 320, 390, 768, 1440
  pixels and light/dark. Checks seven root entries, single current-page marker,
  page overflow, minimum root target height and current-page-only contents.
  Mobile menu expansion/link activation and keyboard focus/link activation pass.
- Manual screenshot review on desktop and mobile completed.
- All non-navigation fenced examples match the prior candidate byte-for-byte.
  No library source changes; canonical interval semantics is unchanged.
- Ruff lint of modified test file and git diff --check pass.

Local build uses existing virtualenv, PYTHONPATH=src and noninteractive plotting:

```sh
python -B -m sphinx -W --keep-going -D release=1.0.2 -D version=1.0 -D 'html_title=Calibrated Explanations v1.0.2' -b html docs /workspace/work/ce-navigation-evidence-20261119/html
```

Version overrides compensate for older candidate metadata installed in the shared
local environment. They do not change the source's runtime or version behavior.
Evidence: `/workspace/work/ce-navigation-evidence-20261119`.

## Remaining work / scientific review

This package improves access and orientation. The existing tutorials still need
visible first-result output, plot interpretation and the planned conventional-ML
versus-CE illustration. The new Quickstart is an orientation route to those
existing examples, not a claim that their content rewrite is complete.

No diabetes classification or California housing examples were introduced.
Dataset choice/targets must be verified before that work. Existing comparison
and API guarantee wording remains subject to scientific author review; navigation
changes do not validate or strengthen it. Feature ranges and prediction ranges
remain distinguished in the new introductions.

The inherited Furo overflow when directly setting the root font size to 200%
remains documented in the previous homepage report; this pass does not claim to
fix it. Automated responsive checks are not a full accessibility audit or an
observed novice usability study.

## Safety and publication

Push destination allowlist remains restricted to ashraf-widaa/ce_doc_beta. GitHub
Actions remains disabled. Publish only this new named RTD version; do not change
latest/default, the published clean baseline or the prior homepage version.
No credentials belong in source, reports or command arguments.

For a local preview, serve the built html directory on port 8775 and open it on
that machine, or forward the cloud port to your own computer.
