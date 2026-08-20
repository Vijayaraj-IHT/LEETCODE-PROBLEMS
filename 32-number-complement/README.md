# Number Complement (LeetCode #476)

**Difficulty:** Easy  
**Code:** `solution.cpp`

## Problem

Return the bitwise complement of an integer — flip every bit of `num`'s binary representation (C++).

## Approach

- Build a mask of 1s spanning exactly `num`'s bit width: start with `mask = 1` and left-shift until it **exceeds** `num`; then `mask - 1` has 1s in every bit position that `num` has (e.g. num=5 (101) → mask=8 (1000) → mask-1=7 (111)).
- XOR with that mask flips precisely those bits and ignores everything above `num`'s most significant bit.

## Complexity

- **Time:** O(log₂ n) — one shift per bit.
- **Space:** O(1).

## Notes

Using `long` for `mask` avoids overflowing `int` when `num` has its sign-adjacent bit set.
