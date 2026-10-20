"""
You are given a network of n directed nodes, labeled from 1 to n. You are also given times, a list of directed edges where times[i] = (ui, vi, ti).

    ui is the source node (an integer from 1 to n)
    vi is the target node (an integer from 1 to n)
    ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).

You are also given an integer k, representing the node that we will send a signal from.

Return the minimum time it takes for all of the n nodes to receive the signal. If it is impossible for all the nodes to receive the signal, return -1 instead.
"""

import heapq

from typing import List

# Dijkstra's Algorithm
# Single Source Shortest Path


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build the adjacency list: u -> [(v, weight), ...]
        adj = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            adj[u].append((v, w))

        # Min-heap stores tuples of (current_dist, node)
        min_heap = [(0, k)]

        # Track the shortest confirmed distance to each node
        shortest_dist = {}

        while min_heap:
            curr_dist, node = heapq.heappop(min_heap)

            # If already visited with a shorter path, skip
            if node in shortest_dist:
                continue

            shortest_dist[node] = curr_dist

            for neighbor, weight in adj[node]:
                if neighbor not in shortest_dist:
                    heapq.heappush(min_heap, (curr_dist + weight, neighbor))

        # If we couldn't reach all n nodes, return -1
        if len(shortest_dist) < n:
            return -1

        # The total time is the maximum of the shortest distances
        return max(shortest_dist.values())
