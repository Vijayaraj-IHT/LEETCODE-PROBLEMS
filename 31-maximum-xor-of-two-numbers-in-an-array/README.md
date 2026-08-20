# Maximum XOR of Two Numbers in an Array (LeetCode #421)

**Difficulty:** Medium  
**Code:** `solution.py`

## Problem

Find the maximum result of `nums[i] XOR nums[j]` over all pairs `i != j`.

## Approach

- Build the answer **bit by bit, most-significant first** (bit 30 down to 0), greedily trying to keep each bit set.
- `mask` accumulates the bits considered so far; `prefixes` is the set of `num & mask` for every number — the "upper part" of each value.
- Candidate = `max_xor | (1 << i)`. The bit is settable iff two prefixes exist whose XOR equals the candidate — check it with `(p ^ potential_max) in prefixes`.
- Keeping only prefixes makes the test O(n) per bit instead of O(n²) pairs.

## Complexity

- **Time:** O(31 · n) — 31 passes over n numbers.
- **Space:** O(n) for the prefix set.
