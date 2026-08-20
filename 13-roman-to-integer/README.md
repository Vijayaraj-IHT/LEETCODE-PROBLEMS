# Roman to Integer (LeetCode #13)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Convert a Roman numeral string to an integer.

## Approach

- Map every symbol to its value (`I=1, V=5, X=10, L=50, C=100, D=500, M=1000`) and walk left to right.
- If the current symbol is **smaller than the next one**, it belongs to a subtractive pair (IV, IX, XL, XC, CD, CM) → subtract it.
- Otherwise add it to the running total.

## Complexity

- **Time:** O(n) — single pass.
- **Space:** O(1) for the lookup map.

## Notes

Assumes the input is a valid Roman numeral (as guaranteed by the problem).
