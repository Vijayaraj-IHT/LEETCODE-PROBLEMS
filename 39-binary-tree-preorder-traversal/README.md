# Binary Tree Preorder Traversal (LeetCode #144)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Given the `root` of a binary tree, return the **preorder traversal** (root → left → right) of its nodes' values.

## Approach

- Iterative stack starting with `root`; pop, record, then push right child before left child so left is processed first (LIFO).
- Each node is visited once; no recursion needed.

## Complexity

- **Time:** O(n) — each node pushed/popped once.
- **Space:** O(h) — stack depth equals tree height.

## Notes

Mirrors the postorder trick in this repo (push left then right, reverse result). LeetCode's `TreeNode` is provided by the judge.
