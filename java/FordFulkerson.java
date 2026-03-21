// Ford-Fulkerson algorithm in Java

import java.util.LinkedList;

/**
 * Simple Ford–Fulkerson implementation using BFS (Edmonds–Karp variant).
 *
 * This class provides a small, self-contained implementation intended for
 * educational/demo purposes. It preserves the original algorithmic behavior
 * while improving readability and input validation.
 */
public class FordFulkerson {

    /**
     * Breadth-first search over the residual graph. Fills {@code parent} with
     * the discovered path (parent[v] = u means edge u->v is in the path).
     *
     * @param residual residual capacity graph (non-null, square)
     * @param s        source vertex
     * @param t        sink vertex
     * @param parent   preallocated int[] used to store the path; must have length
     *                 == n
     * @return true if there is a path from s to t in residual with positive
     *         capacity
     */
    public static boolean bfs(int[][] residual, int s, int t, int[] parent) {
        if (residual == null)
            throw new IllegalArgumentException("residual must not be null");
        final int n = residual.length;
        if (parent == null || parent.length != n)
            throw new IllegalArgumentException("parent must be non-null and length == residual.length");

        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; ++i)
            visited[i] = false;

        LinkedList<Integer> queue = new LinkedList<>();
        queue.add(s);
        visited[s] = true;
        parent[s] = -1;

        while (!queue.isEmpty()) {
            int u = queue.poll();
            for (int v = 0; v < n; v++) {
                if (!visited[v] && residual[u][v] > 0) {
                    queue.add(v);
                    parent[v] = u;
                    visited[v] = true;
                }
            }
        }

        return visited[t];
    }

    /**
     * Compute the max flow from s to t using the Ford–Fulkerson method
     * (Edmonds–Karp implementation using BFS for path discovery).
     *
     * @param graph adjacency matrix of capacities (non-null, square)
     * @param s     source index (0-based)
     * @param t     sink index (0-based)
     * @return the value of the maximum flow
     */
    public static int fordFulkerson(int[][] graph, int s, int t) {
        if (graph == null)
            throw new IllegalArgumentException("graph must not be null");
        final int n = graph.length;
        for (int i = 0; i < n; i++) {
            if (graph[i] == null || graph[i].length != n)
                throw new IllegalArgumentException("graph must be a square matrix");
        }
        if (s < 0 || s >= n || t < 0 || t >= n)
            throw new IllegalArgumentException("source/sink out of bounds");

        // Create residual graph as a copy of the original capacities
        int[][] residual = new int[n][n];
        for (int u = 0; u < n; u++) {
            System.arraycopy(graph[u], 0, residual[u], 0, n);
        }

        int[] parent = new int[n];
        int maxFlow = 0;

        // While there exists an augmenting path, add its bottleneck to maxFlow
        while (bfs(residual, s, t, parent)) {
            int pathFlow = Integer.MAX_VALUE;
            for (int v = t; v != s; v = parent[v]) {
                int u = parent[v];
                pathFlow = Math.min(pathFlow, residual[u][v]);
            }

            for (int v = t; v != s; v = parent[v]) {
                int u = parent[v];
                residual[u][v] -= pathFlow;
                residual[v][u] += pathFlow;
            }

            maxFlow += pathFlow;
        }

        return maxFlow;
    }

    public static void main(String[] args) {
        int[][] graph = new int[][] {
                { 0, 8, 0, 0, 3, 0 },
                { 0, 0, 9, 0, 0, 0 },
                { 0, 0, 0, 0, 7, 2 },
                { 0, 0, 0, 0, 0, 5 },
                { 0, 0, 7, 4, 0, 0 },
                { 0, 0, 0, 0, 0, 0 }
        };

        int maxFlow = fordFulkerson(graph, 0, 5);
        System.out.println("Max Flow: " + maxFlow);
    }
}