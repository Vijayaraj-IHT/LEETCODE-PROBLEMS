# Letter Combinations of a Phone Number (LeetCode #17)

**Difficulty:** Medium  
**Code:** `solution.py`

## Problem

Given a digit string (2–9) on a phone keypad, return all possible letter combinations it could represent.

## Approach

- The digit → letters mapping is built once in `__init__`.
- Iterative expansion (a non-recursive DFS): start from `['']`; for each digit, rebuild the list by extending every existing prefix with each letter of that digit.
- After processing all digits, the list holds exactly all products of one letter per digit.

## Complexity

- **Time:** O(4ᵏ · k) — k digits, up to 4 letters each, strings of length k.
- **Space:** O(4ᵏ) for the combination list.

## Notes

'0' and '1' have no letters, so a digit string containing either empties the combination list and `[]` is returned.
