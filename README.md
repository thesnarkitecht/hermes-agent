<p align="center">
  <img src="assets/huntington-logo.svg" alt="HUNTINGTON-AGENT" width="160">
</p>

# HUNTINGTON-AGENT

A terminal-first AI agent for Huntington, built on the open-source
[Hermes Agent](https://github.com/NousResearch/hermes-agent) by Nous Research (MIT). It keeps the
upstream engine (memory, skills, subagents, scheduled jobs, the terminal and browser tools) and
narrows the product to what Huntington uses. `scripts/huntington/sync-upstream.sh` keeps pulling in
new upstream features.

## Install (terminal)

Linux, macOS, WSL2:

```bash
curl -fsSL https://raw.githubusercontent.com/thesnarkitecht/huntington-agent/main/scripts/install.sh | bash
```

Windows (PowerShell):

```powershell
iex (irm https://raw.githubusercontent.com/thesnarkitecht/huntington-agent/main/scripts/install.ps1)
```

Both installers clone this repository. After installing, reload your shell and run `hermes`:

```bash
hermes            # chat in the CLI
hermes setup      # pick a model provider, tools and messaging
hermes model      # switch provider or model
hermes update     # update from this repository
```

The command is still `hermes`. Upstream's docs, skills and installer all depend on that name, and
keeping it is what lets upstream merges apply cleanly.

## What this build includes

| Area | Supported | Planned |
|---|---|---|
| Interface | Classic CLI. `hermes dashboard` hosts the same CLI in the browser. | |
| Model providers | Anthropic (API key, or Claude subscription sign-in) · OpenAI (API key, or ChatGPT sign-in) · MiniMax (API key, or browser sign-in) · Moonshot / Kimi (API key) · Ollama (local server, or Ollama Cloud API key) | |
| Terminal backend | `local` | Huntington VM service (a terminal-backend plugin) |
| Browser | Local Chromium (Lightpanda optional) | |
| Web search | Off by default; opt in with `hermes tools`. Backends: xAI, Brave Search, DuckDuckGo, Perplexity | |
| Image generation | OpenAI (API key, or ChatGPT sign-in) | Local image generation |
| Text-to-speech | Microsoft Edge TTS (default), Piper (local) | Qwen TTS |
| Messaging | Microsoft Teams, email, A2A | |

Removed from upstream: the Electron desktop app and its browser-hosted Webapp, the Ink TUI,
Docker and Nix installs, upstream's release publishing, and every other messaging platform
(Telegram, Discord, Slack, WhatsApp, Signal, Yuanbao and the rest). The full list is in
[`huntington/removed-paths.txt`](huntington/removed-paths.txt). The provider, backend and tool
choices live in [`hermes_cli/huntington.py`](hermes_cli/huntington.py).

## Staying current with upstream

```bash
scripts/huntington/sync-upstream.sh
```

The script merges `NousResearch/hermes-agent` `main`, deletes every path in
`huntington/removed-paths.txt` again, and keeps the fork's copy of each file in
`huntington/fork-owned-paths.txt`. A conflict can still happen where an upstream change lands
next to one of the fork's one-line hooks into `hermes_cli/huntington.py`. In that case the script
stops and lists the files to resolve by hand.

Upstream tests that drive removed features are deleted (they are listed in
`huntington/removed-paths.txt`). Upstream tests that assert upstream's wider defaults, such as other
providers in the pickers or other TTS backends, are deselected through
`huntington/deselected-tests.txt`, which the root `conftest.py` reads. When a sync brings in a new
upstream test of that kind, add its node id there. The fork's own contract is
`tests/hermes_cli/test_huntington_policy.py`. Run the tests before pushing:

```bash
scripts/run_tests.sh tests/hermes_cli tests/tools
```

[`huntington/TRIM-ANALYSIS.md`](huntington/TRIM-ANALYSIS.md) covers what else could be trimmed
from the engine.

## Upstream documentation

Upstream's documentation at <https://hermes-agent.nousresearch.com/docs/> still describes the
shared engine: configuration, skills, memory, cron and tools. Where it covers features listed as
removed above, it does not apply to this build.

## License

MIT, as upstream. See [LICENSE](LICENSE).
