# Longest Palindromic Substring (LeetCode #5)

**Difficulty:** Medium  
**Code:** `solution.py`

## Problem

Return the longest palindromic substring of `s`.

## Approach

- Every palindrome expands around a center; there are `2n - 1` centers (n single-character, n-1 between characters).
- For each index `i`, `expand` is called twice: odd-length center `(i, i)` and even-length center `(i, i+1)`.
- `expand` moves two pointers outward while the characters match and returns the longest palindrome around that center.
- `max(..., key=len)` keeps the longest substring seen so far.

## Complexity

- **Time:** O(n²) — n-1 centers × up to n-length expansion.
- **Space:** O(1) extra, excluding the output copy.
