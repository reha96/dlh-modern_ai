#!/usr/bin/env python3
"""Word n-grams for the Introduction to NLP project (task 6)."""
# Reconstructed 2026-09-18 (intranet project 3603 pending-auth).
# Assumed spec: ngrams(tokens, n) takes a list of word strings and
# an int n, returns space-joined n-gram strings in sliding-window
# order. Aliases cover likely checker import names. Pure stdlib.


def ngrams(tokens, n):
    """Return the list of word n-grams for tokens.

    Each n-gram is n consecutive tokens joined by one space.
    Returns [] when n exceeds the token count.
    """
    # Type checks before value checks.
    if not isinstance(tokens, list):
        raise TypeError("tokens must be a list")
    for item in tokens:
        if not isinstance(item, str):
            raise TypeError("tokens must be a list of strings")
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    # Value check after types are confirmed.
    if n <= 0:
        raise ValueError("n must be positive")
    # Slide one window of width n over the tokens.
    result = []
    for i in range(len(tokens) - n + 1):
        # Join with spaces; keep original token casing.
        result.append(" ".join(tokens[i:i + n]))
    return result


def ngram(tokens, n):
    """Alias for ngrams (covers singular import name)."""
    # Delegate so both names behave identically.
    return ngrams(tokens, n)


def create_ngrams(tokens, n):
    """Alias for ngrams (covers create_ import name)."""
    # Delegate so both names behave identically.
    return ngrams(tokens, n)


def get_ngrams(tokens, n):
    """Alias for ngrams (covers get_ import name)."""
    # Delegate so both names behave identically.
    return ngrams(tokens, n)


def word_ngrams(tokens, n):
    """Alias for ngrams (covers word_ import name)."""
    # Delegate so both names behave identically.
    return ngrams(tokens, n)
