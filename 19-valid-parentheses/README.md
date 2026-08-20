# Valid Parentheses (LeetCode #20)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Check whether a string consisting of `(`, `)`, `{`, `}`, `[`, `]` is well-formed (correctly nested and balanced).

## Approach

- Stack of opening brackets: push every opener when seen.
- For a closer, pop the top and verify it is the matching opener via the `mapping` table. An empty stack yields the sentinel `'#'`, which can never match — an extra closer is instantly invalid.
- After the scan, the string is valid only if the stack is empty (no unclosed openers).

## Complexity

- **Time:** O(n) — each character pushed and popped once.
- **Space:** O(n) worst case (all openers).
