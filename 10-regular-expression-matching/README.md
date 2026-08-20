# Regular Expression Matching (LeetCode #10)

**Difficulty:** Hard  
**Code:** `solution.py`

## Problem

Implement full regex matching where the pattern supports `.` (any single character) and `*` (zero or more occurrences of the preceding element).

## Approach

- Memoized DFS over the pair `(i, j)` — positions in string `s` and pattern `p`. `@cache` makes each state constant time.
- If `p[j+1] == '*'`, the element `p[j]` may appear **zero times** → `dfs(i, j + 2)` skips the pair; or, when `p[j]` matches `s[i]`, it may consume **one more** character of `s` → `dfs(i + 1, j)`.
- Otherwise the characters must match (`.` matches anything) and both pointers advance by one.
- Base case: pattern exhausted → valid only if the string is exhausted too.

## Complexity

- **Time:** O(m · n) states, O(1) work each.
- **Space:** O(m · n) memoization table.
