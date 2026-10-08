# Longest Valid Parentheses (LeetCode #32)

**Difficulty:** Hard  
**Code:** `solution.py`

## Problem

Given a string `s` containing only `'('` and `')'`, return the length of the longest well-formed (valid) parentheses substring.

## Approach

- Stack holds **indices**; initialize with `-1` as base for the first valid segment.
- Scan `s`: `'('` → push its index; `')'` → pop. If stack becomes empty, push current index as new base (last invalid position). Otherwise `i - stack[-1]` is the length of the current valid substring — update `max_len`.

## Complexity

- **Time:** O(n) — single pass.
- **Space:** O(n) for the stack.

## Notes

Stack-of-indices is the classic linear solution — no DP needed. Recent AC on the profile (submission `2121420662`) suggests this problem was among the solved 58.
