# Zigzag Conversion (LeetCode #6)

**Difficulty:** Medium  
**Code:** `solution.py`

## Problem

Write string `s` in a zigzag pattern over `numRows` rows, then read it off row by row (left to right, top to bottom) to produce the converted string.

## Approach

- Simulate the path: keep `numRows` row strings and append each character to the current row.
- `step` is `+1` while moving down and `-1` while moving up; the direction flips when the index reaches the top row (`0`) or the bottom row (`numRows - 1`).
- Trivial cases (`numRows == 1` or `numRows >= len(s)`) return `s` unchanged; otherwise join all rows.

## Complexity

- **Time:** O(n).
- **Space:** O(n) for the row strings.
