# Design Circular Queue (LeetCode #622)

**Difficulty:** Medium  
**Code:** `solution.py`

## Problem

Design a circular queue with fixed capacity `k`. Support `enQueue`, `deQueue`, `Front`, `Rear`, `isEmpty`, `isFull` in O(1).

## Approach

- Fixed array `queue` of size `k` plus `head` (front index), `tail` (next insertion index), `size`, and `capacity`.
- `enQueue`: write at `tail`, advance `tail = (tail + 1) % capacity`, `size++`.
- `deQueue`: advance `head = (head + 1) % capacity`, `size--`.
- `Front` is `queue[head]`; `Rear` is `queue[(tail - 1 + capacity) % capacity]` (element before `tail`).
- Modulo arithmetic makes the buffer wrap around without shifting.

## Complexity

- **Time:** O(1) per operation.
- **Space:** O(k) for the backing array.

## Notes

The `size` field disambiguates full vs empty (both would otherwise have `head == tail`). This is the array-based circular buffer pattern.
