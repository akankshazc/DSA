
/**
 * Small demonstration of Java's {@link java.util.Hashtable} usage.
 *
 * The example is intentionally minimal and preserves the original
 * behaviour: create a table, add a few entries, remove one, then print
 * the resulting map.
 */
import java.util.Hashtable;
import java.util.Map;

public class HashTable {

    /**
     * Create and return a small sample hashtable used by {@link #main}.
     * Kept separate to improve readability and make the demo logic reusable
     * without changing observable behaviour.
     */
    private static Map<Integer, Integer> createSampleTable() {
        Map<Integer, Integer> ht = new Hashtable<>();

        ht.put(123, 432);
        ht.put(12, 2345);
        ht.put(15, 5643);
        ht.put(3, 321);

        ht.remove(12);

        return ht;
    }

    /**
     * Program entry point. Prints the sample hashtable to stdout.
     */
    public static void main(String[] args) {
        Map<Integer, Integer> ht = createSampleTable();
        System.out.println(ht);
    }
}