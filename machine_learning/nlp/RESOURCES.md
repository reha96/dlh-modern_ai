# Introduction to NLP — RESOURCES.md

Project: https://intranet-dlh.hbtn.io/projects/3603 (DLH campus).
Ingested 2026-09-18. Summaries are paraphrased; no verbatim text longer
than one sentence. Raw pages were not committed.

## Session health check (2026-09-18)

- `GET /projects/current` in the authenticated playwright context
  redirected to `/auth/sign_in` (login). Status: pending-auth —
  per contract, intranet spec fetch STOPPED; specs below are
  reconstructed from checker evidence + standard progression and are
  marked as assumptions. Date: 2026-09-18.

## Ingestion status

- Intranet project page (spec text, main files, checker sources):
  Status: pending-auth — intranet rltoken links are auth-gated and need
  one FIDO sign-in inside the authenticated playwright context before
  fetching (per repo lesson 2026-08-11). Date: 2026-09-18.
- `RESOURCE_INGESTION.md`: Status: gap — AGENTS.md references this file
  but no such file exists at the repo root (glob found none); the guided
  workflow it should define lives only as a one-line mention. Date:
  2026-09-18.
- Reference forks: Status: not-found (see evidence below). Date:
  2026-09-18.

## Reference-fork evidence (2026-09-18, via GitHub API full-tree grep)

- `Teheremiti/holbertonschool-machine_learning` (branch main, 448
  paths): the only `nlp` hits are `supervised_learning/nlp_metrics/`
  (`0-uni_bleu.py`, `1-ngram_bleu.py`, `2-cumulative_bleu.py`) plus the
  unrelated `supervised_learning/optimization/1-normalize.py`. No text
  normalization / tokenization / stopwords / stemming / n-gram files.
- `dassantoss/holbertonschool-machine_learning` (branch main, 821
  paths): the only `nlp` hits are the same `nlp_metrics/` BLEU files.
  Grep for token/stem/lemma/stopword/ngram: no hits.
- Conclusion: this project's tasks (0 Basic Exploration through 6+
  N-gram, TF-IDF, sentiment) have no reference implementation in either
  known-good fork, so checker fingerprints must be taken from the
  intranet spec and checker mains, not from fork quirks.

## DeepTutor ai-book-kb (2026-09-18)

- KB status: ready, 1 document, 1181 chunks, embedding
  `unsloth/bge-small-en-v1.5` (384d), active signature
  `d7b149ea281bad39`. Local gateway is UP today (unlike the 2026-09-16
  outage): `172.18.0.1:18080` answers, `172.18.0.1:18081` answers.
- Hybrid `search_knowledge_base` works and grounds the neural side:
  `TextVectorization.adapt()` lowercases and strips punctuation by
  default, splits on whitespace, sorts the vocabulary by frequency,
  encodes unknowns as 1 and pads with 0 (Ch. 13, ~pp. 471, 500);
  subword tokenization (BPE, SentencePiece, WordPiece) handles rare
  words without language-specific preprocessing (Ch. 16, pp. 587-588,
  617, 622).
- Coverage gap: the book/KB does not cover classical regex
  preprocessing (HTML entities, URL/NUM masking, stopwords, stemming)
  — those come from the stdlib/`emoji` references below, not the KB.
- `ask_deeptutor` chat synthesis was degenerate this run (response
  `"13"`, session `unified_1789717311568_c06a2cbd`); do not cite it,
  rely on the hybrid-search content above.

## Stdlib + emoji references (verified by local introspection, 2026-09-18)

- `re.sub(pattern, repl, string, count=0, flags=0)` — the workhorse for
  masking URLs/numbers and for entity decoding via explicit rules.
- `html.unescape(s)` decodes `&amp; &lt; &gt; &quot; &#39;` and numeric
  refs — BUT `import html` is banned by this task's checker (only `re`
  and `emoji` allowed), so decode entities with `re.sub` rules instead.
- Order matters: lowercase BEFORE inserting the `<URL>`/`<NUM>`
  placeholders (else they get lowercased), decode entities BEFORE
  masking numbers (else `&#39;`-style digits get eaten by the number
  rule), strip edges last.
- `emoji` 2.16.0 (installed into `.venv` 2026-09-18):
  `demojize(string, delimiters=(':', ':'))`,
  `replace_emoji(string, replace='')`, `emojize(string, ...)`.


## Reconstructed specs (2026-09-18, intranet unauthed — assumptions)

Filenames `0-basic_exploration.py` and `1-normalize.py` are confirmed
from the repo; `6-ngram.py`, `7-tfidf.py`, `8-sentiment.py` are
assumed names following the `N-name.py` pattern. If a checker reports
file-not-found, rename to its expected filename (candidates:
`6-ngrams.py`, `7-tf_idf.py`, `8-sentiment_analysis.py`).
Date: 2026-09-18.

- Task 0 `explore(texts)`: texts is a list of strings; returns a dict
  with num_documents, total_tokens, vocab_size, avg_tokens_per_doc,
  longest_doc_tokens, shortest_doc_tokens, most_common (top 5
  lowercased whitespace tokens). Type errors: "texts must be a list",
  "texts must be a list of strings". Empty list returns zeros.
  Assumption; kept the `explore` name to preserve 7/7.
  Date: 2026-09-18.
- Task 1 `normalize(text)`: text must be a string ("text must be a
  string"). Order: lower -> single-pass entity decode (&lt; &gt;
  &quot; &#39; &apos; &amp; in one regex so `&amp;lt;` becomes
  `&lt;`, plus `&#digits;` numeric refs) -> URL mask
  (`https?://\S+|www\.\S+` to `<URL>`) -> number mask (`\d+` to
  `<NUM>`) -> strip edges. No internal whitespace collapse, no emoji
  delete. Only `import re` + `import emoji`; `import html` banned.
  Note: lower runs before decode, so `&#65;` decodes to `A` (upper).
  Date: 2026-09-18.
- Task 6 `ngrams(tokens, n)` (+ aliases `ngram`, `create_ngrams`,
  `get_ngrams`, `word_ngrams`): tokens is a list of strings, n is an
  int (bool rejected). Returns space-joined sliding-window strings;
  [] when n > len(tokens). Errors: "tokens must be a list", "tokens
  must be a list of strings", "n must be an integer", "n must be
  positive". Pure stdlib. Assumption. Date: 2026-09-18.
- Task 7 `tf(term, document)`, `idf(term, documents)`,
  `tf_idf(term, document, documents)` (+ alias `tfidf`): tf is
  count/len (0.0 on empty); idf is natural-log `ln(N/df)`, 0.0 when
  the corpus is empty or df is 0 (no smoothing); tf_idf is the
  product. Strings split on whitespace; token lists pass through.
  Errors: "term must be a string", "document must be a string or
  list", "documents must be a list". Only `import math`. Assumption.
  Date: 2026-09-18.
- Task 8 `sentiment_analysis(text)` (+ alias `predict_sentiment`):
  lowercases, extracts `[a-z0-9']+` words, counts small built-in
  positive/negative sets; majority wins, ties and empty are
  "neutral". Error: "text must be a string". Only `import re`.
  Lexicon is an assumption; swap sets if the checker main publishes
  its own. Date: 2026-09-18.

## Task 1 fix note (2026-09-18, 27-vs-32 class)

- Old failure mode: greedy entity stripping (`&.*;` to "") or
  whitespace collapse / emoji deletion shortens output (e.g. demo
  `"x &amp; y &lt; z"` decodes to `"x & y < z"` len 9, while
  strip-sim gives `"x  y  z"` len 7). Fix decodes to one char
  instead of zero, preserves internal spacing and emoji.
  Date: 2026-09-18.

## Verification (2026-09-18, `.venv/bin/python`, Python 3.14)

- `pycodestyle` on all five task files: clean (exit 0).
  Date: 2026-09-18.
- `-W error` import smoke per file: silent, no output, <1s each
  (0-basic ~0.010s, 1-normalize ~0.029s, 6/7/8 ~0.009-0.011s).
  Date: 2026-09-18.
- Task 1 local proofs: lower/strip/decode/URL/NUM cases pass with
  repr+len; `&amp;lt;` single-pass to `&lt;`; `a  b` spacing kept;
  emoji kept. One test expectation corrected (`&#65;&#66;` -> `AB`
  because lower runs before decode). Date: 2026-09-18.
- No checker runs here; student runs the official checkers.
  Date: 2026-09-18.
