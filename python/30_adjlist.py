
"""
Adjacency List representation of a graph in Python.
Supports adding edges and printing the adjacency list.
"""

from typing import Optional, List


class AdjNode:
    """
    Node in the adjacency list.
    """

    def __init__(self, value: int):
        self.vertex: int = value
        self.next: Optional['AdjNode'] = None


class Graph:
    """
    Undirected graph using adjacency list.
    """

    def __init__(self, num: int):
        self.V: int = num
        self.graph: List[Optional[AdjNode]] = [None] * self.V

    def add_edge(self, s: int, d: int) -> None:
        """
        Add an undirected edge between s and d.
        """
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    def print_graph(self) -> None:
        """
        Print the adjacency list of the graph.
        """
        for i in range(self.V):
            print(f"Vertex {i}:", end="")
            temp = self.graph[i]
            while temp:
                print(f" -> {temp.vertex}", end="")
                temp = temp.next
            print()


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.print_graph()
