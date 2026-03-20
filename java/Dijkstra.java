
/**
 * Dijkstra.java
 *
 * A clean, documented implementation of Dijkstra's shortest-path algorithm
 * for small adjacency-matrix graphs. The implementation preserves the
 * algorithm's behavior while adding validation, clearer names and a
 * method that returns the computed distances so callers can reuse them.
 */

import java.util.Arrays;
import java.util.Objects;

public class Dijkstra {

    /**
     * Compute shortest path distances from the given source to all vertices
     * using Dijkstra's algorithm. The graph is expected to be an adjacency
     * matrix where a 0 indicates no direct edge (except on the diagonal).
     *
     * @param graph  adjacency matrix (must be non-null and square)
     * @param source source vertex index
     * @return array of distances from source to every vertex
     * @throws NullPointerException     if graph is null
     * @throws IllegalArgumentException if graph is not square or source is invalid
     */
    public static int[] dijkstra(int[][] graph, int source) {
        Objects.requireNonNull(graph, "graph must not be null");
        final int n = graph.length;
        for (int[] row : graph) {
            if (row.length != n) {
                throw new IllegalArgumentException("graph must be a square matrix");
            }
        }
        if (source < 0 || source >= n) {
            throw new IllegalArgumentException("source index out of bounds");
        }

        boolean[] visited = new boolean[n];
        int[] distance = new int[n];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[source] = 0; // distance to self is zero

        for (int i = 0; i < n; i++) {
            int u = findMinDistance(distance, visited);
            if (u == -1) {
                // Remaining vertices are unreachable from source
                break;
            }
            visited[u] = true;

            for (int v = 0; v < n; v++) {
                // graph[u][v] != 0 indicates an edge; skip visited vertices
                if (!visited[v] && graph[u][v] != 0 && distance[u] != Integer.MAX_VALUE) {
                    int newDist = distance[u] + graph[u][v];
                    if (newDist < distance[v]) {
                        distance[v] = newDist;
                    }
                }
            }
        }
        return distance;
    }

    /**
     * Helper that finds the unvisited vertex with the smallest tentative
     * distance. Returns -1 when no such vertex exists (all remaining
     * vertices are unreachable).
     */
    private static int findMinDistance(int[] distance, boolean[] visited) {
        int min = Integer.MAX_VALUE;
        int minIndex = -1;
        for (int i = 0; i < distance.length; i++) {
            if (!visited[i] && distance[i] < min) {
                min = distance[i];
                minIndex = i;
            }
        }
        return minIndex;
    }

    /**
     * Demo: constructs an example graph and prints shortest distances from
     * the source vertex 0. Output format is preserved from the original
     * example.
     */
    public static void main(String[] args) {
        int[][] graph = new int[][] {
                { 0, 0, 1, 2, 0, 0, 0 },
                { 0, 0, 2, 0, 0, 3, 0 },
                { 1, 2, 0, 1, 3, 0, 0 },
                { 2, 0, 1, 0, 0, 0, 1 },
                { 0, 0, 3, 0, 0, 2, 0 },
                { 0, 3, 0, 0, 2, 0, 1 },
                { 0, 0, 0, 1, 0, 1, 0 }
        };

        int source = 0;
        int[] distances = dijkstra(graph, source);

        for (int i = 0; i < distances.length; i++) {
            System.out.println(String.format("Distance from %d to %d is %d", source, i, distances[i]));
        }
    }
}