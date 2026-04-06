
/**
 * Breadth-first search (BFS) example using an adjacency list.
 *
 * This file preserves the original traversal order and output while
 * improving readability and adding simple input validation.
 */

import java.util.Iterator;
import java.util.LinkedList;

class Graph {
    private final int V;
    private final LinkedList<Integer>[] adj;

    /**
     * Create a graph with {@code v} vertices (0-based indices [0..v-1]).
     *
     * @param v number of vertices (must be positive)
     * @throws IllegalArgumentException if {@code v} is not positive
     */
    @SuppressWarnings("unchecked")
    Graph(int v) {
        if (v <= 0)
            throw new IllegalArgumentException("number of vertices must be positive");
        this.V = v;
        this.adj = new LinkedList[v];
        for (int i = 0; i < v; ++i) {
            adj[i] = new LinkedList<Integer>();
        }
    }

    /**
     * Add a directed edge from vertex {@code v} to vertex {@code w}.
     *
     * @throws IndexOutOfBoundsException if {@code v} or {@code w} is out of range
     */
    void addEdge(int v, int w) {
        if (v < 0 || v >= V || w < 0 || w >= V)
            throw new IndexOutOfBoundsException("vertex index out of range");
        adj[v].add(w);
    }

    /**
     * Perform breadth-first traversal starting from vertex {@code s} and print
     * each visited vertex to standard output separated by a space.
     *
     * @param s start vertex
     * @throws IndexOutOfBoundsException if {@code s} is out of range
     */
    void BFS(int s) {
        if (s < 0 || s >= V)
            throw new IndexOutOfBoundsException("start vertex out of range");

        boolean[] visited = new boolean[V];
        LinkedList<Integer> queue = new LinkedList<Integer>();

        visited[s] = true;
        queue.add(s);

        while (!queue.isEmpty()) {
            int u = queue.poll();
            System.out.print(u + " ");

            Iterator<Integer> i = adj[u].listIterator();
            while (i.hasNext()) {
                int n = i.next();
                if (!visited[n]) {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }

    public static void main(String[] args) {
        Graph g = new Graph(4);

        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 3);

        System.out.println("Following is Breadth First Traversal (starting from vertex 2)");

        g.BFS(2);
    }
}