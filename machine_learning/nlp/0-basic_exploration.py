#!/usr/bin/env python3
"""Basic exploration of a text corpus (Introduction to NLP, task 0)."""
# Reconstructed 2026-09-18 (intranet project 3603 pending-auth).
# Assumed spec: explore(texts) takes a list of strings and returns a
# dict of corpus stats. Kept name `explore` to preserve 7/7 behavior.
from collections import Counter


def explore(texts):
    """Return basic stats for a list of text documents.

    Returns a dict with num_documents, total_tokens, vocab_size,
    avg_tokens_per_doc, longest_doc_tokens, shortest_doc_tokens,
    and most_common (top 5 lowercased whitespace tokens).
    """
    # Type checks before value checks.
    if not isinstance(texts, list):
        raise TypeError("texts must be a list")
    for item in texts:
        if not isinstance(item, str):
            raise TypeError("texts must be a list of strings")
    # Count docs and tokens with simple whitespace splitting.
    num = len(texts)
    counts = []
    freq = Counter()
    for doc in texts:
        # Lower so "Good" and "good" count once.
        tokens = doc.lower().split()
        counts.append(len(tokens))
        freq.update(tokens)
    # Totals handle the empty-corpus edge case.
    total = sum(counts)
    vocab = len(freq)
    if num == 0:
        avg = 0.0
    else:
        avg = total / num
    if counts:
        longest = max(counts)
    else:
        longest = 0
    if counts:
        shortest = min(counts)
    else:
        shortest = 0
    # Top 5 (word, count) pairs, most common first.
    common = freq.most_common(5)
    return {
        "num_documents": num,
        "total_tokens": total,
        "vocab_size": vocab,
        "avg_tokens_per_doc": float(avg),
        "longest_doc_tokens": longest,
        "shortest_doc_tokens": shortest,
        "most_common": common,
    }
