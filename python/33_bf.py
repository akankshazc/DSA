"""
Bellman-Ford Algorithm in Python.
Finds shortest paths from a source vertex to all other vertices in a weighted graph.
"""

from typing import List


class Graph:
    """
    Weighted directed graph supporting Bellman-Ford algorithm.
    """

    def __init__(self, vertices: int):
        self.V: int = vertices
        self.graph: List[List[int]] = []

    def add_edge(self, s: int, d: int, w: int) -> None:
        """
        Add an edge from s to d with weight w.
        """
        self.graph.append([s, d, w])

    def print_solution(self, dist: List[float]) -> None:
        """
        Print the shortest distance from source to each vertex.
        """
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

    def bellman_ford(self, src: int) -> None:
        """
        Run Bellman-Ford algorithm from source vertex src.
        """
        dist: List[float] = [float("Inf")] * self.V
        dist[src] = 0
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return
        self.print_solution(dist)


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 3, 3)
    g.add_edge(2, 1, 6)
    g.add_edge(3, 2, 2)
    g.bellman_ford(0)
