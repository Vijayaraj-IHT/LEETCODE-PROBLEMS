# Longest Substring Without Repeating Characters (LeetCode #3)

**Difficulty:** Medium  
**Code:** `solution.py`

## Problem

Find the length of the longest substring of `s` that contains no repeating characters.

## Approach

- Sliding window `[start, end]` plus a hashmap `char_map` of the last-seen index of each character.
- If `s[end]` was last seen at an index **at or after** `start`, the window contains a duplicate — jump `start` to `char_map[s[end]] + 1`.
- Always record the latest index of `s[end]` and update `max_len` with the current window size `end - start + 1`.

## Complexity

- **Time:** O(n) — each character enters and leaves the window at most once.
- **Space:** O(min(n, alphabet size)).
