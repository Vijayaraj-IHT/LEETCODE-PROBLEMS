# Minimum Bit Flips to Convert Number (LeetCode #1318)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Return the minimum number of bit flips (0→1 or 1→0 in the binary representation) needed to convert `start` into `goal`.

## Approach

- `start ^ goal` has a `1` in **exactly** the positions where the two numbers differ — and each such position needs one flip, no more, no fewer.
- Count the set bits with the Brian Kernighan idiom: `x &= x - 1` clears the lowest set bit, so the loop runs once per differing bit.

## Complexity

- **Time:** O(number of differing bits) — at most 32 for 32-bit integers.
- **Space:** O(1).
