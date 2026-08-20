# Generate Parentheses (LeetCode #22)

**Difficulty:** Medium  
**Code:** `solution.py`

## Problem

Return all combinations of `n` pairs of well-formed parentheses.

## Approach

- BFS over states `(string, open_count, close_count)`, starting from `('', 0, 0)`.
- A state whose string has length `2n` is complete → collect it.
- Two rules keep every prefix valid: append `'('` while `open_count < n`; append `')'` only while `close_count < open_count` (a closing bracket can only follow an unmatched opening one).

## Complexity

- **Time/Space:** O(n · C(n)) states, where C(n) is the nth Catalan number; strings have length 2n.
- Each generated string is valid by construction — no post-filtering.
