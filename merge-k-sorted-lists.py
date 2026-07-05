# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        return self.helper(lists)

    def helper(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        length = len(lists)

        # Base case
        if length == 1:
            return lists[0]

        l1 = self.helper(lists[0 : length // 2])
        l2 = self.helper(lists[length // 2 : length])

        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, first: Optional[ListNode], second: Optional[ListNode]):

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
