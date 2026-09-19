"""
Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q are descendants. The ancestor is allowed to be a descendant of itself.
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:

        root_cp = root
        path_to_p: list[TreeNode] = []
        path_to_q: list[TreeNode] = []

        # Find path to 'p'
        while root is not None:
            path_to_p.append(root)
            if root.val == p.val:
                break

            if p.val < root.val:
                root = root.left
            else:
                root = root.right

        # Reset root ref
        root = root_cp

        # Find path to 'q'
        while root is not None:
            path_to_q.append(root)
            if root.val == q.val:
                break

            if q.val < root.val:
                root = root.left
            else:
                root = root.right

        if len(path_to_p) > len(path_to_q):
            reverse_traversal_list = path_to_p[::-1]
            st = set(path_to_q)
        else:
            reverse_traversal_list = path_to_q[::-1]
            st = set(path_to_p)

        for node in reverse_traversal_list:
            if node in st:
                return node
