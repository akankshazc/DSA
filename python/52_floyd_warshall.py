"""
Floyd-Warshall Algorithm in Python.
Finds shortest paths between all pairs of vertices in a weighted graph.
"""

from typing import List

nV = 4
INF = 999


def floyd_warshall(G: List[List[int]]) -> None:
    """
    Runs Floyd-Warshall algorithm and prints shortest distances.
    Args:
        G (List[List[int]]): Adjacency matrix of the graph.
    """
    distance = [row[:] for row in G]
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(
                    distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)


def print_solution(distance: List[List[int]]) -> None:
    """
    Prints the distance matrix.
    Args:
        distance (List[List[int]]): Matrix of shortest distances.
    """
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print()


if __name__ == "__main__":
    G = [
        [0, 3, INF, 5],
        [2, 0, INF, 4],
        [INF, 1, 0, INF],
        [INF, INF, 2, 0]
    ]
    floyd_warshall(G)
