"""
There is a new alien language that uses the English alphabet, but the order of the letters is unknown.

You are given a list of strings words from the alien language's dictionary. It is claimed that the strings in words are sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of strings in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

    The first letter where they differ is smaller in a than in b.
    a is a prefix of b and a.length < b.length.
"""

from typing import List, Set, Tuple, Dict


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # So it is easier to disqualify the dictionary
        # Will maintain a set of tuples (first, second) where first is lexicographically smaller
        # If at any instant, there is a conflict, the dictionary is not possible
        # Also for any two consecutive words, if the second word is a prefix of the first, then also disqualify

        if len(words) == 1:
            return words[0]

        edge_set: Set[Tuple[str, str]] = set()
        all_possible_nodes: Set[str] = set()

        # Two or more words
        for idx in range(len(words) - 1):
            first = words[idx]
            second = words[idx + 1]

            # Exhaustive set of all possible nodes
            all_possible_nodes.update(first)
            all_possible_nodes.update(second)

            # Duplicate words
            if first == second:
                continue

            # Iterating over the first word's characters
            # Assumption is that

            _idx = 0
            try:
                while _idx < len(first) and (first[_idx] == second[_idx]):
                    _idx += 1
            except IndexError:
                return ""

            # We traversed the entire first word
            if _idx == len(first):
                continue

            # We hit a differentiating character
            edge = (
                second[_idx],
                first[_idx],
            )  # Edge defining from parent -> child, as the second word character is the higher order character

            counter_edge = (first[_idx], second[_idx])

            # We need to ensure that counter_edge does not exist in the set, other the dictionary is not possible
            if counter_edge in edge_set:
                return ""

            # Now that we know the counter_edge is absent, we can add the regular edge
            edge_set.add(edge)

        adj_list: Dict[str, Set[str]] = {}

        for edge in edge_set:
            parent, child = edge

            # Ensuring the parent element exists
            if parent not in adj_list:
                adj_list[parent] = set()

            # Ensuring the child element also exists
            if child not in adj_list:
                adj_list[child] = set()

            # Adding the edge from parent -> child
            adj_list[parent].add(child)

        topological_stack: List[str] = []
        visited: Set[str] = set()

        track: Set[str] = set()

        for node in adj_list.keys():
            flag = self.is_cyclic(
                curr_node=node,
                track=track,
                visited=visited,
                adj_list=adj_list,
            )

            if flag:
                return ""

        visited = set()

        for node in adj_list.keys():
            self.topo_depth_first_search(
                curr_node=node,
                visited=visited,
                topological_stack=topological_stack,
                adj_list=adj_list,
            )

        remainder_nodes = list(all_possible_nodes.difference(topological_stack))
        ans = "".join(topological_stack) + "".join(remainder_nodes)

        return ans

    def is_cyclic(
        self,
        curr_node: str,
        track: Set[str],
        visited: Set[str],
        adj_list: Dict[str, Set[str]],
    ):
        if curr_node in track:
            return True

        flag = False
        track.add(curr_node)
        for neighbour in adj_list[curr_node]:
            flag = flag or self.is_cyclic(
                curr_node=neighbour,
                track=track,
                visited=visited,
                adj_list=adj_list,
            )

        visited.add(curr_node)
        track.remove(curr_node)

        return flag

    def topo_depth_first_search(
        self,
        curr_node: str,
        visited: Set[str],
        topological_stack: List[str],
        adj_list: Dict[str, Set[str]],
    ):
        if curr_node in visited:
            return

        visited.add(curr_node)

        for neighbour in adj_list[curr_node]:
            self.topo_depth_first_search(
                curr_node=neighbour,
                visited=visited,
                topological_stack=topological_stack,
                adj_list=adj_list,
            )

        topological_stack.append(curr_node)
