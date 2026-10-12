"""
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

    LRUCache(int capacity) Initialize the LRU cache of size capacity.
    int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.

A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in O(1) average time complexity.
"""

from typing import Optional


class Node:
    def __init__(
        self,
        val: int,
        next: "Optional[Node]" = None,
        prev: "Optional[Node]" = None,
    ) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.recency_list_head: Optional[Node] = None
        self.recency_list_tail: Optional[Node] = None
        self.list_length = 0

    # Both get() and put() use this to maintain the doubly linked list.
    def move_to_tail(self, node: Node) -> None:
        if node == self.recency_list_tail:
            return

        # Remove node from its current position
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        # Update head if the node was the head
        if node == self.recency_list_head:
            self.recency_list_head = node.next

        # Append node to the tail
        node.prev = self.recency_list_tail
        node.next = None

        if self.recency_list_tail:
            self.recency_list_tail.next = node

        self.recency_list_tail = node

    def remove_lru(self) -> None:
        if self.recency_list_head is None:
            return

        lru_node = self.recency_list_head
        self.cache.pop(lru_node.val)

        # Update head independently
        self.recency_list_head = lru_node.next

        # After removal, if the head exists, update ref
        if self.recency_list_head:
            self.recency_list_head.prev = None
        else:
            # Else the list is empty and we need to update the tail
            self.recency_list_tail = None

        lru_node.next = None
        lru_node.prev = None
        self.list_length -= 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value, node = self.cache[key]

        self.move_to_tail(node)

        return value

    def put(self, key: int, value: int) -> None:

        # If key already exists, update its value and recency.
        if key in self.cache:
            # Update the value
            self.cache[key][0] = value

            node = self.cache[key][1]

            # FIX 10: Correctly update recency and all linked-list pointers.
            self.move_to_tail(node)
            return

        # If overflow, remove the LRU
        if self.list_length >= self.capacity:
            self.remove_lru()

        # Insert the new key.
        node = Node(key)
        self.cache[key] = [value, node]

        if self.recency_list_tail is None:
            self.recency_list_head = node
        else:
            node.prev = self.recency_list_tail
            self.recency_list_tail.next = node

        self.recency_list_tail = node
        self.list_length += 1
