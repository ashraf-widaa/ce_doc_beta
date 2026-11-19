from __future__ import annotations

from pathlib import Path

from tests.helpers.doc_utils import resolve_doc

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"


def test_top_level_toctree_targets_exist() -> None:
    expected = (
        "get-started/index",
        "sections/what-and-why",
        "sections/how-ce-works",
        "sections/in-practice",
        "sections/software-integration",
        "sections/project-resources",
    )
    index_path = resolve_doc("index")
    index = index_path.read_text()
    for slug in expected:
        assert slug in index, f"Missing toctree entry for {slug}"
        target = resolve_doc(slug)
        assert target.exists(), f"Document referenced by {slug} is missing"


def test_maintenance_docs_exist() -> None:
    expected = [
        "maintenance/legacy-plotting-reference.md",
    ]
    for path in expected:
        assert (DOCS / path).exists(), f"Maintenance document {path} is missing"


def test_upgrade_docs_exist() -> None:
    assert (DOCS / "upgrade" / "v1.0.0-upgrade-checklist.md").exists()
    assert (DOCS / "upgrade" / "index.md").exists()


def test_safe_defaults_doc_exists() -> None:
    assert (DOCS / "foundations" / "how-to" / "safe-defaults.md").exists()


def test_upgrade_index_in_toctree() -> None:
    # Upgrade guidance belongs with installation and integration, not first use.
    text = (DOCS / "sections" / "software-integration.md").read_text(encoding="utf-8")
    assert "Upgrade guides <../upgrade/index>" in text


def test_reject_policy_doc_contract_sections_exist() -> None:
    reject_doc = resolve_doc("practitioner/advanced/reject-policy")
    content = reject_doc.read_text(encoding="utf-8")

    required_snippets = (
        "## Reject-aware return types",
        "`predict` / `predict_proba`: returns `RejectResult`",
        "### Threshold tie behavior",
        "`y <= threshold`",
        'eps = meta.get("epsilon")  # scalar float',
        "if len(result.explanations) == 0:",
        'result.metadata["source_indices"]',
    )

    for snippet in required_snippets:
        assert snippet in content, f"Missing reject-policy contract snippet: {snippet}"


def test_should_keep_one_reachable_sidebar_home_per_document() -> None:
    """Shared pages remain reachable without repeated parents or navigation cycles."""
    import posixpath
    import re
    from collections import defaultdict

    parents = defaultdict(list)
    children = defaultdict(list)
    blocks = re.compile(r"^```\{toctree\}\n(.*?)^```", re.MULTILINE | re.DOTALL)
    for page in DOCS.rglob("*.md"):
        parent = page.relative_to(DOCS).as_posix()[:-3]
        for block in blocks.findall(page.read_text(encoding="utf-8")):
            for line in block.splitlines():
                line = line.strip()
                if not line or line.startswith(":") or line.endswith("<self>"):
                    continue
                match = re.match(r".*?\s*<([^>]+)>$", line)
                target = match.group(1) if match else line
                target = posixpath.normpath(posixpath.join(posixpath.dirname(parent), target))
                parents[target].append(parent)
                children[parent].append(target)
    assert not {target: owners for target, owners in parents.items() if len(owners) > 1}
    seen = set()

    def walk(page, ancestors):
        assert page not in ancestors, f"Navigation cycle: {page}"
        seen.add(page)
        for child in children[page]:
            walk(child, ancestors | {page})

    walk("index", set())
    assert set(parents) <= seen
