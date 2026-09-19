"""
Given the head of a linked list and an integer n, remove the nth node from the end of the list and return its head.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listLen = 0

        curr = head
        while curr is not None:
            listLen += 1
            curr = curr.next

        if listLen == 1:
            return None

        removalIdx = listLen - n

        if removalIdx == 0:
            newHead = head.next
            head.next = None
            return newHead

        curr = head
        idx = 0
        while idx < removalIdx - 1:
            idx += 1
            curr = curr.next

        # At the node, just before the removal one
        removalNode = curr.next
        removalNodeNext = removalNode.next
        curr.next = removalNodeNext
        removalNode.next = None

        return head
