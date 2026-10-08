# Remove Duplicates from Sorted List (LeetCode #83)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Given the head of a sorted linked list, delete all duplicates so each element appears only once. Return the modified list.

## Approach

- Single pass with `curr` pointer: while `curr` and `curr.next` exist, compare values.
- If `curr.val == curr.next.val`, bypass `curr.next` (`curr.next = curr.next.next`) — duplicates are adjacent in a sorted list.
- Otherwise advance `curr`.

## Complexity

- **Time:** O(n) — each node visited once.
- **Space:** O(1) — in-place.

## Notes

Sorted-list variant of "Remove Duplicates from Sorted Array" (#26 / `22-remove-duplicates-from-sorted-array`). No extra memory; the list is edited by re-linking.
