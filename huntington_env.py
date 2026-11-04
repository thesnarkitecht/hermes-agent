"""HUNTINGTON-AGENT environment aliases: ``HUNTINGTON_<NAME>`` sets ``HERMES_<NAME>``.

The engine reads ``HERMES_*`` variables (``HERMES_HOME``, ``HERMES_TUI``, ...). Users of this build
may spell them ``HUNTINGTON_*`` instead; an explicit ``HERMES_*`` value wins. Applied once, when
``hermes_constants`` is first imported, so child processes inherit both spellings.
"""
from __future__ import annotations

import os
from collections.abc import MutableMapping

_PREFIX = "HUNTINGTON_"


def apply_env_aliases(environ: MutableMapping[str, str] = os.environ) -> None:
    for key, value in list(environ.items()):
        if key.startswith(_PREFIX) and len(key) > len(_PREFIX):
            environ.setdefault("HERMES_" + key[len(_PREFIX):], value)
