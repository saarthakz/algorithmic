"""
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, first: Optional[TreeNode], second: Optional[TreeNode]) -> bool:
        # Both nodes are None: structurally matching base case
        if first is None and second is None:
            return True

        # One node is None and the other is not: structural mismatch
        if (first and not second) or (second and not first):
            return False

        assert first is not None
        assert second is not None

        # Node values must match
        if first.val != second.val:
            return False

        # Recursively verify both left and right subtrees match
        return self.isSameTree(first.left, second.left) and self.isSameTree(
            first.right, second.right
        )
