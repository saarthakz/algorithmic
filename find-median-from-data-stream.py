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
