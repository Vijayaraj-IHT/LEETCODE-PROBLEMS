# Add Two Numbers (LeetCode #2)

**Difficulty:** Medium  
**Code:** `solution.py`

## Problem

Two non-negative integers are stored as linked lists in **reverse digit order** (least significant digit at the head). Return their sum as a reversed linked list.

## Approach

- A `dummy` head plus `curr` pointer build the result list; `carry` holds the overflow digit.
- The loop runs while either list still has nodes **or** a carry is pending: `total = val1 + val2 + carry`, new node stores `total % 10`, `carry = total // 10`.
- Advance whichever list still has a node; a missing list contributes 0, so unequal lengths are handled naturally.
- Return `dummy.next` — the real head of the result.

## Complexity

- **Time:** O(max(m, n)).
- **Space:** O(1) extra, excluding the output list (the output itself is O(max(m, n))).

## Notes

`ListNode` is normally provided by the judge; a local definition is included here so the file runs standalone.
