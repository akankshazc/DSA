
/**
 * Kosaraju's algorithm to find strongly connected components (SCCs).
 *
 * This is a small educational implementation; the algorithm and printed
 * output are preserved and only small style/input-validation improvements
 * have been applied.
 */

import java.util.Iterator;
import java.util.LinkedList;
import java.util.Stack;

class Graph {
    private final int V;
    private final LinkedList<Integer>[] adj;

    /**
     * Create a graph with {@code s} vertices (0..s-1).
     *
     * @throws IllegalArgumentException if {@code s} is not positive
     */
    @SuppressWarnings("unchecked")
    Graph(int s) {
        if (s <= 0)
            throw new IllegalArgumentException("number of vertices must be positive");
        V = s;
        adj = new LinkedList[s];
        for (int i = 0; i < s; ++i) {
            adj[i] = new LinkedList<Integer>();
        }
    }

    // Add edge
    void addEdge(int s, int d) {
        checkVertex(s);
        checkVertex(d);
        adj[s].add(d);
    }

    private void checkVertex(int v) {
        if (v < 0 || v >= V)
            throw new IndexOutOfBoundsException("vertex index out of range: " + v);
    }

    // DFS
    void DFSUtil(int s, boolean visitedVertices[]) {
        checkVertex(s);
        visitedVertices[s] = true;
        System.out.print(s + " ");

        Iterator<Integer> i = adj[s].iterator();
        while (i.hasNext()) {
            int n = i.next();
            if (!visitedVertices[n])
                DFSUtil(n, visitedVertices);
        }
    }

    // Transpose the graph
    Graph Transpose() {
        Graph g = new Graph(V);
        for (int s = 0; s < V; s++) {
            Iterator<Integer> i = adj[s].listIterator();
            while (i.hasNext()) {
                int d = i.next();
                g.adj[d].add(s);
            }
        }
        return g;
    }

    void fillOrder(int s, boolean visitedVertices[], Stack<Integer> stack) {
        checkVertex(s);
        visitedVertices[s] = true;

        Iterator<Integer> i = adj[s].iterator();
        while (i.hasNext()) {
            int n = i.next();
            if (!visitedVertices[n])
                fillOrder(n, visitedVertices, stack);
        }
        stack.push(Integer.valueOf(s));
    }

    // Print strongly connected component
    void printSCC() {
        Stack<Integer> stack = new Stack<>();

        boolean visitedVertices[] = new boolean[V];

        for (int i = 0; i < V; i++)
            if (!visitedVertices[i])
                fillOrder(i, visitedVertices, stack);

        Graph gr = Transpose();

        for (int i = 0; i < V; i++)
            visitedVertices[i] = false;

        while (!stack.isEmpty()) {
            int s = stack.pop().intValue();

            if (!visitedVertices[s]) {
                gr.DFSUtil(s, visitedVertices);
                System.out.println();
            }
        }
    }

    public static void main(String args[]) {
        Graph g = new Graph(8);
        g.addEdge(0, 1);
        g.addEdge(1, 2);
        g.addEdge(2, 3);
        g.addEdge(2, 4);
        g.addEdge(3, 0);
        g.addEdge(4, 5);
        g.addEdge(5, 6);
        g.addEdge(6, 4);
        g.addEdge(6, 7);

        System.out.println("Strongly Connected Components:");
        g.printSCC();
    }
}