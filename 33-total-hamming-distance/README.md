# Total Hamming Distance (LeetCode #477)

**Difficulty:** Medium  
**Code:** `solution.c`

## Problem

The Hamming distance between two numbers is the count of bit positions where they differ. Sum it over **all pairs** in the array (C).

## Approach

- Work per bit position instead of per pair: at position `i`, let `count_ones` be the numbers with a 1 there and `n - count_ones` the numbers with a 0.
- Every (1, 0) pair differs at that bit, contributing exactly `count_ones * (n - count_ones)` to the total — no double counting, since each unordered pair has exactly one 1-holder and one 0-holder at a differing bit.
- Sum over all 32 bit positions.

## Complexity

- **Time:** O(32 · n) vs O(n² · 32) for the naive pairwise loop.
- **Space:** O(1).
