
/**
 * Adjacency-list representation (undirected) demo.
 *
 * This file demonstrates building a simple undirected graph using an
 * adjacency list backed by {@link java.util.ArrayList}. The example output
 * and algorithmic behaviour are preserved; the code is refactored for
 * readability and uses the {@link java.util.List} interface.
 */

import java.util.List;
import java.util.ArrayList;

class Graph {

    /**
     * Add an undirected edge between {@code s} and {@code d} in the
     * adjacency list {@code am}.
     *
     * @throws IndexOutOfBoundsException if s or d are out of range for am
     */
    static void addEdge(List<List<Integer>> am, int s, int d) {
        am.get(s).add(d);
        am.get(d).add(s);
    }

    public static void main(String[] args) {

        // Create the graph
        int V = 5;
        List<List<Integer>> am = new ArrayList<>(V);

        for (int i = 0; i < V; i++) {
            am.add(new ArrayList<Integer>());
        }

        // Add edges
        addEdge(am, 0, 1);
        addEdge(am, 0, 2);
        addEdge(am, 0, 3);
        addEdge(am, 1, 2);

        printGraph(am);
    }

    // Print the graph (keeps the original printed layout)
    static void printGraph(List<List<Integer>> am) {
        for (int i = 0; i < am.size(); i++) {
            System.out.println("\nVertex " + i + ":");
            for (Integer neighbor : am.get(i)) {
                System.out.print(" -> " + neighbor);
            }
            System.out.println();
        }
    }
}