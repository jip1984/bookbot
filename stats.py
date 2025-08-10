from typing import Dict, List

def number_of_words(text):

    return len(text.split())

def count_characters(text: str) -> Dict[str, int]:
    """
    Return a dict mapping each character (lowercased) to its count.
    Includes spaces, punctuation, digits, etc.
    """
    counts: Dict[str, int] = {}
    for ch in text:
        ch = ch.lower()
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_characters(char_counts: Dict[str, int]) -> List[dict]:
    """
    Return a list like:
    [{'char': 'e', 'num': 44538}, ...] sorted by 'num' desc.
    Only alphabetic characters are included (spaces/punct removed).
    """
    items = [{"char": ch, "num": n}
             for ch, n in char_counts.items()
             if ch.isalpha()]                 # keep letters (incl. accents)
    items.sort(key=lambda x: x["num"], reverse=True)
    return items