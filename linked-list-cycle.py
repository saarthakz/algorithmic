"""
Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visitedSet = set()

        curr = head

        # Traverse the linked list tracking visited node references in a hash set
        while curr is not None:
            # If current node address has been visited before, a cycle exists
            if curr in visitedSet:
                return True

            visitedSet.add(curr)
            curr = curr.next

        # Reached end of list (null), no cycle present
        return False
