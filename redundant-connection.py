"""
You are given a connected undirected graph with n nodes labeled from 1 to n. Initially, it contained no cycles and consisted of n-1 edges.

We have now added one additional edge to the graph. The edge has two different vertices chosen from 1 to n, and was not an edge that previously existed in the graph.

The graph is represented as an array edges of length n where edges[i] = [ai, bi] represents an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the graph is still a connected non-cyclical graph. If there are multiple answers, return the edge that appears last in the input edges.
"""

import heapq

# Prim's Algorithm (A twist on it)
# Minimum Cost Spanning Tree


class Solution:

    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)

        # Build adjacency list: node -> list of (weight/index, neighbor)
        adj = {i: [] for i in range(1, n + 1)}
        for idx, (u, v) in enumerate(edges):
            adj[u].append((idx, v))
            adj[v].append((idx, u))

        visited = set()
        mst_edge_indices = set()
        min_heap = []

        # Start Prim's from node 1
        visited.add(1)
        for weight, neighbor in adj[1]:
            heapq.heappush(min_heap, (weight, 1, neighbor))

        while min_heap and len(mst_edge_indices) < n - 1:
            weight, u, v = heapq.heappop(min_heap)

            if v in visited:
                continue

            visited.add(v)
            mst_edge_indices.add(weight)

            for next_weight, neighbor in adj[v]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (next_weight, v, neighbor))

        # The single edge index NOT in mst_edge_indices is the redundant edge
        for idx in range(n):
            if idx not in mst_edge_indices:
                return edges[idx]

        return []
