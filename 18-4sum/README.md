# 4Sum (LeetCode #18)

**Difficulty:** Medium  
**Code:** `solution.py`

## Problem

Find all unique quadruplets in the array that sum to `target`.

## Approach

- Generalizes the 3Sum pattern: sort once, then **two nested loops** fix indices `i` and `j` (each skipping repeated values so no duplicate quadruplet is produced), and a **two-pointer** search finds the remaining two elements.
- Two-pointer logic as in 3Sum: sum too small → move `left` right; too large → move `right` left; on a hit, skip duplicates on both pointers before advancing.

## Complexity

- **Time:** O(n³) — n² fixed pairs × O(n) two-pointer pass.
- **Space:** O(1) extra (ignoring output and sort).
