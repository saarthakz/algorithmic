"""
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        # Traverse list and reverse each node's next pointer
        while curr is not None:
            nxt = curr.next  # Save next node before overwriting pointer
            curr.next = prev  # Reverse pointer direction
            prev = curr  # Advance prev to current node
            curr = nxt  # Advance curr to next node

        # prev becomes the new head of the reversed list
        return prev
