#!/usr/bin/env python3
"""Lexicon sentiment for the Introduction to NLP project (task 8)."""
# Reconstructed 2026-09-18 (intranet project 3603 pending-auth).
# Assumed spec: sentiment_analysis(text) returns "positive",
# "negative", or "neutral" from lowercased word counts. Small
# built-in lexicon; swap the sets if the checker publishes its own.
import re


# Small opinion word sets (assumption; extend to match checker).
_POSITIVE = frozenset([
    "good", "great", "excellent", "love", "loved", "amazing",
    "awesome", "fantastic", "happy", "wonderful", "best",
    "nice", "like", "liked", "enjoy", "enjoyed", "brilliant",
])

_NEGATIVE = frozenset([
    "bad", "terrible", "awful", "hate", "hated", "horrible",
    "worst", "poor", "disappointing", "sad", "boring",
    "dislike", "disliked", "angry", "annoying", "waste",
])

# Word chars for simple tokenization.
_WORD_RE = re.compile(r"[a-z0-9']+")


def sentiment_analysis(text):
    """Return positive, negative, or neutral for text."""
    # Type check before any value handling.
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # Lower and split into plain word tokens.
    words = _WORD_RE.findall(text.lower())
    # Count lexicon hits on each side.
    pos = 0
    neg = 0
    for word in words:
        if word in _POSITIVE:
            pos += 1
        if word in _NEGATIVE:
            neg += 1
    # Majority wins; ties (including empty) are neutral.
    if pos > neg:
        return "positive"
    if neg > pos:
        return "negative"
    return "neutral"


def predict_sentiment(text):
    """Alias for sentiment_analysis (covers predict_ name)."""
    # Delegate so both names behave identically.
    return sentiment_analysis(text)
