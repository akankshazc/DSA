/**
 * Adjacency-matrix representation for an undirected graph.
 *
 * This class is a compact demo of using a boolean matrix to represent an
 * undirected graph. The implementation preserves the original behaviour and
 * demo output; changes are limited to documentation, input validation and
 * minor readability improvements.
 */
class Graph {
    private final boolean[][] adjMatrix;
    private final int numVertices;

    /**
     * Create a graph with {@code numVertices} vertices (0..numVertices-1).
     *
     * @throws IllegalArgumentException if {@code numVertices} is not positive
     */
    public Graph(int numVertices) {
        if (numVertices <= 0)
            throw new IllegalArgumentException("numVertices must be positive");
        this.numVertices = numVertices;
        this.adjMatrix = new boolean[numVertices][numVertices];
    }

    /**
     * Add an undirected edge between {@code i} and {@code j}.
     *
     * @throws IndexOutOfBoundsException if {@code i} or {@code j} is out of range
     */
    public void addEdge(int i, int j) {
        checkVertex(i);
        checkVertex(j);
        adjMatrix[i][j] = true;
        adjMatrix[j][i] = true;
    }

    /**
     * Remove the undirected edge between {@code i} and {@code j}.
     *
     * @throws IndexOutOfBoundsException if {@code i} or {@code j} is out of range
     */
    public void removeEdge(int i, int j) {
        checkVertex(i);
        checkVertex(j);
        adjMatrix[i][j] = false;
        adjMatrix[j][i] = false;
    }

    private void checkVertex(int v) {
        if (v < 0 || v >= numVertices)
            throw new IndexOutOfBoundsException("vertex index out of range: " + v);
    }

    /**
     * Return a textual representation of the adjacency matrix where each row
     * starts with the vertex index followed by 0/1 entries for each column.
     */
    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        for (int i = 0; i < numVertices; i++) {
            s.append(i).append(": ");
            for (int j = 0; j < numVertices; j++) {
                s.append(adjMatrix[i][j] ? '1' : '0').append(' ');
            }
            s.append('\n');
        }
        return s.toString();
    }

    public static void main(String args[]) {
        Graph g = new Graph(4);

        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);

        System.out.print(g.toString());
    }
}