from collections import defaultdict
from typing import Dict, List


class Solution:

    def findItinerary(self, tickets: List[List[str]], start: str = "JFK") -> List[str]:
        # Edge count map: adj_matrix[u][v] = remaining tickets from u to v
        adj_matrix: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))

        for source, dest in tickets:
            adj_matrix[source][dest] += 1

        return self.pathfinder(start, adj_matrix)

    def pathfinder(
        self,
        node: str,
        adj_matrix: Dict[str, Dict[str, int]],
    ) -> List[str]:
        cyclic_tracks: List[List[str]] = []
        non_cyclic_tracks: List[List[str]] = []

        # Sort neighbor keys upfront for lexicographical preference
        sorted_destinations = sorted(adj_matrix[node].keys())

        for neighbour in sorted_destinations:

            # Consume tickets one by one along this directed edge
            while adj_matrix[node][neighbour] > 0:
                adj_matrix[node][neighbour] -= 1  # Use edge

                neighbour_track = self.pathfinder(neighbour, adj_matrix)

                # Distinguish between cycles that return to `node` vs outgoing trails
                if neighbour_track and neighbour_track[-1] == node:
                    cyclic_tracks.append(neighbour_track)
                else:
                    non_cyclic_tracks.append(neighbour_track)

        def sort_key(elem: List[str]):
            return elem[0] if elem else ""

        cyclic_tracks.sort(key=sort_key)
        non_cyclic_tracks.sort(key=sort_key)

        # Reconstruct the itinerary: [current node] + [all returned cycles] + [final dead-end trail]
        full_track: List[str] = [node]

        for curr_track in cyclic_tracks:
            full_track.extend(curr_track)

        for curr_track in non_cyclic_tracks:
            full_track.extend(curr_track)

        return full_track
