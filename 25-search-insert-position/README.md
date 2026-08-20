# Search Insert Position (LeetCode #35)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Given a sorted array (distinct values) and a target, return the target's index — or the index where it **would be inserted** to keep the array sorted.

## Approach

- Standard binary search over `[low, high]`: return `mid` immediately on a hit.
- On a miss, the search invariants guarantee that `low` lands exactly on the first position where `nums[low] > target` — which is precisely the insertion index.
- Returning `low` after the loop handles both "just before the end" and "at the end" insertions with one value.

## Complexity

- **Time:** O(log n).
- **Space:** O(1).
