
/**
 * Depth-first search (DFS) example using an adjacency list. This class is a
 * small educational/demo implementation; the DFS traversal order and output
 * are preserved from the original example.
 */

import java.util.LinkedList;
import java.util.Iterator;

class Graph {
    private final LinkedList<Integer>[] adjLists;
    private final boolean[] visited;

    /**
     * Construct a graph with the given number of vertices (0..vertices-1).
     *
     * @param vertices number of vertices (must be > 0)
     * @throws IllegalArgumentException if vertices &lt;= 0
     */
    @SuppressWarnings("unchecked")
    Graph(int vertices) {
        if (vertices <= 0)
            throw new IllegalArgumentException("vertices must be positive");
        adjLists = new LinkedList[vertices];
        visited = new boolean[vertices];

        for (int i = 0; i < vertices; i++) {
            adjLists[i] = new LinkedList<Integer>();
        }
    }

    /**
     * Add a directed edge from {@code src} to {@code dest}.
     */
    void addEdge(int src, int dest) {
        if (src < 0 || src >= adjLists.length || dest < 0 || dest >= adjLists.length)
            throw new IndexOutOfBoundsException("vertex index out of range");
        adjLists[src].add(dest);
    }

    /**
     * Perform DFS starting at {@code vertex}. Prints visited vertices to
     * standard output (space separated). Does not reset the visited array -
     * this preserves the original behaviour.
     *
     * @param vertex start vertex
     */
    void DFS(int vertex) {
        if (vertex < 0 || vertex >= adjLists.length)
            throw new IndexOutOfBoundsException("start vertex out of range");

        visited[vertex] = true;
        System.out.print(vertex + " ");

        Iterator<Integer> ite = adjLists[vertex].listIterator();
        while (ite.hasNext()) {
            int adj = ite.next();
            if (!visited[adj]) {
                DFS(adj);
            }
        }
    }

    public static void main(String args[]) {
        Graph g = new Graph(4);

        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 3);

        System.out.println("Following is Depth First Traversal");

        g.DFS(2);
    }
}