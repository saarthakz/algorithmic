"""
Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""

from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        self.get_height_and_balance(root)
        return self.is_balanced

    def get_height_and_balance(self, node: Optional[TreeNode]) -> Tuple[int, int]:
        """
        Returns (height, balance_factor) for the given node.
        Height of a leaf is 0 (or 1 depending on convention).
        """
        if not node:
            return -1, 0  # height = -1 for empty node, balance factor = 0

        left_height, _ = self.get_height_and_balance(node.left)
        right_height, _ = self.get_height_and_balance(node.right)

        # Height is max depth of children + 1
        current_height = 1 + max(left_height, right_height)

        balance_factor = right_height - left_height
        if abs(balance_factor) > 1:
            self.is_balanced = False

        return current_height, balance_factor
