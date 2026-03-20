
/**
 * CountingSort.java
 *
 * Counting sort implementation for non-negative integers. This class provides a
 * straightforward in-place sorting routine (the algorithm internally uses an
 * output buffer). The public behavior is preserved; edits focus on
 * documentation, validation and readability.
 */

import java.util.Arrays;
import java.util.Objects;

public class CountingSort {

    /**
     * Sorts the first {@code size} elements of {@code array} in ascending order
     * using counting sort. The array must contain non-negative integers.
     *
     * @param array the array to sort (must not be null)
     * @param size  number of elements to sort (must be between 0 and array.length)
     * @throws NullPointerException     if array is null
     * @throws IllegalArgumentException if size is out of range
     */
    public void countSort(int[] array, int size) {
        Objects.requireNonNull(array, "array must not be null");
        if (size < 0 || size > array.length) {
            throw new IllegalArgumentException("size is out of range");
        }

        if (size == 0) {
            return;
        }

        int[] output = new int[size];

        // Find the largest element of the array
        int max = array[0];
        for (int i = 1; i < size; i++) {
            if (array[i] > max) {
                max = array[i];
            }
        }

        int[] count = new int[max + 1];

        // Store the count of each element
        for (int i = 0; i < size; i++) {
            count[array[i]]++;
        }

        // Store the cumulative count
        for (int i = 1; i <= max; i++) {
            count[i] += count[i - 1];
        }

        // Build the output array (stable)
        for (int i = size - 1; i >= 0; i--) {
            output[count[array[i]] - 1] = array[i];
            count[array[i]]--;
        }

        // Copy the sorted elements into original array
        for (int i = 0; i < size; i++) {
            array[i] = output[i];
        }
    }

    // Driver code
    public static void main(String[] args) {
        int[] data = { 4, 2, 2, 8, 3, 3, 1 };
        int size = data.length;
        CountingSort cs = new CountingSort();
        cs.countSort(data, size);
        System.out.println("Sorted Array in Ascending Order:");
        System.out.println(Arrays.toString(data));
    }
}