# Merge Sorted Array (LeetCode #88)

**Difficulty:** Easy  
**Code:** `solution.c`

## Problem

Merge sorted `nums2` (length `n`) into sorted `nums1` (length `m + n`, padded with zeros at the tail) so that `nums1` becomes one sorted array — in place (C).

## Approach

- `nums1`'s tail is free padding space, so merge **backwards from the end**: `p` points at the last free slot, `p1`/`p2` at the current tails of the real data in `nums1` and `nums2`.
- Write the **larger** of the two tails into `nums1[p]` and advance the corresponding pointer — the largest remaining elements always belong at the end.
- When `nums2` is exhausted, stop: any leftover `nums1` elements are already in their final positions. Only `nums2` leftovers need the second copy loop.

## Complexity

- **Time:** O(m + n).
- **Space:** O(1) — no auxiliary buffer.

## Notes

Merging from the back is the key trick: merging from the front would overwrite `nums1` elements that haven't been placed yet.
