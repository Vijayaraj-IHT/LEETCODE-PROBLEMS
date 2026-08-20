# Palindrome Number (LeetCode #9)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Determine whether an integer is a palindrome (reads the same forwards and backwards) — without converting it to a string.

## Approach

- Quick rejections: negatives (the minus sign) and non-zero numbers ending in `0` can never read the same backwards.
- Reverse only the **second half** of the number: while `x > reversed_half`, move the last digit of `x` onto `reversed_half`. Stopping halfway avoids overflow when the whole number would be reversed.
- Even digit count: `x == reversed_half`. Odd digit count: the middle digit sits in `reversed_half` and is ignored — `x == reversed_half // 10`.

## Complexity

- **Time:** O(log₁₀n) — half of the digits are processed.
- **Space:** O(1).
