from collections import defaultdict


class Solution:
    def characterReplacement(self, st: str, k: int) -> int:
        freqMap = defaultdict(int)
        maxLength = 1
        maxFreq = 1
        left = 0

        def getMaxFreq(freqMap: dict):
            maxFreq = 1
            for key in freqMap.keys():
                maxFreq = max(maxFreq, freqMap[key])
            return maxFreq

        def isWindowValid(left: int, right: int, maxFreq: int, k: int):
            windowSize = right - left + 1
            cond = windowSize - maxFreq <= k
            return cond

        for right in range(len(st)):
            # Expand the window to the right

            # Add the character to the freqMap
            currChar = st[right]
            freqMap[currChar] += 1

            # Get the current max freq
            maxFreq = getMaxFreq(freqMap)

            # If the window is valid
            if isWindowValid(left, right, maxFreq, k):
                # Update the maxLength
                maxLength = max(maxLength, right - left + 1)
            else:
                # Since the window is no longer valid, we shorten the window from the left
                while not isWindowValid(left, right, maxFreq, k):
                    leftChar = st[left]

                    # Reduce the freq of the leftChar since it is being removed from the window
                    freqMap[leftChar] -= 1

                    # Update the maxFreq
                    maxFreq = getMaxFreq(freqMap)

                    left += 1

        return maxLength
