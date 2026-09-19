"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

    The left subtree of every node contains only nodes with keys less than the node's key.
    The right subtree of every node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees are also binary search trees.

"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inOrder(self, node: Optional[TreeNode], arr: list[int]):
        if not node:
            return

        self.inOrder(node.left, arr)
        arr.append(node.val)
        self.inOrder(node.right, arr)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        arr = []
        self.inOrder(root, arr)
        return arr[k - 1]
