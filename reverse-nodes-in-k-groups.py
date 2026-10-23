"""
You are given the head of a singly linked list head and a positive integer k.

You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.

Return the modified list after reversing the nodes in each group of k.

You are only allowed to modify the nodes' next pointers, not the values of the nodes.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next: Optional["ListNode"] = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> Optional[ListNode]:

        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        previous_grp_last: Optional[ListNode] = None
        prev = None
        curr = head
        for cnt in range(length // k):
            start = curr
            prev = None
            for _ in range(k):
                assert curr is not None
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            # Set the new global head for the Linked List
            if start == head:
                head = prev

            if previous_grp_last:
                previous_grp_last.next = prev

            previous_grp_last = start

        previous_grp_last.next = curr
        return head
