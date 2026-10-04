"""
You are given the root of a binary tree root. Invert the binary tree and return its root.
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: empty subtree
        if not root:
            return

        # Recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Swap the left and right child references
        root.left, root.right = root.right, root.left
        return root
