from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        adj_list = self._adj_list_from_graph(start_node=node)
        graph_node_ref = self._graph_from_adj_list(adj_list)

        return graph_node_ref[node.val]

    def _adj_list_from_graph(self, start_node: Node):
        adj_list = {}
        queue = [start_node]
        visited = set()

        while len(queue):
            curr = queue.pop(0)
            adj_list[curr.val] = [neighbour.val for neighbour in curr.neighbors]
            visited.add(curr)

            for neighbour in curr.neighbors:
                if neighbour not in visited:
                    queue.append(neighbour)

        return adj_list

    def _graph_from_adj_list(self, adj_list: dict[int, list[int]]):
        graph_node_ref: dict[int, Node] = {}

        # Creating all the new nodes
        for val in adj_list.keys():
            graph_node_ref[val] = Node(val=val)

        # Now that all the new nodes are created, we can reference the neighbors using these new nodes

        for val in adj_list.keys():
            curr_node = graph_node_ref[val]
            curr_node_neighbour_vals = adj_list[val]

            for neighbour in curr_node_neighbour_vals:
                curr_node.neighbors.append(graph_node_ref[neighbour])

        return graph_node_ref
