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
