
"""
Adjacency Matrix representation of a graph in Python.
Supports adding/removing edges and printing the matrix.
"""

from typing import List


class Graph:
    """
    Undirected graph using adjacency matrix.
    """

    def __init__(self, size: int):
        """
        Initialize the adjacency matrix for a graph of given size.
        """
        self.adjMatrix: List[List[int]] = [
            [0 for _ in range(size)] for _ in range(size)]
        self.size: int = size

    def add_edge(self, v1: int, v2: int) -> None:
        """
        Add an undirected edge between v1 and v2.
        """
        if v1 == v2:
            print(f"Same vertex {v1} and {v2}")
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def remove_edge(self, v1: int, v2: int) -> None:
        """
        Remove the edge between v1 and v2.
        """
        if self.adjMatrix[v1][v2] == 0:
            print(f"No edge between {v1} and {v2}")
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self) -> int:
        return self.size

    def print_matrix(self) -> None:
        """
        Print the adjacency matrix.
        """
        for row in self.adjMatrix:
            print(' '.join(f'{val:4}' for val in row))


def main() -> None:
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.print_matrix()


if __name__ == "__main__":
    main()
