"""
You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.
"""

# AVL Tree Solution
# O(n * ln(n))

"""
from typing import List
from typing import List, Optional


class Node:
    def __init__(self, key: int):
        self.key = key
        self.count = 1
        self.height = 1
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class AVLTree:
    def height(self, node: Optional[Node]) -> int:
        return node.height if node else 0

    def update_height(self, node: Node) -> None:
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node: Node) -> int:
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y: Node) -> Node:
        x = y.left
        subtree = x.right

        x.right = y
        y.left = subtree

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x: Node) -> Node:
        y = x.right
        subtree = y.left

        y.left = x
        x.right = subtree

        self.update_height(x)
        self.update_height(y)

        return y

    def rebalance(self, node: Node) -> Node:
        self.update_height(node)
        balance = self.balance_factor(node)

        # Left-heavy
        if balance > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right-heavy
        if balance < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert(self, root: Optional[Node], key: int) -> Node:
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            root.count += 1
            return root

        return self.rebalance(root)

    def min_node(self, node: Node) -> Node:
        while node.left:
            node = node.left
        return node

    def _delete_all(self, root: Optional[Node], key: int) -> Optional[Node]:
        "Remove an entire node, including all its occurrences."
        if root is None:
            return None

        if key < root.key:
            root.left = self._delete_all(root.left, key)
        elif key > root.key:
            root.right = self._delete_all(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            successor = self.min_node(root.right)
            root.key = successor.key
            root.count = successor.count
            root.right = self._delete_all(root.right, successor.key)

        return self.rebalance(root)

    def delete(self, root: Optional[Node], key: int) -> Optional[Node]:
        if root is None:
            return None

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Multiple copies: remove just one occurrence.
            if root.count > 1:
                root.count -= 1
                return root

            # Zero or one child.
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            # Two children: replace with the inorder successor.
            successor = self.min_node(root.right)
            root.key = successor.key
            root.count = successor.count

            # Remove the successor node entirely to avoid
            # duplicate keys in separate nodes.
            root.right = self._delete_all(root.right, successor.key)

        return self.rebalance(root)

    def maximum(self, root: Node) -> int:
        while root.right:
            root = root.right
        return root.key

        
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0 or k > len(nums):
            return []

        tree = AVLTree()
        root: Optional[Node] = None
        ans = []

        # Build the first window.
        for num in nums[:k]:
            root = tree.insert(root, num)

        ans.append(tree.maximum(root))

        # Slide the window one position at a time.
        for i in range(k, len(nums)):
            outgoing = nums[i - k]
            incoming = nums[i]

            root = tree.delete(root, outgoing)
            root = tree.insert(root, incoming)

            ans.append(tree.maximum(root))

        return ans
"""

# Heap Solution
# O(n * ln(n))

"""
from typing import List
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0 or k > len(nums):
            return []

        # Store (-value, index) to simulate a max-heap
        heap = [(-nums[idx], idx) for idx in range(k)]
        heapq.heapify(heap)

        ans = [-heap[0][0]]

        for idx in range(k, len(nums)):
            # Add the incoming element
            heapq.heappush(heap, (-nums[idx], idx))

            # Remove expired elements from the top
            while heap and heap[0][1] <= idx - k:
                heapq.heappop(heap)

            # The heap root is the maximum in the current window
            ans.append(-heap[0][0])

        return ans
"""

# Monotonic Deque Solution
# O(n)

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Stores indices
        # Front of the queue maintains higher values
        # Back of the queue maintains the lower values
        dq = deque()

        ans = []

        for idx in range(len(nums)):

            # Remove indices outside the current window (expired indices)
            while dq and dq[0] <= idx - k:
                dq.popleft()

            # Remove candidates smaller than the current element
            while dq and nums[dq[-1]] <= nums[idx]:
                dq.pop()

            # Add the current candidate
            dq.append(idx)

            # Record the maximum once the first window is complete
            if idx >= k - 1:
                ans.append(nums[dq[0]])

        return ans
