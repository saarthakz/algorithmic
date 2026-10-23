"""
There are n airports, labeled from 0 to n - 1, which are connected by some flights. You are given an array flights where flights[i] = [from_i, to_i, price_i] represents a one-way flight from airport from_i to airport to_i with cost price_i. You may assume there are no duplicate flights and no flights from an airport to itself.

You are also given three integers src, dst, and k where:

    src is the starting airport
    dst is the destination airport
    src != dst
    k is the maximum number of stops you can make (not including src and dst)

Return the cheapest price from src to dst with at most k stops, or return -1 if it is impossible.
"""

from typing import List, Set, Dict
from collections import defaultdict


class Solution:

    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj_List = defaultdict(list)
        for origin, destination, price in flights:
            adj_List[origin].append((destination, price))

        memo = {}
        active_path = set()

        cheapest = self.helper(src, k, dst, adj_List, memo, active_path)
        return cheapest if cheapest != int(1e10) else -1

    def helper(
        self,
        current_airport: int,
        stops_remaining: int,
        destination: int,
        flight_map: Dict,
        memo: Dict,
        active_path: Set,
    ) -> int:
        if current_airport == destination:
            return 0
        if stops_remaining < 0:
            return int(1e10)

        state = (current_airport, stops_remaining)
        if state in memo:
            return memo[state]

        active_path.add(current_airport)
        cheapest_cost = int(1e10)

        for next_airport, ticket_price in flight_map[current_airport]:
            if next_airport not in active_path:
                cost = ticket_price + self.helper(
                    next_airport,
                    stops_remaining - 1,
                    destination,
                    flight_map,
                    memo,
                    active_path,
                )
                cheapest_cost = min(cheapest_cost, cost)

        active_path.remove(current_airport)

        memo[state] = cheapest_cost
        return cheapest_cost
