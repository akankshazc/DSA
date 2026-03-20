
/**
 * BinarySearch.java
 *
 * A small, self-contained binary search example with documentation and
 * simple input validation. The algorithm behavior is preserved.
 */

import java.util.Arrays;
import java.util.Objects;

public class BinarySearch {

    /**
     * Perform binary search on a sorted int array (ascending order).
     *
     * @param array the sorted array to search (must not be null)
     * @param key   the value to search for
     * @param low   lower index (inclusive)
     * @param high  upper index (inclusive)
     * @return the index of the key if found, otherwise -1
     * @throws IllegalArgumentException if the array is null or indices are invalid
     */
    public static int binarySearch(int[] array, int key, int low, int high) {
        Objects.requireNonNull(array, "array must not be null");
        if (low < 0 || high >= array.length || low > high) {
            throw new IllegalArgumentException("Invalid low/high indices");
        }

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (key == array[mid]) {
                return mid;
            }
            if (key > array[mid]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }

    /**
     * Convenience overload that searches the entire array.
     *
     * @param array the sorted array to search (must not be null)
     * @param key   the value to search for
     * @return the index of the key if found, otherwise -1
     */
    public static int binarySearch(int[] array, int key) {
        Objects.requireNonNull(array, "array must not be null");
        if (array.length == 0) {
            return -1;
        }
        return binarySearch(array, key, 0, array.length - 1);
    }

    /**
     * Simple demo for BinarySearch.
     * Prints the result of searching for a value in a small array.
     */
    public static void main(String[] args) {
        int[] array = { 3, 4, 5, 6, 7, 8, 9 };
        int key = 4;

        System.out.println("Array: " + Arrays.toString(array));
        System.out.println("Searching for: " + key);

        int result = binarySearch(array, key);
        if (result == -1) {
            System.out.println("Not found");
        } else {
            System.out.println("Element found at index " + result);
        }
    }
}