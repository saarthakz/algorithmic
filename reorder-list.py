"""
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

In the general case, label the nodes by their original zero-based positions from 0 to n - 1. After reordering, those original positions appear in this order:

[0, n-1, 1, n-2, 2, n-3, ...]

These numbers represent node positions, not the values stored in the nodes.

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        first = []
        second = []

        # Copy the head reference
        head_ref_cp = head

        # Get the length
        length = 0
        while head_ref_cp is not None:
            length += 1
            head_ref_cp = head_ref_cp.next

        # Reset the reference
        head_ref_cp = head

        for idx in range(length - (length // 2)):
            first.append(head_ref_cp)
            head_ref_cp = head_ref_cp.next

        while head_ref_cp is not None:
            second.append(head_ref_cp)
            head_ref_cp = head_ref_cp.next

        second = second[::-1]  # Reversing the order

        # Length of first is length - length // 2
        # Length of second is length // 2

        combined = []

        for idx in range(length // 2):
            combined.append(first[idx])
            combined.append(second[idx])

        if length % 2 != 0:
            combined.append(first[-1])

        for idx in range(len(combined) - 1):
            node = combined[idx]
            next_node = combined[idx + 1]
            node.next = next_node

        combined[-1].next = None
        new_head = combined[0]
        head = new_head
