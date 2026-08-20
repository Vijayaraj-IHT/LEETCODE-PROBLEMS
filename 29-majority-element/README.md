# Majority Element (LeetCode #169)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Return the element that appears more than ⌊n/2⌋ times in the array.

## Approach

- Boyer-Moore majority vote: keep a `candidate` and a `count`.
- When `count` hits `0`, re-adopt the current number as the candidate.
- Every element not equal to the candidate cancels one vote (`count -= 1`); equal elements add a vote.
- A true majority (more than half) can never be fully cancelled by everything else, so it survives to the end.

## Complexity

- **Time:** O(n) — single pass.
- **Space:** O(1).

## Notes

Correct because the problem **guarantees** a majority exists. Without that guarantee, a second pass would be needed to verify the candidate's actual frequency.
