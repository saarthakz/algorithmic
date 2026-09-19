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
        if first is None and second is None:
            return True

        if (first and not second) or (second and not first):
            return False

        assert first is not None
        assert second is not None

        if first.val != second.val:
            return False

        return self.isSameTree(first.left, second.left) and self.isSameTree(
            first.right, second.right
        )
