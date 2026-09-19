"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, first: Optional[ListNode], second: Optional[ListNode]
    ) -> Optional[ListNode]:
        combined = []

        if not first:
            return second

        if not second:
            return first

        while first is not None and second is not None:
            if first.val < second.val:
                combined.append(first)
                first = first.next
            else:
                combined.append(second)
                second = second.next

        while first is not None:
            combined.append(first)
            first = first.next

        while second is not None:
            combined.append(second)
            second = second.next

        for idx in range(len(combined) - 1):
            node = combined[idx]
            next_node = combined[idx + 1]
            node.next = next_node

        combined[-1].next = None

        return combined[0]
