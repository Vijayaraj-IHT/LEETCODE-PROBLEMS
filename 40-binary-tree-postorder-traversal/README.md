# Binary Tree Postorder Traversal (LeetCode #145)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Given the `root` of a binary tree, return the **postorder traversal** (left → right → root) of its nodes' values.

## Approach

- Modified preorder: push root, then repeatedly pop, append value, push **left before right**.
- This yields a reverse-postorder (root → right → left); reversing the result gives true postorder (left → right → root).
- Single stack, no visited flag needed.

## Complexity

- **Time:** O(n).
- **Space:** O(h) for the stack plus O(n) for the reversed output.

## Notes

Companion to the preorder solution — same iterative pattern, just reversed. Alternative two-stack or `node.left`/`node.right` order variations are equivalent.
