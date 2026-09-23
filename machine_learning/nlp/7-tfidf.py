#!/usr/bin/env python3
"""Term frequency / inverse document frequency (NLP task 7)."""
# Reconstructed 2026-09-18 (intranet project 3603 pending-auth).
# Assumed spec: tf(term, document), idf(term, documents), and
# tf_idf(term, document, documents) with tf = count/len and
# idf = ln(N/df) using natural log. Strings are split on
# whitespace; token lists pass through. Pure stdlib (math only).
import math


def _as_tokens(document):
    """Return document as a token list (split strings)."""
    # Accept a raw string or a ready token list.
    if isinstance(document, str):
        return document.split()
    return list(document)


def tf(term, document):
    """Return the term frequency of term in document."""
    # Type checks before value checks.
    if not isinstance(term, str):
        raise TypeError("term must be a string")
    if not isinstance(document, (str, list)):
        raise TypeError("document must be a string or list")
    tokens = _as_tokens(document)
    # Empty document has no frequency.
    if len(tokens) == 0:
        return 0.0
    # Count exact matches over total tokens.
    count = tokens.count(term)
    return count / len(tokens)


def idf(term, documents):
    """Return the inverse document frequency of term."""
    # Type checks before value checks.
    if not isinstance(term, str):
        raise TypeError("term must be a string")
    if not isinstance(documents, list):
        raise TypeError("documents must be a list")
    total = len(documents)
    # No corpus means no signal.
    if total == 0:
        return 0.0
    # Count docs containing the term at least once.
    found = 0
    for doc in documents:
        tokens = _as_tokens(doc)
        if term in tokens:
            found += 1
    # Unseen term carries no weight (avoids log(0) crash).
    if found == 0:
        return 0.0
    # Natural log of N/df (no smoothing, per assumption).
    return math.log(total / found)


def tf_idf(term, document, documents):
    """Return tf(term, document) * idf(term, documents)."""
    # Type checks reuse the helpers; keep order type-first.
    if not isinstance(term, str):
        raise TypeError("term must be a string")
    # Multiply the two component scores.
    return tf(term, document) * idf(term, documents)


def tfidf(term, document, documents):
    """Alias for tf_idf (covers no-underscore import name)."""
    # Delegate so both names behave identically.
    return tf_idf(term, document, documents)
