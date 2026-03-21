
/**
 * Huffman Coding example (constructs a Huffman tree and prints codes).
 *
 * This file preserves the original demonstration logic and output while
 * improving readability and adding documentation.
 */

import java.util.PriorityQueue;
import java.util.Comparator;

/**
 * Node used by the Huffman tree. Package-private for simplicity in this
 * small demo (keeps structure identical to the original implementation).
 */
class HuffmanNode {
    int item; // frequency or weight
    char c; // character for leaf nodes
    HuffmanNode left;
    HuffmanNode right;
}

/**
 * Comparator to order HuffmanNode instances by their weight (item).
 */
class ImplementComparator implements Comparator<HuffmanNode> {
    @Override
    public int compare(HuffmanNode x, HuffmanNode y) {
        return x.item - y.item;
    }
}

/**
 * Main demo class for Huffman coding. Kept public to match filename and to
 * allow direct execution via `java Huffman`.
 */
public class Huffman {

    /**
     * Recursively print Huffman codes for leaf nodes. This method is
     * defensive: it returns immediately for a null root (no-op).
     *
     * @param root current subtree root
     * @param s    accumulated bit string for the path to {@code root}
     */
    public static void printCode(HuffmanNode root, String s) {
        if (root == null)
            return;

        if (root.left == null && root.right == null && Character.isLetter(root.c)) {
            System.out.println(root.c + "   |  " + s);
            return;
        }

        printCode(root.left, s + "0");
        printCode(root.right, s + "1");
    }

    public static void main(String[] args) {

        int n = 4;
        char[] charArray = { 'A', 'B', 'C', 'D' };
        int[] charfreq = { 5, 1, 6, 3 };

        PriorityQueue<HuffmanNode> q = new PriorityQueue<>(n, new ImplementComparator());

        for (int i = 0; i < n; i++) {
            HuffmanNode hn = new HuffmanNode();
            hn.c = charArray[i];
            hn.item = charfreq[i];
            hn.left = null;
            hn.right = null;
            q.add(hn);
        }

        HuffmanNode root = null;

        while (q.size() > 1) {
            HuffmanNode x = q.poll();
            HuffmanNode y = q.poll();

            HuffmanNode f = new HuffmanNode();
            f.item = x.item + y.item;
            f.c = '-';
            f.left = x;
            f.right = y;
            root = f;

            q.add(f);
        }

        System.out.println(" Char | Huffman code ");
        System.out.println("--------------------");
        printCode(root, "");
    }
}