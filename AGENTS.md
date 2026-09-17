# DLH Workflow Contract

This file governs every DLH (Holberton ML) task in this repo. Follow the 5-step
rhythm in order. The goal is one consistent loop: explain, template, student
codes, verify, checker.

## The Task Rhythm

1. **Prepare**
   - Fetch the reference implementations from both known-good forks:
     `Teheremiti/holbertonschool-machine_learning` and
     `dassantoss/holbertonschool-machine_learning` (raw.githubusercontent.com).
   - Inspect the project's data files (shapes, dtypes, keys) if present.
   - Create the template file: full class skeleton from the previous task,
     intranet-spec docstrings, `pass`/stub bodies for the new method, header
     comment `(Based on N-*.py)`. **No solution code in the template.**
   - Ingest the project's intranet resources: summarize articles, pull video
     transcripts, capture crucial bits into `<project>/RESOURCES.md`. Runs
     once per project at the first task's Prepare; see
     `RESOURCE_INGESTION.md`. Never ingest mid-task.
2. **Explain** — use the `RESOURCE_INGESTION.md` and DeepTutor Research Workflow
    plus the guided cheat sheet below.
3. **Student codes** — the student fills the stubs step by step. Answer
   questions; never put solution code into a concept explanation unless asked.
4. **Verify** — run the verification battery (below) before the student submits.
5. **Check** — student runs the official checker; diagnose any failure against
   the reference forks.

### Guided cheat sheet (start of every task)

At the start of each task, output a 1-page copy-paste-friendly cheat sheet
covering only the functions/structures that task needs: an API table with
TF version-accurate signatures (defaults vs what to explicitly set for the
task), one minimal per-layer usage snippet each (NOT the full task
solution), common pitfalls (wrong namespace like `K.Add` vs
`K.layers.Add`, missing assignment, padding, axis, seed), plus a 3-line
usage-order reminder. Format example: the Identity Block `K` cheat sheet
(`Conv2D`, `BatchNormalization(axis=3)`, `Activation('relu')`,
`Add()([X, A_prev])` list-arg, `HeNormal(seed=0)`).


## DeepTutor Research Workflow

The `deeptutor` MCP server is connected (`DEEPTUTOR_HOME=~/Documents/deeptutor-workspace`, deeptutor 1.6.x via pipx — canonical KB/data root; see share `dPGgbDrd` Pi-hosting plan for packaging notes). This project's DeepTutor knowledge base is **ai-book-kb** — 1181 chunks from *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow, 3rd ed.* (`llamaindex`, `unsloth/bge-small-en-v1.5` 384d, local gateway `172.18.0.1:18080/18081`). Prefer this KB for grounded ML questions (only KB with content; `opencode` KB exists but is empty).

- Read-only tools: `list_knowledge_bases` / `get_knowledge_base_info(name=...)` (metadata, work offline). `list_sessions` is broken (missing `deeptutor.services.session.manager` module) — do not rely on it.
- Asking: `search_knowledge_base(name="ai-book-kb", query=..., mode="hybrid"|"vector")` for fast retrieval with page citations, then `ask_deeptutor` (`message`, `knowledge_bases: ["ai-book-kb"]`, `capability: "chat"` or `deep_solve`/`deep_question`) for synthesis; reuse the returned `session_id` for follow-ups (reuse untested 2026-09-16 — `ask` timed out before issuing one).
- Gateway dependency: both query tools need the local gateway (`:18080` chat, `:18081` embeddings). If down, `search` returns `All connection attempts failed` (hybrid fails fast, vector hangs to MCP timeout) and `ask_deeptutor` times out — verify with `curl` to the gateway and restart its container before retrying.
- Example (deep_cnns ResNet task): `search_knowledge_base(name="ai-book-kb", query="residual connection identity block ResNet", mode="hybrid")` → `ask_deeptutor(message="Explain residual connections / identity blocks from the Hands-On ML book (cite pages)", knowledge_bases=["ai-book-kb"], capability="chat")`. Keep `knowledge_bases` explicit; if the KB does not cover the question, say so.
- Local gateway is `http://172.18.0.1:18080/v1` + `http://172.18.0.1:18081/v1/embeddings`; no external API key needed. Never create/update/delete KBs without explicit approval.

## Conventions and Lessons

- Error messages must match the intranet spec character-for-character.
- Type checks before value checks; validation order per the spec.
- Student comment style: short plain-language `#` comment per block.
- Reference-fork quirks are checker fingerprints — match them, don't "fix"
  them: `1.0000001 - A` in cost, `range(iterations + 1)` loop, `argmax + 2`
  (PCA), `np.random.standard_normal` == `np.random.randn` (both N(0,1)).
- **Never leave module-level executable code** in task files. Import must be
  silent and fast (<1s). Test harnesses go in a separate file or not at all.
- Data files go in `.gitignore` with explicit paths (mnist txt files, npz
  datasets). Never commit them.
- When a project's tasks are done, rewrite its README per
  `STUDY_GUIDE_TEMPLATE.md`.
- Verification environment: **always** run tests and code with `my-venv`
  (`my-venv/bin/python`, numpy 2.4.4, matplotlib 3.11.0). Never system
  `python3` for task code, tests, or verification runs.
- TensorFlow projects (keras, cnn, deep_cnns, ...): TF 2.15 has no Python
  3.14 wheels, so my-venv cannot run it. Use `tf-venv` (`tf-venv/bin/python`,
  python 3.11, tensorflow 2.15.0, numpy 1.25.2) — mirrors the checker. Both
  venvs are gitignored; create with `uv` if missing.

## Verification Battery

Run before the student submits, for every task file:

- [ ] `pycodestyle` clean
- [ ] compile + import smoke test: no module-level side effects, no output,
      no `RuntimeWarning` under `my-venv/bin/python -W error` (or
      `tf-venv/bin/python` for TF tasks)
- [ ] attribute shapes and initial values match the spec
- [ ] every exception type and message exact
- [ ] behavioral anchors (cost decreases after training, sigmoid output in
      (0,1), threshold at 0.5, gradient matches finite differences)
- [ ] for graph tasks: mocked-`plt` call order (plot, xlabel, ylabel, title,
      show)
- [ ] `RESOURCES.md`: every Read-or-watch resource has a summary or an
      explicit status marker and a Date line. No silent drops.

## Lessons Log

Append new lessons here as they are learned; the file is meant to grow.

- 2026-08-07: verification and test runs always use `my-venv`, never system
  `python3` (keeps numpy 2.4.4 / matplotlib consistent with the checker's
  tooling and available everywhere).
- 2026-08-07: a test harness pasted at the bottom of a task file runs on every
  `import` (7-neuron.py: 20s import + stdout pollution). Harnesses live
  outside task files, or in a `__main__` guard in a scratch file.
- 2026-08-11: intranet rltoken links are auth-gated and relative — prefix
  `https://intranet-dlh.hbtn.io` and follow them inside the authenticated
  playwright context only.
- 2026-08-11: run the session health check before any ingestion run
  (`/projects/current` must not redirect to `/auth/login`); else ask the user
  for one FIDO sign-in. The active profile has the freshest `Default/Cookies`
  mtime, not the newest profile dir.
- 2026-08-11: paywall chain for articles: archive.org first, then the
  playwright context, then mark `paywalled` — never summarize a stub.
- 2026-08-12: `tf-venv` has no pip (`python -m pip` → "No module named pip";
  no pip script in `bin/`). Add packages with `uv pip install --python
  tf-venv/bin/python` or `python -m ensurepip` first (pip 24.0 available).
- 2026-08-12: the `my-venv/bin/pip` shebang is fixed (rewritten 2026-08-11 to
  the new repo path); direct `my-venv/bin/pip` works. The earlier stale-
  shebang lesson is obsolete.
- 2026-08-12: `my-venv` is ignored by its own nested `my-venv/.gitignore`
  (`*`), not the root `.gitignore`; only `tf-venv/` is listed at root. Both
  venvs are safe from commits.
- 2026-08-11: this repo is public. Raw transcripts never commit; summaries
  only, own words, no verbatim text longer than one sentence.
- 2026-09-16: cheat-sheet-first workflow — open every task with the guided
  cheat sheet (API table + minimal snippets + pitfalls + usage order) before
  templating, so the student codes from the sheet, not from solution text.
- 2026-09-16: DeepTutor section updated from share `dPGgbDrd` (Pi-hosting plan:
  deeptutor 1.6.x via pipx, canonical `DEEPTUTOR_HOME` data root, LLM gateway
  ports) + live test: `list_knowledge_bases` / `get_knowledge_base_info`
  work offline (ai-book-kb ready, 1181 chunks, signature `d7b149ea281bad39`);
  `list_sessions` broken (missing session.manager module); `search`/`ask`
  need the local gateway — down today (`curl` 000, only open-notebook/
  surrealdb containers up), so hybrid `search` fails fast, vector `search`
  and `ask` time out. Check gateway before relying on DeepTutor answers.
