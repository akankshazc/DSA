"""
Rabin-Karp Algorithm in Python.
Searches for a pattern in a text using hashing.
"""

from typing import Any

d = 10


def search(pattern: str, text: str, q: int) -> None:
    """
    Searches for all occurrences of pattern in text using Rabin-Karp algorithm.
    Args:
        pattern (str): Pattern to search for.
        text (str): Text to search in.
        q (int): A prime number for hashing.
    """
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            else:
                print(f"Pattern is found at position: {i + 1}")
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q


if __name__ == "__main__":
    text = "ABCCDDAEFG"
    pattern = "CDD"
    q = 13
    search(pattern, text, q)
