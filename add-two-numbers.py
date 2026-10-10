"""
You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:

        first = 0
        idx = 0

        while l1:
            first += l1.val * (10**idx)
            l1 = l1.next
            idx += 1

        second = 0
        idx = 0
        while l2:
            second += l2.val * (10**idx)
            l2 = l2.next
            idx += 1

        ans = first + second
        idx = 0
        ans_digits = []

        if ans == 0:
            return ListNode(0)

        while ans:
            ans_digits.append(ans % 10)
            ans = ans // 10

        head = ListNode(ans_digits[0])
        curr = head

        for idx in range(1, len(ans_digits)):
            curr.next = ListNode(ans_digits[idx])
            curr = curr.next

        return head
