"""
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
The pair [0, 1], indicates that must take course 1 before taking course 0.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
Return true if it is possible to finish all courses, otherwise return false.
"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Format [first, second] => 'first' requires 'second'
        adj_list: dict[int, set[int]] = {}
        for prereq in prerequisites:
            assert len(prereq) == 2, "More than 2 elements in the prereq"
            first, second = prereq

            if first == second:
                return False

            if second in adj_list:
                adj_list[second].add(first)  # Directed graph for second -> first
            else:
                adj_list[second] = set([first])
            if first not in adj_list:
                adj_list[first] = set()

        track = set()
        visited = set()
        nodes = list(adj_list.keys())
        flag = False

        for node in nodes:
            if node in visited:
                continue

            flag = flag or self.has_cycle(track, visited, node, adj_list)
            if flag:
                return False

        return not flag

    def has_cycle(
        self, track: set, visited: set, curr: int, adj_list: dict[int, set[int]]
    ):
        if curr in visited:
            return False

        if curr in track:
            return True

        track.add(curr)
        flag = False
        for neighbour in adj_list[curr]:
            flag = flag or self.has_cycle(track, visited, neighbour, adj_list)

        track.remove(curr)
        visited.add(curr)

        return flag
