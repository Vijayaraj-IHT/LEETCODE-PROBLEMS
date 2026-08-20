# Longest Common Prefix (LeetCode #14)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Find the longest string prefix common to all strings in the list.

## Approach

- Sort the list alphabetically. In sorted order, the strings that differ the most are the **first and last**, so their common prefix is exactly the common prefix of the whole set.
- Walk both strings character by character, accumulating the match; stop at the first mismatch or the end of the shorter string.

## Complexity

- **Time:** O(n · L · log n) for sorting + O(L) for the final comparison.
- **Space:** O(log n) sort overhead (in-place list sort).

## Notes

`strs.sort()` mutates the caller's list in place — pass a copy if the original order matters. (Alternative: vertical scan without sorting, O(total characters).)
