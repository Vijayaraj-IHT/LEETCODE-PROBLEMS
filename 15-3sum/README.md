# 3Sum (LeetCode #15)

**Difficulty:** Medium  
**Code:** `solution.py`

## Problem

Find all unique triplets in the array that sum to zero.

## Approach

- Sort the array once — sorting makes duplicate-skipping and the two-pointer search possible.
- Fix index `i` (skip a repeated value of `i`; stop entirely once `nums[i] > 0`, since no zero-sum triplet can exist from there on).
- For the remaining suffix, two pointers hunt for a pair summing to `-nums[i]`: sum too small → move `left` right; too large → move `right` left; equal → record the triplet.
- After each hit, skip duplicate values on **both** pointers so the same triplet is never recorded twice.

## Complexity

- **Time:** O(n²) — n fixed indices × O(n) two-pointer pass.
- **Space:** O(1) extra (ignoring output and the in-place sort's stack).
