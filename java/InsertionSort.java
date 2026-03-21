
/**
 * Insertion sort example.
 *
 * This class provides a small, self-contained insertion-sort implementation
 * and a demo runner. The algorithmic logic is preserved from the original
 * implementation; changes are limited to documentation, visibility, and a
 * null-check for clearer error reporting.
 */
import java.util.Arrays;

public class InsertionSort {

    /**
     * Sorts the given array in ascending order using insertion sort.
     * The method mutates the provided array in-place.
     *
     * @param array the array to sort (must not be null)
     * @throws IllegalArgumentException if {@code array} is null
     */
    public static void insertionSort(int[] array) {
        if (array == null)
            throw new IllegalArgumentException("array must not be null");

        int size = array.length;

        for (int step = 1; step < size; step++) {
            int key = array[step];
            int j = step - 1;

            // Compare key with each element on the left of it until an element smaller than
            // it is found.
            // For descending order, change key<array[j] to key>array[j].
            while (j >= 0 && key < array[j]) {
                array[j + 1] = array[j];
                --j;
            }

            // Place key after the element just smaller than it.
            array[j + 1] = key;
        }
    }

    // Driver / demo
    public static void main(String[] args) {
        int[] data = { 9, 5, 1, 4, 3 };
        insertionSort(data);
        System.out.println("Sorted Array in Ascending Order: ");
        System.out.println(Arrays.toString(data));
    }
}