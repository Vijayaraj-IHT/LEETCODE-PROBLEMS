# Climbing Stairs (LeetCode #70)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

You can climb 1 or 2 stairs at a time. In how many distinct ways can you reach the `n`th stair?

## Approach

- The last step is either from stair n−1 (a 1-step move) or from stair n−2 (a 2-step move), so `ways(n) = ways(n−1) + ways(n−2)` — a Fibonacci-like recurrence with `ways(1)=1`, `ways(2)=2`.
- Iterative bottom-up with **two rolling variables** instead of an array: `current = one_step_back + two_steps_back`, then roll both forward.
- Base case `n <= 2` returns `n` directly.

## Complexity

- **Time:** O(n) — one loop from 3 to n.
- **Space:** O(1).
