
"""
Ford-Fulkerson Algorithm in Python.
Finds the maximum flow in a flow network using BFS for path searching.
"""

from typing import List


class Graph:
    """
    Directed graph supporting Ford-Fulkerson maximum flow algorithm.
    """

    def __init__(self, graph: List[List[int]]) -> None:
        self.graph: List[List[int]] = graph
        self.ROW: int = len(graph)

    def searching_algo_BFS(self, s: int, t: int, parent: List[int]) -> bool:
        """
        Uses BFS to find an augmenting path from s to t.
        Args:
            s (int): Source vertex.
            t (int): Sink vertex.
            parent (List[int]): List to store path.
        Returns:
            bool: True if path exists, False otherwise.
        """
        visited = [False] * self.ROW
        queue: List[int] = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return visited[t]

    def ford_fulkerson(self, source: int, sink: int) -> int:
        """
        Computes the maximum flow from source to sink using Ford-Fulkerson algorithm.
        Args:
            source (int): Source vertex.
            sink (int): Sink vertex.
        Returns:
            int: Maximum flow value.
        """
        parent: List[int] = [-1] * self.ROW
        max_flow = 0
        while self.searching_algo_BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return int(max_flow)


if __name__ == "__main__":
    graph = [
        [0, 8, 0, 0, 3, 0],
        [0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 7, 2],
        [0, 0, 0, 0, 0, 5],
        [0, 0, 7, 4, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    g = Graph(graph)
    source = 0
    sink = 5
    print(f"Max Flow: {g.ford_fulkerson(source, sink)}")
