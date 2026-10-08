# Shortest Subarray with Sum at Least K (LeetCode #862)

**Difficulty:** Hard  
**Code:** `solution.py`

## Problem

Given an array `nums` (may contain negatives) and integer `k`, find the length of the shortest **contiguous** subarray with sum `>= k`, or `-1` if none exists.

## Approach

- Prefix sums `prefix[i] = sum(nums[0:i])`; the sum of `nums[l:r]` is `prefix[r] - prefix[l]`.
- Monotonic increasing deque `q` stores candidate left indices with increasing `prefix` values.
- For each `i`: while `prefix[i] - prefix[q[0]] >= k`, the window `[q[0], i)` is valid — update `res` and pop left (seek shorter). Then maintain increasing order by popping `q[-1]` while `prefix[i] <= prefix[q[-1]]` (a smaller prefix dominates a larger one for future `i`).
- Append `i`. Answer is `res` or `-1`.

## Complexity

- **Time:** O(n) — each index enters/leaves deque once.
- **Space:** O(n) for prefix and deque.

## Notes

The monotonic queue is the same idea as Sliding Window Maximum (#239) but over prefix minima. Handles negatives, unlike a two-pointer window.
