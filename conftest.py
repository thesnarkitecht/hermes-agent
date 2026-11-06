"""HUNTINGTON-AGENT: deselect upstream tests that drive features this fork removes or gates.

`huntington/deselected-tests.txt` lists pytest node ids (one per line, `#` comments). Each one
exercises a removed platform/backend or asserts upstream's wider defaults (other providers, TTS and
search backends, the TUI, the desktop app). Whole test files for removed features are deleted via
`huntington/removed-paths.txt` instead. The fork's own policy contract is
`tests/hermes_cli/test_huntington_policy.py`.
"""
from __future__ import annotations

from pathlib import Path

_LIST = Path(__file__).resolve().parent / "huntington" / "deselected-tests.txt"


def _deselected() -> frozenset[str]:
    try:
        lines = _LIST.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return frozenset()
    return frozenset(s for s in (line.strip() for line in lines) if s and not s.startswith("#"))


def pytest_collection_modifyitems(config, items):
    ids = _deselected()
    if not ids:
        return
    # A parametrized id whose parameters contain spaces is recorded up to its first space,
    # leaving an unclosed "[": such an entry deselects every node id it prefixes.
    prefixes = tuple(i for i in ids if "[" in i and not i.endswith("]"))
    drop = [item for item in items if item.nodeid in ids or (prefixes and item.nodeid.startswith(prefixes))]
    if drop:
        config.hook.pytest_deselected(items=drop)
        kept = {id(item) for item in drop}
        items[:] = [item for item in items if id(item) not in kept]
