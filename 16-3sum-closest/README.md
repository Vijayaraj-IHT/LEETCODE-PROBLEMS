# 3Sum Closest (LeetCode #16)

**Difficulty:** Medium  
**Code:** `solution.py`

## Problem

Return the sum of three numbers in the array that is closest to the given `target`.

## Approach

- Sort; fix index `i` and run a two-pointer scan over the rest.
- If `current_sum` is **below** the target, advance `left` to increase the sum; otherwise advance `right` to decrease it — the pointers always move the sum closer to the target.
- Track the smallest `|sum - target|` seen so far in `diff`; if an exact match is found, return it immediately (it can't be improved).

## Complexity

- **Time:** O(n²).
- **Space:** O(1) extra (plus sort overhead).

## Notes

Assumes at least 3 elements — the initial best `diff` uses the three smallest values after sorting.
