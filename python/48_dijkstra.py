"""
Dijkstra's Algorithm in Python.
Finds shortest paths in a weighted graph from a source vertex to all other vertices.
"""

import sys
from typing import List, Tuple


class Graph:
    """
    Graph class implementing Dijkstra's shortest path algorithm.
    """

    def __init__(self, vertices: List[List[int]], edges: List[List[int]]) -> None:
        """
        Initialize the graph with adjacency and weight matrices.
        Args:
            vertices (List[List[int]]): Adjacency matrix (0/1).
            edges (List[List[int]]): Weight matrix.
        """
        self.vertices = vertices
        self.edges = edges
        self.num_vertices = len(vertices[0])

    def find_next_vertex(self, distances: List[Tuple[int, int]]) -> int:
        """
        Find the unvisited vertex with minimum distance.
        Args:
            distances (List[Tuple[int, int]]): List of [visited, distance] pairs.
        Returns:
            int: Index of next vertex to visit.
        """
        v = -1
        for index in range(self.num_vertices):
            if distances[index][0] == 0 and (v < 0 or distances[index][1] <= distances[v][1]):
                v = index
        return v

    def dijkstra(self) -> List[int]:
        """
        Run Dijkstra's algorithm from vertex 'a'.
        Returns:
            List[int]: List of shortest distances from source.
        """
        distances = [[0, 0]]
        for _ in range(self.num_vertices - 1):
            distances.append([0, sys.maxsize])

        for _ in range(self.num_vertices):
            current = self.find_next_vertex(distances)
            for neighbor in range(self.num_vertices):
                if (self.vertices[current][neighbor] == 1 and
                        distances[neighbor][0] == 0):
                    new_distance = distances[current][1] + \
                        self.edges[current][neighbor]
                    if distances[neighbor][1] > new_distance:
                        distances[neighbor][1] = new_distance
            distances[current][0] = 1

        return [d[1] for d in distances]


if __name__ == "__main__":
    # Example graph representation
    vertices = [
        [0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 1, 0]
    ]
    edges = [
        [0, 0, 1, 2, 0, 0, 0],
        [0, 0, 2, 0, 0, 3, 0],
        [1, 2, 0, 1, 3, 0, 0],
        [2, 0, 1, 0, 0, 0, 1],
        [0, 0, 3, 0, 0, 2, 0],
        [0, 3, 0, 0, 2, 0, 1],
        [0, 0, 0, 1, 0, 1, 0]
    ]

    graph = Graph(vertices, edges)
    distances = graph.dijkstra()

    for i, distance in enumerate(distances):
        print(
            f"Distance of {chr(ord('a') + i)} from source vertex: {distance}")
