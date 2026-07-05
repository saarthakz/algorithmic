# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        root_val = preorder[0]
        root_node = TreeNode(root_val)

        # Find the index in 'inorder'

        root_val_idx = inorder.index(root_val)
        root_node.left = self.buildSubTree(inorder[:root_val_idx], preorder)

        if root_val_idx != len(inorder) - 1:
            root_node.right = self.buildSubTree(inorder[root_val_idx + 1 :], preorder)

        return root_node

    def buildSubTree(self, elems: List[int], preorder: List[int]) -> Optional[TreeNode]:

        # Elems will always be a sliced version of the 'inorder' list
        if len(elems) == 0:
            return None

        if len(elems) == 1:
            return TreeNode(val=elems[0])

        # Find the root amongst the current elems
        elems_map: dict[int, int] = {}

        # Key: val :: Element Val: Index
        for idx, elem in enumerate(elems):
            elems_map[elem] = idx

        new_root = None

        for idx in range(len(preorder)):
            if preorder[idx] in elems_map:
                new_root = preorder[idx]
                break

        assert new_root is not None

        root_idx = elems_map[new_root]

        # Now we have the new root amongst the current elements
        root_elem_node = TreeNode(new_root)
        root_elem_node.left = self.buildSubTree(elems[:root_idx], preorder)

        if root_idx != len(elems) - 1:
            root_elem_node.right = self.buildSubTree(elems[root_idx + 1 :], preorder)

        return root_elem_node
