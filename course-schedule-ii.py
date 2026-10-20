"""
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.
"""

from typing import List, Dict, Set


class Solution:
    def findOrder(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
    ) -> List[int]:

        # Include every course, even those without prerequisites.
        adj_list: Dict[int, Set[int]] = {course: set() for course in range(numCourses)}

        for prereq in prerequisites:
            first, second = prereq

            if first == second:
                return []

            adj_list[second].add(first)

        # First pass: detect cycles.
        track: Set[int] = set()
        visited: Set[int] = set()

        for node in range(numCourses):
            if self.has_cycle(track, visited, node, adj_list):
                return []

        # Second pass: build topological ordering.
        topo_stack: List[int] = []
        visited = set()

        for node in range(numCourses):
            self.depth_first_topo_search(node, adj_list, visited, topo_stack)

        return list(reversed(topo_stack))

    def has_cycle(
        self,
        track: Set[int],
        visited: Set[int],
        curr: int,
        adj_list: Dict[int, Set[int]],
    ) -> bool:
        if curr in track:
            return True

        if curr in visited:
            return False

        track.add(curr)

        for neighbour in adj_list[curr]:
            if self.has_cycle(track, visited, neighbour, adj_list):
                track.remove(curr)
                return True

        track.remove(curr)
        visited.add(curr)

        return False

    def depth_first_topo_search(
        self,
        node: int,
        adj_list: Dict[int, Set[int]],
        visited: Set[int],
        topo_stack: List[int],
    ) -> None:
        if node in visited:
            return

        visited.add(node)

        for neighbour in adj_list[node]:
            self.depth_first_topo_search(neighbour, adj_list, visited, topo_stack)

        topo_stack.append(node)
