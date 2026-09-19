"""
The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.

For example:

    For arr = [1,2,3], the median is 2.
    For arr = [1,2], the median is (1 + 2) / 2 = 1.5

Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far.

"""

import bisect


class MedianFinder:

    def __init__(self):
        self.arr = []

    # Naive approach
    def addNum(self, num: int) -> None:
        self.arr.insert(self.lowerBound(num), num)
        return

    def findMedian(self) -> float:

        length = len(self.arr)

        # Odd elements
        if length % 2:
            return self.arr[len(self.arr) // 2]
        else:
            first = self.arr[length // 2 - 1]
            second = self.arr[length // 2]
            return (first + second) / 2

    # Gives the index of the element which is just greater, or equal to the current number
    # This will be used to get the index where we want to insert the number
    def lowerBound(self, num: int) -> int:
        return bisect.bisect_left(self.arr, num)
