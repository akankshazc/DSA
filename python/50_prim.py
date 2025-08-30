"""
Prim's Algorithm in Python.
Finds the Minimum Spanning Tree (MST) of a weighted undirected graph using Prim's algorithm.
"""

from typing import List

INF = 9999999
V = 5
G: List[List[int]] = [
    [0, 9, 75, 0, 0],
    [9, 0, 95, 19, 42],
    [75, 95, 0, 51, 66],
    [0, 19, 51, 0, 31],
    [0, 42, 66, 31, 0]
]


def prim_mst(graph: List[List[int]], vertices: int) -> None:
    """
    Prints the edges and weights of the MST using Prim's algorithm.
    Args:
        graph (List[List[int]]): Adjacency matrix of the graph.
        vertices (int): Number of vertices in the graph.
    """
    selected = [False] * vertices
    selected[0] = True
    no_edge = 0
    print("Edge : Weight\n")
    while no_edge < vertices - 1:
        minimum = INF
        x = y = 0
        for i in range(vertices):
            if selected[i]:
                for j in range(vertices):
                    if not selected[j] and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j
        print(f"{x}-{y}:{graph[x][y]}")
        selected[y] = True
        no_edge += 1


if __name__ == "__main__":
    prim_mst(G, V)
