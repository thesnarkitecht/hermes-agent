<p align="center">
  <img src="assets/huntington-logo.svg" alt="HUNTINGTON-AGENT" width="160">
</p>

# HUNTINGTON-AGENT

A terminal-first AI agent by HIP. It is built on an open-source, MIT-licensed agent engine
(memory, skills, subagents, scheduled jobs, the terminal and browser tools), narrowed to what
Huntington uses. `scripts/huntington/sync-upstream.sh` keeps pulling in new engine features.

## Install (terminal)

Linux, macOS, WSL2:

```bash
curl -fsSL https://raw.githubusercontent.com/thesnarkitecht/huntington-agent/main/scripts/install.sh | bash
```

Windows (PowerShell):

```powershell
iex (irm https://raw.githubusercontent.com/thesnarkitecht/huntington-agent/main/scripts/install.ps1)
```

Both installers clone this repository into `~/.huntington` (Windows: `%LOCALAPPDATA%\huntington`),
which also holds your configuration, keys, sessions and skills. The repository is private, so the
one-line install needs GitHub access; see "Installing from a private repository" below. After
installing, reload your shell and run `huntington`:

```bash
huntington            # chat in the CLI
huntington setup      # pick a model provider, tools and messaging
huntington model      # switch provider or model
huntington update     # update from this repository
```

`hermes` still works as an alias for `huntington`: the engine's skills and scripts call it.

### Installing from a private repository

`raw.githubusercontent.com` and `git clone` both need credentials for a private repository. Either
make the repository public, or install with a GitHub token that can read it:

```bash
export GITHUB_TOKEN=<token with read access to thesnarkitecht/huntington-agent>
curl -fsSL -H "Authorization: token $GITHUB_TOKEN" https://raw.githubusercontent.com/thesnarkitecht/huntington-agent/main/scripts/install.sh | HERMES_REPO_URL="https://x-access-token:$GITHUB_TOKEN@github.com/thesnarkitecht/huntington-agent.git" bash
```

That token ends up in the installed checkout's git remote (`~/.huntington/hermes-agent/.git/config`)
so `huntington update` can pull. Use a fine-grained, read-only token for this one repository.

## What this build includes

| Area | Supported | Planned |
|---|---|---|
| Interface | Classic CLI. `huntington dashboard` hosts the same CLI in the browser. | |
| Model providers | Anthropic (API key, or Claude subscription sign-in) · OpenAI (API key, or ChatGPT sign-in) · MiniMax (API key, or browser sign-in) · Moonshot / Kimi (API key) · Ollama (local server, or Ollama Cloud API key) | |
| Terminal backend | `local` | Huntington VM service (a terminal-backend plugin) |
| Browser | Local Chromium (Lightpanda optional) | |
| Web search | Off by default; opt in with `huntington tools`. Backends: xAI, Brave Search, DuckDuckGo, Perplexity | |
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

## Engine documentation

The upstream engine's documentation (<https://hermes-agent.nousresearch.com/docs/>) still describes
configuration, skills, memory, cron and tools; read its `hermes` commands as `huntington` and
`~/.hermes` as `~/.huntington`. Where it covers features listed as removed above, it does not apply.

## License

MIT. The engine is the open-source Hermes Agent project; its copyright and license notice are in
[LICENSE](LICENSE) and must stay with every copy.
