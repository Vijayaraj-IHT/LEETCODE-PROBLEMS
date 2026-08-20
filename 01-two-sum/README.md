# Two Sum (LeetCode #1)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers that add up to `target`.

## Approach

- For each index `i`, compute `check = target - nums[i]` — the value that must also be present in the array.
- `check in nums` is a linear membership scan; when found, `nums.index(check)` gives the complement's index and the pair is returned.
- The `i != nums.index(check)` guard prevents using the same element twice when `nums[i]` is itself the complement (e.g. `target = 2 * nums[i]`).

## Complexity

- **Time:** O(n²) — membership check and `index()` each scan the list per iteration.
- **Space:** O(1) extra.

## Notes

This is the brute-force version. The classic O(n) solution is a single pass with a `value -> index` hashmap. Note `list.index` always finds the *first* occurrence of a value, which is less precise than tracking indices explicitly.
