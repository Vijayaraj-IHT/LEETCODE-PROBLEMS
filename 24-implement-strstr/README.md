# Implement strStr() (LeetCode #28)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Return the index of the first occurrence of `needle` in `haystack`, or `-1` if it is not present.

## Approach

- Brute-force sliding window: for every valid start position `i` in `0 .. n - m`, compare the slice `haystack[i : i + m]` with `needle`.
- Return the first `i` where the slices match; `-1` if the loop finishes without a hit.
- The loop bound `n - m + 1` is exactly the set of positions where a length-m window still fits.

## Complexity

- **Time:** O(n · m) — up to n − m + 1 comparisons, each O(m).
- **Space:** O(1) (slices are compared in place for this pattern).

## Notes

An empty needle returns `0` (the empty string matches at position 0). For very long inputs, KMP or Rabin-Karp do better.
