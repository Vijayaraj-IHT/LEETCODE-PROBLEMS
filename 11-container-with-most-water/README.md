# Container With Most Water (LeetCode #11)

**Difficulty:** Medium  
**Code:** `solution.py`

## Problem

Given `n` vertical lines at x-positions `0..n-1` with heights `height[i]`, find the two lines that together with the x-axis hold the most water.

## Approach

- Two pointers start at both ends; enclosed area = `min(height[left], height[right]) * (right - left)`.
- After recording the area, **always move the shorter line inward**: the height is capped by the shorter side, so keeping the taller side can never increase the area — the width only shrinks.
- This guarantees every potentially better container is still examined.

## Complexity

- **Time:** O(n) — pointers move at most n steps in total.
- **Space:** O(1).

## Notes

A `from typing import List` import was added so the file runs standalone.
