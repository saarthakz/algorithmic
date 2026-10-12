"""
The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes. Note that the path can not include the same node twice.

Given the root of a binary tree root, return the diameter of the tree.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0
        self.go_deep_and_update_on_return(root)
        return self.max_dia

    def go_deep_and_update_on_return(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        left_depth = self.go_deep_and_update_on_return(node.left)
        right_depth = self.go_deep_and_update_on_return(node.right)
        curr_dia = left_depth + right_depth
        self.max_dia = max(self.max_dia, curr_dia)

        return 1 + max(left_depth, right_depth)
