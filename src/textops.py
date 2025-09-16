# src/textops.py

from typing import List


def unique_words_preserve_order(words: List[str]) -> List[str]:
    """
    Return a list of unique words in the order they first appeared.
    """
    seen = set()
    result = []
    for w in words:
        if w not in seen:
            seen.add(w)
            result.append(w)
    return result


def top_k_frequent_first_tie(words: List[str], k: int) -> List[str]:
    """
    Return the top k most frequent words.
    - If frequencies tie, pick the one that appeared first in the list.
    - Raises ValueError if k <= 0.
    """
    if k <= 0:
        raise ValueError("k must be positive")

    freq = {}
    first_seen = {}

    for idx, w in enumerate(words):
        freq[w] = freq.get(w, 0) + 1
        if w not in first_seen:
            first_seen[w] = idx

    # Sort by (-count, first appearance index)
    sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], first_seen[w]))

    return sorted_words[:k]


def redact_words(words: List[str], to_redact: List[str]) -> List[str]:
    """
    Replace all words in `to_redact` with "***".
    """
    to_redact_set = set(to_redact)
    return ["***" if w in to_redact_set else w for w in words]
