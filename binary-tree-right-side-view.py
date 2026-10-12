"""
You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.
"""

from typing import Optional, List, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue: List[Tuple[Optional[TreeNode], int]] = [(root, 0)]
        level_mark_set = set()
        ans = []

        while len(queue):
            node, node_level = queue.pop(0)
            if not node:
                continue

            queue.append((node.right, node_level + 1))
            queue.append((node.left, node_level + 1))

            if node_level in level_mark_set:
                continue

            ans.append(node.val)
            level_mark_set.add(node_level)

        return ans
