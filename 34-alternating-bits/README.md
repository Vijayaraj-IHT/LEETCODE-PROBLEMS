# Alternating Bits (LeetCode #693)

**Difficulty:** Easy  
**Code:** `solution.c`

## Problem

Check whether the adjacent bits of the integer `n` always alternate (C).

## Approach

- `n ^ (n >> 1)` compares each bit with the next one down: adjacent bits **differ** → XOR bit is 1, same → 0. So for a fully alternating `n`, the result is a run of all 1s (e.g. n=5 (101) → 5 ^ 2 = 111b).
- All-1 numbers (2ᵏ − 1) have the property `x & (x + 1) == 0`, because adding 1 turns them into a pure power of two. That single test decides it.

## Complexity

- **Time:** O(1).
- **Space:** O(1).

## Notes

The `long` type prevents sign-bit surprises when `n` is near the top of the int range.
