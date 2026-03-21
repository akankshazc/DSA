/**
 * Floyd-Warshall algorithm example (all-pairs shortest paths) with a
 * small, self-contained API and improved validation & documentation.
 *
 * Notes:
 * - This preserves the original algorithm behavior and sample output.
 * - Distances of "infinite" edges use the sentinel value {@code INF}.
 */
public class FloydWarshall {
    /**
     * A sentinel value representing "no path". Matches the original example.
     */
    public static final int INF = 9999;

    /**
     * Compute the all-pairs shortest-path distances using the Floyd–Warshall
     * algorithm. The input adjacency matrix is not modified; a new matrix is
     * returned with computed shortest distances.
     *
     * @param graph square adjacency matrix where graph[i][j] is the direct
     *              edge weight from i to j or {@code INF} if no direct edge
     * @return a new matrix (same dimensions as {@code graph}) with shortest
     *         path distances filled in
     * @throws IllegalArgumentException if {@code graph} is null or not square
     */
    public static int[][] floydWarshall(int[][] graph) {
        if (graph == null) {
            throw new IllegalArgumentException("graph must not be null");
        }

        final int n = graph.length;
        for (int i = 0; i < n; i++) {
            if (graph[i] == null || graph[i].length != n) {
                throw new IllegalArgumentException("graph must be a square matrix");
            }
        }

        int[][] dist = new int[n][n];

        // Copy input matrix so we don't mutate caller data.
        for (int i = 0; i < n; i++) {
            System.arraycopy(graph[i], 0, dist[i], 0, n);
        }

        // Standard Floyd–Warshall triple loop.
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }

        return dist;
    }

    /**
     * Pretty-print a distance matrix to standard output. Uses the same
     * "INF" sentinel token as the original example.
     *
     * @param matrix the distance matrix to print (must be square/non-null)
     */
    public static void printMatrix(int[][] matrix) {
        if (matrix == null)
            return;
        final int n = matrix.length;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == INF) {
                    System.out.print("INF ");
                } else {
                    System.out.print(matrix[i][j] + "  ");
                }
            }
            System.out.println();
        }
    }

    /**
     * Sample runner matching the original example. Compiles and runs the
     * algorithm on a small toy graph and prints the result.
     */
    public static void main(String[] args) {
        int[][] graph = {
                { 0, 3, INF, 5 },
                { 2, 0, INF, 4 },
                { INF, 1, 0, INF },
                { INF, INF, 2, 0 }
        };

        int[][] result = floydWarshall(graph);
        printMatrix(result);
    }
}