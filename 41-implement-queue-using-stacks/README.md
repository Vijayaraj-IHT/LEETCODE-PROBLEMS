# Implement Queue using Stacks (LeetCode #232)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Implement a FIFO queue using only two stacks. Support `push(x)`, `pop()`, `peek()`, and `empty()`.

## Approach

- Two stacks: `s1` for incoming pushes, `s2` for outgoing pops/peeks.
- `push` → append to `s1` (O(1)).
- `peek`/`pop` → if `s2` is empty, pour all of `s1` into `s2` (reversing order, so the oldest element is on top). Then `s2.pop()` is the queue front.
- Each element moves at most twice (s1 → s2), so amortized O(1).

## Complexity

- **Time:** Amortized O(1) per operation, O(n) worst-case for a single `pop` when `s2` is empty.
- **Space:** O(n).

## Notes

The classic companion to "Implement Stack using Queues" (#225). The `peek()` helper centralizes the transfer logic so `pop()` stays one line.
