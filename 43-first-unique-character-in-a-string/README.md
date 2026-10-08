# First Unique Character in a String (LeetCode #387)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Given a string `s`, return the index of the first non-repeating character, or `-1` if none exists.

## Approach

- One pass with `Counter` to count frequency of each character.
- Second pass in original order: first character with `count == 1` is the answer; if none, return `-1`.

## Complexity

- **Time:** O(n) — two linear scans.
- **Space:** O(1) extra — at most 26 lowercase letters (O(n) worst-case for Unicode).

## Notes

Two-pass is optimal and readable; a single-pass with OrderedDict is possible but not needed for this constraint.
