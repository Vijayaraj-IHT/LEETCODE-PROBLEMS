# Third Maximum Number (LeetCode #414)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Return the **third distinct** maximum number in the array; if it doesn't exist, return the maximum.

## Approach

- One pass maintaining the top three **distinct** values (`first >= second >= third`), seeded with `float('-inf')` sentinels.
- Skip a number already present among the top three (deduplication), otherwise insert it and shift the rest down:
  - bigger than `first` → all three shift down;
  - bigger than `second` → `second`/`third` shift;
  - bigger than `third` → replace `third`.
- Return `third` if a third distinct value was ever found, otherwise `first` (the maximum).

## Complexity

- **Time:** O(n).
- **Space:** O(1).
