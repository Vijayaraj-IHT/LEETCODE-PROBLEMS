# Remove Duplicates from Sorted Array (LeetCode #26)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Given a sorted array, remove duplicates **in place** (O(1) extra space) and return the new length.

## Approach

- Classic slow/fast two pointers: `slow` always points at the last unique value.
- The `fast` pointer scans ahead; when it finds a value different from `nums[slow]`, advance `slow` and copy the new value there.
- Unique values end up packed at the front of the array; the new length is `slow + 1`.
- Values beyond `slow` don't matter — the problem only cares about the first k elements.

## Complexity

- **Time:** O(n) — single pass.
- **Space:** O(1).

## Notes

A `from typing import List` import was added so the file runs standalone.
