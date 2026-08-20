# Integer to Roman (LeetCode #12)

**Difficulty:** Medium  
**Code:** `solution.py`

## Problem

Convert an integer (1 – 3999) to its Roman numeral string.

## Approach

- A greedy table ordered from largest to smallest, **including the six subtractive pairs**: CM (900), CD (400), XC (90), XL (40), IX (9), IV (4) — these handle the 4 and 9 cases directly.
- For each entry, append the symbol as many times as it fits: `count, remaining = divmod(remaining, val)`.
- Because the table is greedy and the Roman system is canonical, the first-fitting symbol is always correct — no backtracking needed.

## Complexity

- **Time:** O(1) — fixed 13-entry table, output is at most 15 characters.
- **Space:** O(1).
