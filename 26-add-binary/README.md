# Add Binary (LeetCode #67)

**Difficulty:** Easy  
**Code:** `solution.c`

## Problem

Given two binary strings `a` and `b`, return their sum as a binary string (C).

## Approach

- Schoolbook addition from the **last character** of both strings with a `carry`.
- Allocate `maxLen + 2` chars (one extra slot for a possible final carry) and fill the buffer **backwards**: digit = `sum % 2`, `carry = sum / 2`.
- If the loop never used the first slot (`k == 0` at the end), `memmove` shifts the string left by one to drop the unused leading gap.
- The buffer is always NUL-terminated, so it is a valid C string either way.

## Complexity

- **Time:** O(max(lenA, lenB)).
- **Space:** O(max(lenA, lenB)) for the returned buffer.

## Notes

Includes were added so the file compiles standalone. The caller must `free()` the returned string.
