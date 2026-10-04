"""
Design a stack class that supports the push, pop, top, and getMin operations.

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

Each function should run in O(1) time.
"""


class MinStack:

    def __init__(self):
        self.stack = []
        # min_stack tracks the minimum element encountered up to each height
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Determine running minimum and push to min_stack to keep sizes synchronized
        curr_min = self.min_stack[-1] if len(self.min_stack) else val
        curr_min = min(curr_min, val)
        self.min_stack.append(curr_min)

    def pop(self) -> None:
        # Pop from both stacks to maintain 1-to-1 minimum mapping
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # Top of min_stack always holds the current minimum in O(1) time
        return self.min_stack[-1]
