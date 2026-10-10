"""
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.
"""

from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], hours: int) -> int:
        max_pile = piles[0]

        for pile in piles:
            max_pile = max(pile, max_pile)

        speed = max_pile
        start = 1
        end = max_pile

        while start <= end:
            curr_speed = (start + end) // 2

            # Valid speed, we can target a lower one
            if self.is_valid_speed(piles, hours, curr_speed):
                speed = curr_speed  # Update the global acceptable speed
                end = speed - 1
            # Invalid speed, we need to target a higher one
            else:
                start = curr_speed + 1
        return speed

    def is_valid_speed(self, piles: List[int], hours: int, speed: int):
        total = 0
        for pile in piles:
            req_hours = math.ceil(pile / speed)
            total += req_hours

        return total <= hours
