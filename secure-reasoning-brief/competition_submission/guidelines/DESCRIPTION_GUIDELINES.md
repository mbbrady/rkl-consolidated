# Kaggle Capstone Description Guidelines

Use this checklist to verify that `competition_submission/description` is clear, within limits, and aligned with both the provided outline and the official scoring criteria.

## Global Requirements
- [ ] Length is **≤ 1500 words** (run `wc -w competition_submission/description`).
- [ ] Written for **judges and general ML practitioners**, not just course instructors.
- [ ] Clearly states **what you built**, **why it matters**, and **what evidence you have** (runs, data, telemetry).
- [ ] Links referenced in the text (GitHub, Kaggle, Hugging Face, demo) all exist and are stable.

## Category 1: The Pitch (30 pts)

### Core Concept & Value (15 pts)
- [ ] Central idea is stated in **1–2 crisp sentences** (what the agent system is and who it serves).
- [ ] Relevance to the **Agents for Good** track is explicit (education / healthcare / sustainability / governance / public-good angle).
- [ ] The **role of agents is central**, not incidental (multi-agent coordination is part of the value, not just implementation detail).
- [ ] Innovation is clear: explains what’s **novel or differentiated** vs a normal summarizer or single-agent tool.

### Writeup Quality (15 pts)
- [ ] Problem → solution → value story is **easy to follow** for a new reader.
- [ ] The outline sections (Problem, Why Agents, What You Created, Demo, The Build, If I Had More Time) flow logically and avoid repetition.
- [ ] Architecture is described at a level that **non-authors could sketch it** (phases, major components, trust boundary).
- [ ] Mentions **concrete impact** or potential impact (time saved, risk reduced, research support, etc.), even if approximate.

## Problem Statement
- [ ] Clearly describes **who** has the problem (e.g., AI practitioners, governance teams, sensitive-data orgs).
- [ ] Explains **what pain** they experience (information overload, trust gap around secure data handling).
- [ ] States why this is **important now** (volume of research, need for secure reasoning).
- [ ] Connects the problem explicitly to **secure reasoning / Type III** rather than generic summarization.

## Why Agents?
- [ ] Explains why a **single model / simple script** is insufficient (local-only vs cloud-only tradeoffs, adaptability, governance).
- [ ] Describes how **specialized agents** map to subproblems (discovery, processing, QA, governance, publication).
- [ ] Makes the **trust boundary** explicit (local vs cloud; raw data vs derived summaries).
- [ ] Mentions benefits like **resilience, observability, and governance-by-design** that emerge from a multi-agent design.

## What You Created (Architecture)
- [ ] Summarizes the **overall pipeline** in 2–3 short paragraphs (phases or layers).
- [ ] Names the **key agent groups** (discovery, processing, governance, publication, monitoring).
- [ ] Highlights the **Type III boundary** and how it’s enforced (what never leaves local; what cloud sees).
- [ ] Briefly mentions **Phase-0 telemetry** as part of the architecture (not just an afterthought).

## Demo
- [ ] Describes what someone **sees in the demo** (daily briefs, weekly blog, telemetry/sample data).
- [ ] Connects demo elements to **real usage** (e.g., “morning brief”, “weekly synthesis”, “ops dashboard”).
- [ ] Provides **at least one concrete link** (HTML demo, GitHub path, or sample brief file).
- [ ] Emphasizes that the demo is **backed by actual runs**, not just a mock.

## The Build
- [ ] Lists the **key technologies and models** (Ollama llama3.2:3b, Gemini 2.0, Python, cron, Parquet).
- [ ] Explains the **local vs cloud** split in implementation (where each runs, how they’re wired).
- [ ] Mentions **Phase-0 research telemetry** and how it’s produced (artifact types, purpose).
- [ ] Includes a short note on **how you developed it** (use of Claude/ChatGPT, human review).

## If I Had More Time
- [ ] Outlines **next concrete steps** (e.g., more agents, richer dashboards, CI/CD, more sources).
- [ ] Connects at least one next step to **course themes** (AgentOps, observability, security, interoperability).
- [ ] Differentiates between **near-term polish** (days/weeks) and **longer-term research directions**.

## Category 2: The Implementation (70 pts) – What the Description Should Surface

### Technical Implementation (50 pts)
- [ ] The description **explicitly mentions** at least **3 key course features**, for example:
  - Multi-agent system: parallel / sequential / loop agents, LLM-powered agents.
  - Tools: custom tools, external APIs (Gemini, Ollama), retrieval, file or DB tools.
  - Sessions & memory: state management across runs, telemetry used as “memory”.
  - Observability: logs, traces, metrics, Phase-0 research telemetry.
  - Agent evaluation: LLM-as-a-judge, quality checks, governance ledger.
  - Agent deployment: cron, cluster, or cloud runtime.
- [ ] Makes clear **how agents are orchestrated** (sequential phases, any parallelism, loops / retries).
- [ ] Clearly distinguishes **local vs cloud** execution and how data safety is maintained (Type III boundary).
- [ ] Mentions any **long-running operations** or session continuity (e.g., repeated daily/weekly runs).
- [ ] Highlights that the system has **real execution history** (number of runs, days in production, sample volumes).

### Documentation / Repo Pointers (20 pts)
- [ ] The description points to the main **README** and/or `SUBMISSION_PACKAGE.md` as the entry point for deeper docs.
- [ ] Briefly notes where judges can find:
  - Architecture diagrams (`ARCHITECTURE.md` / `ARCHITECTURE_DIAGRAM.md`).
  - Telemetry documentation (`TELEMETRY_*` files).
  - Sample data (`competition_submission/sample_telemetry`, `content/briefs`).
- [ ] Avoids duplicating full docs; instead, **summarizes** and links so judges know there is strong documentation behind the writeup.

## Bonus Alignment (20 pts) – Make Sure It’s Obvious
- [ ] Mentions **Gemini** explicitly and how it powers at least one agent (QA, insight generation, weekly synthesis).
- [ ] Mentions **deployment evidence** (cron, homelab, cluster, or cloud runtime) so judges can award deployment bonus.
- [ ] If you’re submitting a video, the description:
  - Stays consistent with the video’s problem/solution/architecture story.
  - References the video link or filename (if allowed by the competition form).

## Kaggle Submission Form Checklist
- [ ] **Title** is short, memorable, and reflects the core idea.
- [ ] **Subtitle** adds one line of context (who it’s for / what it does).
- [ ] **Card & Thumbnail Image** chosen that visually matches the project (e.g., brief screenshot, architecture diagram, or RKL branding).
- [ ] **Submission Track** correctly set to **Agents for Good**.
- [ ] **Media Gallery**: YouTube URL added if you’re submitting a video, or explicitly skipped if not.
- [ ] **Project Description** field uses exactly the contents of `competition_submission/description` (or a lightly formatted version) and stays under **1500 words**.
- [ ] **Attachments** include at least one working code link:
  - Public GitHub repo pointing to `rkl-consolidated/secure-reasoning-brief` (with tag/commit for the submission), **or**
  - Kaggle Notebook containing the agent code and documentation.

## Course & Criteria Alignment (Sanity Checks)
- [ ] At least one sentence connects the project to **multi-agent systems** (Day 3 concepts).
- [ ] At least one sentence connects to **AgentOps / telemetry / quality** (Days 4–5).
- [ ] Mentions that the system has **run in production over multiple days** with real telemetry.
- [ ] Avoids deep internal course jargon that an external judge wouldn’t recognize, or briefly explains it.
