"""
You are given a 2-D integer array points, where points[i] = [xi, yi]. Each points[i] represents a distinct point on a 2-D plane.

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between the two points, i.e. |xi - xj| + |yi - yj|.

Return the minimum cost to connect all points together, such that there exists exactly one path between each pair of points.
"""

import heapq
from typing import List, Tuple


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        # Step 1: Precompute all edges in memory (Adjacency List)
        # adj[u] will store tuples of (cost, v)
        adj: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
        for idx in range(n):
            x1, y1 = points[idx]
            for j in range(idx + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[idx].append((dist, j))
                adj[j].append((dist, idx))

        # Step 2: Prim's algorithm using a Priority Queue
        visited = [False] * n
        min_heap: List[Tuple[int, int]] = [(0, 0)]  # (cost, node)
        total_cost = 0
        nodes_in_mst = 0

        while min_heap and nodes_in_mst < n:
            cost, u = heapq.heappop(min_heap)

            # Skip if already included in the MST
            if visited[u]:
                continue

            # Add node u to the MST
            visited[u] = True
            total_cost += cost
            nodes_in_mst += 1

            # Traverse precomputed edges from adjacency list
            for weight, v in adj[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (weight, v))

        return total_cost
