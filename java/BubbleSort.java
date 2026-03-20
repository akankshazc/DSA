
/**
 * BubbleSort.java
 *
 * Simple implementation of bubble sort with a small demo. The algorithm and
 * observable behavior are preserved; this edit focuses on readability,
 * documentation and API clarity.
 */

import java.util.Arrays;
import java.util.Objects;

public class BubbleSort {

    /**
     * Sorts the provided integer array in ascending order using bubble sort.
     * This method performs the sort in-place.
     *
     * @param array the array to sort (must not be null)
     * @throws NullPointerException if array is null
     */
    public static void bubbleSort(int[] array) {
        Objects.requireNonNull(array, "array must not be null");
        int size = array.length;

        for (int i = 0; i < size - 1; i++) {
            for (int j = 0; j < size - i - 1; j++) {
                // compare two adjacent elements
                // change > to < to sort in descending order
                if (array[j] > array[j + 1]) {
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
    }

    /**
     * Small demo that runs bubble sort on a short sample array.
     * 
     * @param args command-line arguments (ignored)
     */
    public static void main(String[] args) {
        int[] data = { -2, 45, 0, 11, -9 };
        System.out.println("Original: " + Arrays.toString(data));

        bubbleSort(data);

        System.out.println("Sorted Array in Ascending Order:");
        System.out.println(Arrays.toString(data));
    }
}