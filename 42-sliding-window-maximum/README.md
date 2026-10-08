# Sliding Window Maximum (LeetCode #239)

**Difficulty:** Hard  
**Code:** `solution.py`

## Problem

Given an array `nums` and window size `k`, return the maximum of each sliding window of size `k`.

## Approach

- Monotonic decreasing deque `q` stores **indices**, not values — front is always the current window's maximum.
- For each `i`: discard `q[0]` if it fell out of the window (`q[0] == i - k`); pop from the back while `nums[q[-1]] < nums[i]` (they can never be a future max).
- Append `i`; once `i >= k - 1` the window is full — record `nums[q[0]]`.

## Complexity

- **Time:** O(n) — each index enters and leaves the deque once.
- **Space:** O(k) for the deque.

## Notes

The deque invariant is the key: it stays sorted descending by value, so the max is always at the front. Same pattern as "Shortest Subarray with Sum at Least K" (#862) in this repo.
