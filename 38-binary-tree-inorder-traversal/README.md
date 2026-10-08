# Binary Tree Inorder Traversal (LeetCode #94)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Given the `root` of a binary tree, return the **inorder traversal** of its nodes' values (left → root → right).

## Approach

- Iterative stack simulation of recursion with a `curr` pointer.
- Go as left as possible, pushing nodes onto `stack`.
- Pop the top, record its value, then move to its right subtree.
- Repeat until both `curr` is null and the stack is empty.

## Complexity

- **Time:** O(n) — each node pushed and popped once.
- **Space:** O(h) — stack holds at most the tree height (O(n) worst case, O(log n) for balanced).

## Notes

LeetCode provides `TreeNode`; the iterative pattern avoids recursion depth limits and mirrors the preorder/postorder stack solutions in this repo.
