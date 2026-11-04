---
sidebar_position: 9
title: "Optional Skills Catalog"
description: "Official optional skills shipped with hermes-agent — install via hermes skills install official/<category>/<skill>"
---

# Optional Skills Catalog

Optional skills ship with hermes-agent under `optional-skills/` but are **not active by default**. Install them explicitly:

```bash
hermes skills install official/<category>/<skill>
```

For example:

```bash
hermes skills install official/blockchain/solana
hermes skills install official/mlops/flash-attention
```

Each skill below links to a dedicated page with its full definition, setup, and usage.

To uninstall:

```bash
hermes skills uninstall <skill-name>
```

## autonomous-ai-agents

| Skill | Description |
|-------|-------------|
| [**agent-merge-conflict-arbiter**](../user-guide/skills/optional/autonomous-ai-agents/autonomous-ai-agents-agent-merge-conflict-arbiter.md) | Neutral arbiter for merge conflicts between two agents. |
| [**dynamic-workflow**](../user-guide/skills/optional/autonomous-ai-agents/autonomous-ai-agents-dynamic-workflow.md) | Plan-in-code fan-outs, adversarial verification, waves. |

## communication

| Skill | Description |
|-------|-------------|
| [**one-three-one-rule**](../user-guide/skills/optional/communication/communication-one-three-one-rule.md) | 1-3-1 decision briefs: problem, three options, one pick. |

## creative

| Skill | Description |
|-------|-------------|
| [**archify**](../user-guide/skills/optional/creative/creative-archify.md) | Validated interactive HTML diagrams, upstream-maintained. |
| [**concept-diagrams**](../user-guide/skills/optional/creative/creative-concept-diagrams.md) | Generate flat, minimal educational SVG visuals as HTML. |
| [**creative-ideation**](../user-guide/skills/optional/creative/creative-creative-ideation.md) | Generate ideas via named methods from creative practice. |
| [**design-md**](../user-guide/skills/optional/creative/creative-design-md.md) | Author/validate/export Google's DESIGN.md token spec files. |
| [**excalidraw**](../user-guide/skills/optional/creative/creative-excalidraw.md) | Hand-drawn Excalidraw JSON diagrams (arch, flow, seq). |
| [**impeccable**](../user-guide/skills/optional/creative/creative-impeccable.md) | Frontend design guidance, upstream-maintained (impeccable). |
| [**simple-english**](../user-guide/skills/optional/creative/creative-simple-english.md) | Rewrite text to ASD-STE100 Simplified Technical English. |
| [**sketch**](../user-guide/skills/optional/creative/creative-sketch.md) | Throwaway HTML mockups: 2-3 design variants to compare. |
| [**system-atlas**](../user-guide/skills/optional/creative/creative-system-atlas.md) | Build explorable isometric architecture atlases as HTML. |
| [**tldraw-offline**](../user-guide/skills/optional/creative/creative-tldraw-offline.md) | Drive and script tldraw offline canvases with an agent. |

## data-science

| Skill | Description |
|-------|-------------|
| [**jupyter-notebook**](../user-guide/skills/optional/data-science/data-science-jupyter-notebook.md) | Iterative Python via live Jupyter kernel (hamelnb). |

## devops

| Skill | Description |
|-------|-------------|
| [**docker-management**](../user-guide/skills/optional/devops/devops-docker-management.md) | Manage Docker containers, images, volumes, and Compose. |
| [**pinggy-tunnel**](../user-guide/skills/optional/devops/devops-pinggy-tunnel.md) | Zero-install localhost tunnels over SSH via Pinggy. |
| [**setup-wizard-generator**](../user-guide/skills/optional/devops/devops-setup-wizard-generator.md) | Generate a bash wizard guiding a human through manual setup. |
| [**watchers**](../user-guide/skills/optional/devops/devops-watchers.md) | Poll RSS, JSON APIs, and GitHub with watermark dedup. |

## dogfood

| Skill | Description |
|-------|-------------|
| [**adversarial-ux-test**](../user-guide/skills/optional/dogfood/dogfood-adversarial-ux-test.md) | Roleplay a hostile user to find and triage UX pain points. |

## email

| Skill | Description |
|-------|-------------|
| [**agentmail**](../user-guide/skills/optional/email/email-agentmail.md) | Use when an agent needs AgentMail CLI email inboxes. |

## finance

| Skill | Description |
|-------|-------------|
| [**3-statement-model**](../user-guide/skills/optional/finance/finance-3-statement-model.md) | Build integrated IS/BS/CF financial workbooks in Excel. |
| [**comps-analysis**](../user-guide/skills/optional/finance/finance-comps-analysis.md) | Build comparable-company valuation workbooks in Excel. |
| [**dcf-model**](../user-guide/skills/optional/finance/finance-dcf-model.md) | Build discounted cash flow valuation workbooks in Excel. |
| [**excel-author**](../user-guide/skills/optional/finance/finance-excel-author.md) | Build auditable financial workbooks headless via openpyxl. |
| [**lbo-model**](../user-guide/skills/optional/finance/finance-lbo-model.md) | Build leveraged buyout workbooks with IRR/MOIC in Excel. |
| [**merger-model**](../user-guide/skills/optional/finance/finance-merger-model.md) | Build M&A accretion/dilution workbooks in Excel. |
| [**pptx-author**](../user-guide/skills/optional/finance/finance-pptx-author.md) | Build PowerPoint decks headless with python-pptx. |
| [**stocks**](../user-guide/skills/optional/finance/finance-stocks.md) | Stock quotes, history, search, compare, crypto via Yahoo. |

## mcp

| Skill | Description |
|-------|-------------|
| [**fastmcp**](../user-guide/skills/optional/mcp/mcp-fastmcp.md) | Build, test, and deploy Python MCP servers. |
| [**mcp-oauth-remote-gateway**](../user-guide/skills/optional/mcp/mcp-mcp-oauth-remote-gateway.md) | Manual OAuth for remote MCP servers on headless gateways. |
| [**mcporter**](../user-guide/skills/optional/mcp/mcp-mcporter.md) | List, auth, and call MCP servers/tools from the terminal. |

## mlops

| Skill | Description |
|-------|-------------|
| [**accelerate**](../user-guide/skills/optional/mlops/mlops-accelerate.md) | Run PyTorch training across GPUs with minimal changes. |
| [**axolotl**](../user-guide/skills/optional/mlops/mlops-training-axolotl.md) | Axolotl: YAML LLM fine-tuning (LoRA, DPO, GRPO). |
| [**chroma**](../user-guide/skills/optional/mlops/mlops-chroma.md) | Embedding database for RAG and semantic search. |
| [**dspy**](../user-guide/skills/optional/mlops/mlops-research-dspy.md) | DSPy: declarative LM programs, auto-optimize prompts, RAG. |
| [**evaluating-llms-harness**](../user-guide/skills/optional/mlops/mlops-evaluation-evaluating-llms-harness.md) | lm-eval-harness: benchmark LLMs (MMLU, GSM8K, etc.). |
| [**faiss**](../user-guide/skills/optional/mlops/mlops-faiss.md) | Fast vector similarity search at billion scale. |
| [**flash-attention**](../user-guide/skills/optional/mlops/mlops-flash-attention.md) | Speed up long-sequence transformer training and inference. |
| [**lambda-labs**](../user-guide/skills/optional/mlops/mlops-lambda-labs.md) | On-demand GPU cloud instances for ML training. |
| [**llama-cpp**](../user-guide/skills/optional/mlops/mlops-inference-llama-cpp.md) | llama.cpp local GGUF inference + HF Hub model discovery. |
| [**modal**](../user-guide/skills/optional/mlops/mlops-modal.md) | Serverless GPU cloud for ML jobs and model APIs. |
| [**nemo-curator**](../user-guide/skills/optional/mlops/mlops-nemo-curator.md) | Curate LLM training data: dedupe, filter, PII redaction. |
| [**obliteratus**](../user-guide/skills/optional/mlops/mlops-obliteratus.md) | OBLITERATUS: abliterate LLM refusals (diff-in-means). |
| [**peft**](../user-guide/skills/optional/mlops/mlops-peft.md) | Fine-tune large LLMs with LoRA on limited GPU memory. |
| [**pytorch-fsdp**](../user-guide/skills/optional/mlops/mlops-pytorch-fsdp.md) | Fully sharded data-parallel training for large models. |
| [**pytorch-lightning**](../user-guide/skills/optional/mlops/mlops-pytorch-lightning.md) | Clean training loops with built-in distributed support. |
| [**saelens**](../user-guide/skills/optional/mlops/mlops-saelens.md) | Train sparse autoencoders to interpret model features. |
| [**segment-anything-model**](../user-guide/skills/optional/mlops/mlops-models-segment-anything-model.md) | SAM: zero-shot image segmentation via points, boxes, masks. |
| [**serving-llms-vllm**](../user-guide/skills/optional/mlops/mlops-inference-serving-llms-vllm.md) | vLLM: high-throughput LLM serving, OpenAI API, quantization. |
| [**simpo**](../user-guide/skills/optional/mlops/mlops-simpo.md) | Reference-free preference alignment, simpler than DPO. |
| [**slime**](../user-guide/skills/optional/mlops/mlops-slime.md) | RL post-training for LLMs with Megatron and SGLang. |
| [**tensorrt-llm**](../user-guide/skills/optional/mlops/mlops-tensorrt-llm.md) | High-throughput LLM inference on NVIDIA GPUs. |
| [**torchtitan**](../user-guide/skills/optional/mlops/mlops-torchtitan.md) | Pretrain LLMs at scale with PyTorch 4D parallelism. |
| [**unsloth**](../user-guide/skills/optional/mlops/mlops-training-unsloth.md) | Unsloth: 2-5x faster LoRA/QLoRA fine-tuning, less VRAM. |

## productivity

| Skill | Description |
|-------|-------------|
| [**box**](../user-guide/skills/optional/productivity/productivity-box.md) | Box manages cloud files, sharing, search, and metadata. |
| [**decision-questionnaire**](../user-guide/skills/optional/productivity/productivity-decision-questionnaire.md) | Turn an unanswerable decision into a questionnaire doc. |
| [**here-now**](../user-guide/skills/optional/productivity/productivity-here-now.md) | Publish sites to &#123;slug&#125;.here.now and store files in Drives. |
| [**live-dashboard**](../user-guide/skills/optional/productivity/productivity-live-dashboard.md) | Build self-updating dashboards from live sources. |

## research

| Skill | Description |
|-------|-------------|
| [**blogwatcher**](../user-guide/skills/optional/research/research-blogwatcher.md) | Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool. |
| [**darwinian-evolver**](../user-guide/skills/optional/research/research-darwinian-evolver.md) | Evolve prompts/regex/SQL/code with Imbue's evolution loop. |
| [**domain-intel**](../user-guide/skills/optional/research/research-domain-intel.md) | Passive recon of subdomains, SSL certs, WHOIS, and DNS. |
| [**gitnexus-explorer**](../user-guide/skills/optional/research/research-gitnexus-explorer.md) | Serve an interactive codebase knowledge graph web UI. |
| [**llm-wiki**](../user-guide/skills/optional/research/research-llm-wiki.md) | Karpathy's LLM Wiki: build/query interlinked markdown KB. |
| [**osint-investigation**](../user-guide/skills/optional/research/research-osint-investigation.md) | Follow the money via public records and sanctions data. |
| [**parallel-cli**](../user-guide/skills/optional/research/research-parallel-cli.md) | Agent-native web search, deep research, and enrichment. |
| [**qmd**](../user-guide/skills/optional/research/research-qmd.md) | Hybrid local search over notes, docs, and transcripts. |
| [**rss-feeds**](../user-guide/skills/optional/research/research-rss-feeds.md) | Read RSS, Atom, JSON feeds; discover feeds behind a page. |
| [**scrapling**](../user-guide/skills/optional/research/research-scrapling.md) | Scrape sites with stealth browsing and Cloudflare bypass. |

## security

| Skill | Description |
|-------|-------------|
| [**1password**](../user-guide/skills/optional/security/security-1password.md) | Set up op CLI, sign in, and read or inject secrets. |
| [**oss-forensics**](../user-guide/skills/optional/security/security-oss-forensics.md) | GitHub supply-chain forensics: recovery, IOCs, reporting. |
| [**web-pentest**](../user-guide/skills/optional/security/security-web-pentest.md) | Authorized web pentest: recon, proof-based exploits, report. |

## software-development

| Skill | Description |
|-------|-------------|
| [**ast-grep**](../user-guide/skills/optional/software-development/software-development-ast-grep.md) | AST-aware structural code search and rewrite via ast-grep. |
| [**code-wiki**](../user-guide/skills/optional/software-development/software-development-code-wiki.md) | Generate wiki docs + Mermaid diagrams for any codebase. |
| [**grill-me**](../user-guide/skills/optional/software-development/software-development-grill-me.md) | Adversarial plan interview before implementation. |
| [**hermes-agent-skill-authoring**](../user-guide/skills/optional/software-development/software-development-hermes-agent-skill-authoring.md) | Author in-repo SKILL.md files: frontmatter and structure. |
| [**node-inspect-debugger**](../user-guide/skills/optional/software-development/software-development-node-inspect-debugger.md) | Debug Node.js via --inspect + Chrome DevTools Protocol CLI. |
| [**pr-lens**](../user-guide/skills/optional/software-development/software-development-pr-lens.md) | Draw code changes as animated architecture/data-flow SVGs. |
| [**python-debugpy**](../user-guide/skills/optional/software-development/software-development-python-debugpy.md) | Debug Python: pdb REPL + debugpy remote (DAP). |
| [**rest-graphql-debug**](../user-guide/skills/optional/software-development/software-development-rest-graphql-debug.md) | Debug REST/GraphQL APIs: status codes, auth, schemas, repro. |
| [**subagent-driven-development**](../user-guide/skills/optional/software-development/software-development-subagent-driven-development.md) | Execute plans via delegate_task subagents (2-stage review). |

## web-development

| Skill | Description |
|-------|-------------|
| [**cloudflare-temporary-deploy**](../user-guide/skills/optional/web-development/web-development-cloudflare-temporary-deploy.md) | Deploy a Worker live, no account, via wrangler --temporary. |
| [**har-derived-api-client**](../user-guide/skills/optional/web-development/web-development-har-derived-api-client.md) | Record a site's XHR into a HAR, derive an HTTP client. |
| [**page-agent**](../user-guide/skills/optional/web-development/web-development-page-agent.md) | Embed an in-page natural-language GUI copilot in web apps. |
| [**publish-site**](../user-guide/skills/optional/web-development/web-development-publish-site.md) | Versioned site deploys to GitHub/Cloudflare/Netlify Pages. |
| [**scrollcraft**](../user-guide/skills/optional/web-development/web-development-scrollcraft.md) | Premium scroll-driven landing pages; scroll = timeline. |

---

## Contributing Optional Skills

To add a new optional skill to the repository:

1. Create a directory under `optional-skills/<category>/<skill-name>/`
2. Add a `SKILL.md` with standard frontmatter (name, description, version, author)
3. Include any supporting files in `references/`, `templates/`, or `scripts/` subdirectories
4. Submit a pull request — the skill will appear in this catalog and get its own docs page once merged
