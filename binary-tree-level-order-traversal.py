"""
Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.
"""

# Definition for a binary tree node.

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        # Queue stores tuples of (node, level_number) for BFS
        queue = [(root, 1)]
        level_ans = {}

        # Process nodes level-by-level
        while len(queue):
            elem, curr_level = queue.pop(0)
            # Group node values by their tree level
            if curr_level in level_ans:
                level_ans[curr_level].append(elem.val)
            else:
                level_ans[curr_level] = [elem.val]

            # Enqueue child nodes with incremented level
            if elem.left:
                queue.append((elem.left, curr_level + 1))

            if elem.right:
                queue.append((elem.right, curr_level + 1))

        # Assemble list of level lists in ascending order of depth
        for key in level_ans.keys():
            ans.append(level_ans.get(key))

        return ans
