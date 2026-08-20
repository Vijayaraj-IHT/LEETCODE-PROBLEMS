# Bitwise OR of Array Ranges (LeetCode #848)

**Difficulty:** Hard  
**Code:** `solution.c`

## Problem

For every subarray `A[i..j]` (i ≤ j), compute `A[i] | A[i+1] | ... | A[j]`. Return the size of the set of all distinct results (C).

## Approach

- Key insight: for a fixed right endpoint `i`, the distinct OR values of subarrays ending at `i` form a **small, monotone** list — extending a subarray to the left only ever *sets* more bits.
- So per endpoint `i`: start the new list with `{A[i]}`, then OR each distinct value from the *previous* endpoint's list with `A[i]`, appending only when the value differs from the last one appended (duplicates are adjacent because the list is monotone).
- Each per-endpoint list stays ≤ ~32 entries (31 bits, each new start sets at least one new bit), so the total work is linear-ish.
- Finally, `qsort` the collected values and count the distinct ones.

## Complexity

- **Time:** O(n · 32) for the OR sweeps, plus sorting up to ~32n collected values.
- **Space:** O(32n) worst-case buffer (pre-allocated, freed at the end).

## Notes

`<stdlib.h>` was added so the file compiles standalone (`malloc`, `qsort`, `free`).
