"""
You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

Create a deep copy of the list.

The deep copy should consist of exactly n new nodes, each including:

    The original value val of the copied node
    A next pointer to the new node corresponding to the next pointer of the original node
    A random pointer to the new node corresponding to the random pointer of the original node

Note: None of the pointers in the new list should point to nodes in the original list.

Node values are not guaranteed to be unique.
"""

from typing import Optional, Dict


# Definition for a Node.
class Node:
    def __init__(
        self, x: int, next: "Optional[Node]" = None, random: "Optional[Node]" = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        # Make an node -> index reference map
        node_idx_map: Dict[Node, int] = {}
        idx = 0
        curr = head
        while curr:
            node_idx_map[curr] = idx
            curr = curr.next
            idx += 1

        # Make an index -> random node index reference map now
        idx_random_map: Dict[int, int] = {}
        curr = head
        idx = 0

        while curr:
            # If the random pointer for the current node is not null
            if curr.random:
                idx_curr_random = node_idx_map[curr.random]
                idx_random_map[idx] = idx_curr_random

            curr = curr.next
            idx += 1

        # Make the new list without the random pointers
        new_head = Node(head.val)
        new_curr = new_head

        curr = head
        while curr and new_curr:
            if curr.next:
                new_curr.next = Node(curr.next.val)

            curr = curr.next
            new_curr = new_curr.next

        # Now create an index -> node map for the newly created list
        idx_node_map: Dict[int, Node] = {}
        new_curr = new_head
        idx = 0
        while new_curr:
            idx_node_map[idx] = new_curr
            new_curr = new_curr.next
            idx += 1

        # Finally update the randoms for the newly created list
        new_curr = new_head
        idx = 0
        while new_curr:
            if idx in idx_random_map:
                random_node_idx = idx_random_map[idx]
                new_curr.random = idx_node_map[random_node_idx]
            new_curr = new_curr.next
            idx += 1

        return new_head
