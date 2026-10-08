# N-ary Tree Postorder Traversal (LeetCode #590)

**Difficulty:** Easy  
**Code:** `solution.py`

## Problem

Given the `root` of an N-ary tree, return the **postorder traversal** (children left-to-right → root).

## Approach

- Modified preorder trick: stack traversal that visits root before children, then reverse.
- Pop node, append `val`, extend stack with `node.children` **in order** (left-to-right). Because the stack is LIFO, the rightmost child is processed first in the forward pass, so reversing at the end restores left-to-right postorder.

## Complexity

- **Time:** O(n).
- **Space:** O(h) stack plus O(n) output.

## Notes

Mirrors binary postorder (#145) — push children in natural order and reverse. The `[::-1]` at the end is the whole insight.
