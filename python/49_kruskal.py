"""
Kruskal's Algorithm in Python.
Finds the Minimum Spanning Tree (MST) of a weighted undirected graph.
"""

from typing import List


class Graph:
    """
    Undirected weighted graph supporting Kruskal's MST algorithm.
    """

    def __init__(self, vertices: int) -> None:
        self.V: int = vertices
        self.graph: List[List[int]] = []

    def add_edge(self, u: int, v: int, w: int) -> None:
        """
        Add an edge to the graph.
        Args:
            u (int): First vertex.
            v (int): Second vertex.
            w (int): Edge weight.
        """
        self.graph.append([u, v, w])

    def find(self, parent: List[int], i: int) -> int:
        """
        Find set of an element i (with path compression).
        Args:
            parent (List[int]): Parent array.
            i (int): Vertex index.
        Returns:
            int: Root of set containing i.
        """
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(
        self, parent: List[int], rank: List[int], x: int, y: int
    ) -> None:
        """
        Union two sets by rank.
        Args:
            parent (List[int]): Parent array.
            rank (List[int]): Rank array.
            x (int): First set root.
            y (int): Second set root.
        """
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_algo(self) -> None:
        """
        Applies Kruskal's algorithm and prints the MST edges.
        """
        result: List[List[int]] = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent: List[int] = [node for node in range(self.V)]
        rank: List[int] = [0] * self.V
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print(f"{u} - {v}: {weight}")


if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 0, 4)
    g.add_edge(2, 0, 4)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 3)
    g.add_edge(2, 5, 2)
    g.add_edge(2, 4, 4)
    g.add_edge(3, 2, 3)
    g.add_edge(3, 4, 3)
    g.add_edge(4, 2, 4)
    g.add_edge(4, 3, 3)
    g.add_edge(5, 2, 2)
    g.add_edge(5, 4, 3)
    g.kruskal_algo()
