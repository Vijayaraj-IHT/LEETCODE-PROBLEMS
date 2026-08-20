# Remove Element (LeetCode #27)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Remove all occurrences of `val` from the array **in place** and return the new length.

## Approach

- Single pass with a write pointer `k` at the front of the array.
- Every element that is **not** `val` is copied to position `k`, then `k` advances — compacting the kept elements to the front.
- The copy is always safe because `k <= i` at every step (we never overwrite an unread element).
- `k` ends up equal to the new length.

## Complexity

- **Time:** O(n).
- **Space:** O(1).

## Notes

A `from typing import List` import was added so the file runs standalone.
