from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list: dict[int, set[int]] = {}

        if not len(edges):
            return True

        for edge in edges:
            assert len(edge) == 2, "Edge has more than 2 elements"
            first, second = edge

            if first in adj_list:
                adj_list[first].add(second)
            else:
                adj_list[first] = set([second])

            if second in adj_list:
                adj_list[second].add(first)
            else:
                adj_list[second] = set([first])

        track = set()
        visited = set()
        nodes = list(adj_list.keys())
        flag = False

        for node in nodes:
            if node in visited:
                continue

            flag = flag or self.has_cycle(track, visited, -1, node, adj_list)
            if flag:
                return False

        # If cycle found through any of the nodes
        if flag:
            return not flag

        # If not, let's check for node continuity
        # flag is False
        cont_st = set()
        continuity = False
        for edge in edges:
            assert len(edge) == 2, "Edge has more than 2 elements"
            first, second = edge
            if first in cont_st or second in cont_st:
                continuity = True
            else:
                continuity = False
            cont_st.add(first)
            cont_st.add(second)
        return continuity

    def has_cycle(
        self,
        track: set,
        visited: set,
        prev: int,
        curr: int,
        adj_list: dict[int, set[int]],
    ):
        if curr in visited:
            return False

        if curr in track:
            return True

        track.add(curr)
        flag = False
        for neighbour in adj_list[curr]:
            if neighbour != prev:
                flag = flag or self.has_cycle(track, visited, curr, neighbour, adj_list)

        track.remove(curr)
        visited.add(curr)

        return flag
