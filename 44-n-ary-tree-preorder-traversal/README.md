# N-ary Tree Preorder Traversal (LeetCode #589)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Given the `root` of an N-ary tree, return the **preorder traversal** (root → children left-to-right).

## Approach

- Iterative stack: pop node, record `node.val`, then push its children **in reverse** (`children[::-1]`) so the leftmost child is on top and processed next.
- Handles `None` root as `[]`.

## Complexity

- **Time:** O(n) — each node visited once.
- **Space:** O(h) stack depth plus O(n) output.

## Notes

Direct generalization of binary preorder (#144) — the only change is extending all children instead of two. LeetCode's `Node` has `val` and `children`.
