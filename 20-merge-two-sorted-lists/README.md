# Merge Two Sorted Lists (LeetCode #21)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Merge two sorted linked lists into a single sorted linked list.

## Approach

- A `dummy` head plus a `tail` pointer build the result without special-casing the first node.
- While both lists have nodes, attach the **smaller** head to `tail.next` and advance that list and `tail`.
- When one list is exhausted, link the remaining nodes of the other list directly (they're already sorted).
- Return `dummy.next` — the real head.

## Complexity

- **Time:** O(m + n).
- **Space:** O(1) — existing nodes are relinked, nothing is allocated except the dummy.

## Notes

A local `ListNode` class and `typing` imports were added so the file runs standalone (LeetCode provides `ListNode` and the imports).
