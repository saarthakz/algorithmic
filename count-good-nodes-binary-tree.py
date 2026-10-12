"""
Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x

Given the root of a binary tree root, return the number of good nodes within the tree.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    INT_MIN = -int(1e10)

    def goodNodes(self, root: TreeNode) -> int:
        self.good_cnt = 0
        self.drill_with_max(root, self.INT_MIN)
        return self.good_cnt

    def drill_with_max(self, node: Optional[TreeNode], curr_max: int):
        if node is None:
            return

        if node.val >= curr_max:
            self.good_cnt += 1
            curr_max = node.val

        self.drill_with_max(node.left, curr_max)
        self.drill_with_max(node.right, curr_max)
