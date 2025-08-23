
"""
Breadth-First Search (BFS) algorithm in Python.
"""

import collections
from typing import Dict, List, Set


def bfs(graph: Dict[int, List[int]], root: int) -> None:
    """
    Perform BFS traversal from the root node.
    """
    visited: Set[int] = set()
    queue = collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        print(f"{vertex} ", end="")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)
