"""
Implement an algorithm to serialize and deserialize a binary tree.

Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or sent across a network to be reconstructed later in another computer environment.

You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. There is no additional restriction on how your serialization/deserialization algorithm should work.
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.str_arr: List[str] = []
        self.serialize_helper(root)
        return ",".join(self.str_arr)

    def serialize_helper(self, node: Optional[TreeNode]):
        if node is None:
            self.str_arr.append("N")
            return

        self.str_arr.append(str(node.val))
        self.serialize_helper(node.left)
        self.serialize_helper(node.right)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.vals = data.split(",")
        self.idx = 0
        return self.deserialize_helper()

    def deserialize_helper(self):
        if self.idx >= len(self.vals):
            return None

        if self.vals[self.idx] == "N":
            self.idx += 1
            return None

        node = TreeNode(int(self.vals[self.idx]))
        self.idx += 1
        node.left = self.deserialize_helper()
        node.right = self.deserialize_helper()
        return node
