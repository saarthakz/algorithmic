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
