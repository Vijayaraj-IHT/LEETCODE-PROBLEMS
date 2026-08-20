# One Bit Character (LeetCode #717)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

A special binary encoding uses the 1-bit character `[0]` and the 2-bit character `[1,0]`. Given a well-formed array guaranteed to end with a 1-bit character, decide whether that final character is `[0]`.

## Approach

- Decode from the **front**: `bits[i] == 1` starts a 2-bit character → jump 2; `bits[i] == 0` is a 1-bit character → jump 1.
- The loop condition `i < n - 1` stops before the last character.
- The final character is `[0]` exactly when the pointer lands precisely on index `n - 1`; landing past it means the last bit was swallowed as the second bit of a `[1,0]` pair.

## Complexity

- **Time:** O(n) — single left-to-right scan.
- **Space:** O(1).
