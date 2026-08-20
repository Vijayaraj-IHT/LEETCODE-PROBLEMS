# Median of Two Sorted Arrays (LeetCode #4)

**Difficulty:** Hard  
**Code:** `solution.py`

## Problem

Given two sorted arrays, return the **median** of the combined elements — the middle element for odd total length, or the average of the two middle elements for even total length.

## Approach

- Concatenate the two arrays into one list and sort it.
- Index the middle: one middle element when the length is odd; the average of the two middle elements (`l[m-1]` and `l[m]`) when even.

## Complexity

- **Time:** O((m+n) · log(m+n)) for the sort.
- **Space:** O(m+n) for the merged list.

## Notes

Simple and correct, but not optimal — the canonical Hard difficulty is the O(log(min(m, n))) binary-search solution that partitions the smaller array.
