
"""
Kosaraju's algorithm to find strongly connected components in a directed graph (Python).
"""

from collections import defaultdict
from typing import List, Dict


class Graph:
    """
    Directed graph supporting Kosaraju's algorithm for SCCs.
    """

    def __init__(self, vertex: int):
        self.V: int = vertex
        self.graph: Dict[int, List[int]] = defaultdict(list)

    def add_edge(self, s: int, d: int) -> None:
        """
        Add an edge from s to d.
        """
        self.graph[s].append(d)

    def dfs(self, d: int, visited_vertex: List[bool]) -> None:
        """
        Depth-first search from vertex d.
        """
        visited_vertex[d] = True
        print(d, end='')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d: int, visited_vertex: List[bool], stack: List[int]) -> None:
        """
        Fill vertices in stack according to their finishing times.
        """
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack.append(d)

    def transpose(self) -> 'Graph':
        """
        Transpose the graph (reverse all edges).
        """
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def print_scc(self) -> None:
        """
        Print all strongly connected components.
        """
        stack: List[int] = []
        visited_vertex: List[bool] = [False] * self.V
        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        gr = self.transpose()
        visited_vertex = [False] * self.V
        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")


if __name__ == "__main__":
    g = Graph(8)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 0)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 4)
    g.add_edge(6, 7)

    print("Strongly Connected Components:")
    g.print_scc()
