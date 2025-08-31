"""
Longest Common Subsequence (LCS) Algorithm in Python.
Finds the longest common subsequence between two strings.
"""

from typing import List


def lcs_algo(S1: str, S2: str, m: int, n: int) -> None:
    """
    Prints the longest common subsequence between S1 and S2.
    Args:
        S1 (str): First string.
        S2 (str): Second string.
        m (int): Length of S1.
        n (int): Length of S2.
    """
    L: List[List[int]] = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i - 1] == S2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    index = L[m][n]
    lcs: List[str] = [""] * (index + 1)
    lcs[index] = ""
    i, j = m, n
    while i > 0 and j > 0:
        if S1[i - 1] == S2[j - 1]:
            lcs[index - 1] = S1[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    print(f"S1 : {S1}\nS2 : {S2}")
    print(f"LCS: {''.join(lcs)}")


if __name__ == "__main__":
    S1 = "ACADB"
    S2 = "CBDA"
    m = len(S1)
    n = len(S2)
    lcs_algo(S1, S2, m, n)
