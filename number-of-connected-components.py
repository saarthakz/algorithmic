"""
You have an undirected graph of n nodes labeled from 0 to n - 1. You are given an integer n and an array edges where edges[i] = [aᵢ, bᵢ] indicates that there is an edge between aᵢ and bᵢ in the graph.

Return the number of connected components in the graph.
"""

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {}

        for edge in edges:
            assert len(edge) == 2, "Edge has more than 2 nodes"
            first, second = edge

            if first in adj_list:
                adj_list[first].add(second)
            else:
                adj_list[first] = set([second])

            if second in adj_list:
                adj_list[second].add(first)
            else:
                adj_list[second] = set([first])

        visited = set()
        ctr = 0

        node_in_edge_cnt = len(adj_list.keys())
        lone_nodes = n - node_in_edge_cnt

        for node in adj_list.keys():
            if node not in visited:
                ctr += 1
            self.depth_first_search(node, visited, adj_list)

        return ctr + lone_nodes

    def depth_first_search(
        self, curr_node: int, visited: set, adj_list: dict[int, set[int]]
    ):
        if curr_node in visited:
            return

        visited.add(curr_node)
        for neighbour in adj_list[curr_node]:
            self.depth_first_search(neighbour, visited, adj_list)
