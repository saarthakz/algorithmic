"""
Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.
"""

from typing import Optional, Dict, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


# class Solution:
#     INT_MIN = int(-1e10)

#     def maxPathSum(self, root: TreeNode):
#         cache: Dict[Tuple[TreeNode, bool], int] = {}
#         return self.helper(root, False, cache)

#     def helper(
#         self,
#         node: Optional[TreeNode],
#         has_parent: bool,
#         cache: Dict[Tuple[TreeNode, bool], int],
#     ) -> int:
#         if node == None:
#             return self.INT_MIN

#         if (node, has_parent) in cache:
#             return cache[(node, has_parent)]

#         # Case one, has a parent, hence can taken only one child
#         if has_parent:
#             val = node.val
#             left_max_sum = self.helper(node.left, True, cache)
#             right_max_sum = self.helper(node.right, True, cache)
#             max_child_sum = max(left_max_sum, right_max_sum)
#             if max_child_sum > 0:
#                 val += max_child_sum
#             cache[(node, has_parent)] = val
#             return val

#         # Case two, no parent,
#         # Either current node can become a parent
#         # Or we can skip this node altogether

#         # If the current node
#         curr_parent_left_max_sum = self.helper(node.left, True, cache)
#         curr_parent_right_max_sum = self.helper(node.right, True, cache)

#         skip_left_max_sum = self.helper(node.left, False, cache)
#         skip_right_max_sum = self.helper(node.right, False, cache)

#         # In the skip case, result is the max of the children results
#         skip_result = max(skip_left_max_sum, skip_right_max_sum)

#         # In the current node as parent case, we can consider, none, one or both the children as per their value
#         curr_parent_result = node.val
#         if curr_parent_left_max_sum > 0:
#             curr_parent_result += curr_parent_left_max_sum
#         if curr_parent_right_max_sum > 0:
#             curr_parent_result += curr_parent_right_max_sum

#         val = max(curr_parent_result, skip_result)
#         cache[(node, has_parent)] = val
#         return val


class Solution:
    INT_MIN = int(-1e10)

    def maxPathSum(self, root: TreeNode):
        cache: Dict[Tuple[TreeNode, bool], int] = {}
        return self.helper(root, False, cache)

    def helper(
        self,
        node: Optional[TreeNode],
        has_parent: bool,
        cache: Dict[Tuple[TreeNode, bool], int],
    ) -> int:
        if node == None:
            return self.INT_MIN

        if (node, has_parent) in cache:
            return cache[(node, has_parent)]

        val = node.val
        left_max_sum = self.helper(node.left, True, cache)
        right_max_sum = self.helper(node.right, True, cache)

        # Case one, has a parent, hence can taken only one child
        if has_parent:
            max_child_sum = max(left_max_sum, right_max_sum)
            if max_child_sum > 0:
                val += max_child_sum
            cache[(node, has_parent)] = val
            return val

        # No parent cases

        # In the current node as parent case, we can consider, none, one or both the children as per their value
        if left_max_sum > 0:
            val += left_max_sum
        if right_max_sum > 0:
            val += right_max_sum

        # In the skip case, result is the max of the children results
        skip_result = max(
            self.helper(node.left, False, cache),
            self.helper(node.right, False, cache),
        )

        val = max(val, skip_result)
        cache[(node, has_parent)] = val
        return val
