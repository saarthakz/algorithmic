"""
Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:

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
    def isLeafNode(self, node: TreeNode) -> bool:
        if node.left is None and node.right is None:
            return True
        return False

    def getTreeMax(self, node: TreeNode) -> int:
        curr = node
        while curr.right:
            curr = curr.right
        return curr.val

    def getTreeMin(self, node: TreeNode) -> int:
        curr = node
        while curr.left:
            curr = curr.left
        return curr.val

    def isValidBST(self, node: Optional[TreeNode]) -> bool:
        if node == None:
            return True

        return self.helper(node)

    def helper(self, node: TreeNode) -> bool:

        # A leaf node is always a valid subtree
        if self.isLeafNode(node):
            return True

        is_left_subtree_valid = self.helper(node.left) if node.left else None
        is_right_subtree_valid = self.helper(node.right) if node.right else None

        if is_left_subtree_valid == False:
            return False

        if is_right_subtree_valid == False:
            return False

        if (node.left and self.getTreeMax(node.left) >= node.val) or (
            node.right and self.getTreeMin(node.right) <= node.val
        ):
            return False

        return True
