# Number of Students Unable to Eat Lunch (LeetCode #1700)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Students queue with preferences `0` (circular) or `1` (square). Sandwiches are stacked. The front student takes the top sandwich if it matches their preference, otherwise goes to the back. Return the number of students who cannot eat.

## Approach

- Count preferences: `counts = Counter(students)` — only the multiset matters, not the order.
- Iterate sandwiches in stack order: if `counts[sandwich] > 0`, one student of that preference eats (`counts[sandwich]--`); else no remaining student wants this sandwich — the rest of the queue (all `counts[0] + counts[1]`) is stuck and is the answer.
- If the loop finishes, everyone ate → `0`.

## Complexity

- **Time:** O(n) — single pass over sandwiches.
- **Space:** O(1) — only two counters.

## Notes

The simulation of rotating the queue is unnecessary; the Counter shortcut works because students of the same preference are interchangeable. This is the optimal O(n) solution.
