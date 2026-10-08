# Number of Recent Calls (LeetCode #933)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Implement `RecentCounter` with `ping(t)` that returns the number of requests in the inclusive interval `[t - 3000, t]`. Calls are in chronological order.

## Approach

- Queue (`deque`) stores timestamps in order.
- Each `ping(t)`: append `t`, then pop from the front while `q[0] < t - 3000` (outside the 3000 ms window).
- Remaining length is the answer.

## Complexity

- **Time:** Amortized O(1) per `ping` — each timestamp is enqueued and dequeued once.
- **Space:** O(w) where w is the number of requests in any 3000 ms window.

## Notes

The sliding window is over time, not array indices — same deque pattern as #239/#862 but with a fixed time delta.
