# String to Integer (atoi) (LeetCode #8)

**Difficulty:** Medium  
**Code:** `solution.py`

## Problem

Convert a string to a 32-bit signed integer, mimicking `atoi()`: skip leading whitespace, read an optional sign, read digits until a non-digit, and clamp the result to the 32-bit range.

## Approach

- `s.lstrip()` drops leading whitespace; an empty string gives `0`.
- Consume one optional `+` / `-` to set the sign (the index `i` moves past it).
- Accumulate `res = res * 10 + int(s[i])` while `s[i].isdigit()`; the scan stops at the first non-digit, so trailing junk is ignored.
- Apply the sign, then clamp to `[-2³¹, 2³¹ − 1]`.

## Complexity

- **Time:** O(n) — single scan of the string.
- **Space:** O(1) extra.

## Notes

Clamping happens *after* full accumulation; a stricter implementation clamps incrementally inside the digit loop.
