# Reverse Integer (LeetCode #7)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Reverse the digits of a 32-bit signed integer; return `0` if the reversed value overflows the 32-bit range.

## Approach

- Separate the sign, then work on `abs(x)`.
- Repeatedly extract the last digit (`pop = x % 10`) and rebuild the answer digit by digit: `res = res * 10 + pop`, shrinking `x` with `x //= 10`.
- Overflow guard: if `res` already exceeds `(2³¹ − 1) // 10`, one more `res * 10` would overflow 32 bits — return `0` before multiplying.
- Re-apply the sign at the end.

## Complexity

- **Time:** O(log₁₀|x|) — one pass over the digits.
- **Space:** O(1).

## Notes

The guard checks *before* each multiplication, so `res` can never exceed the 32-bit range during the loop.
