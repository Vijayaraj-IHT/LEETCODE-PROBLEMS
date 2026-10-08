# Implement Stack using Queues (LeetCode #225)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Implement a LIFO stack using only a single queue. Support `push(x)`, `pop()`, `top()`, and `empty()`.

## Approach

- Single `deque` `q` holds the stack with the **top at the front** (`q[0]`).
- `push(x)`: append `x` to the back, then rotate the previous `n-1` elements to the back (`q.append(q.popleft())`). This moves the new element to the front, preserving LIFO order with only queue operations.
- `pop` is `popleft()`, `top` is `q[0]`, `empty` checks length.

## Complexity

- **Time:** `push` O(n) (rotation), `pop`/`top`/`empty` O(1).
- **Space:** O(n).

## Notes

Companion to "Implement Queue using Stacks" (#232 / `41-implement-queue-using-stacks`). An alternative two-queue solution exists; this single-queue rotation is more concise and matches the repo's deque style.
