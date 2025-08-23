
"""
Depth-First Search (DFS) algorithm in Python.
"""

from typing import Dict, Set, Optional


def dfs(graph: Dict[str, Set[str]], start: str, visited: Optional[Set[str]] = None) -> Set[str]:
    """
    Perform DFS traversal from the start node.
    """
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited


if __name__ == "__main__":
    graph = {
        '0': {'1', '2'},
        '1': {'0', '3', '4'},
        '2': {'0'},
        '3': {'1'},
        '4': {'2', '3'}
    }
    dfs(graph, '0')
