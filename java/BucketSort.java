
/**
 * BucketSort.java
 *
 * Simple bucket sort implementation for floating point numbers in [0, 1).
 * The method sorts the provided array in-place. This edit focuses on
 * documentation and readability; the algorithm itself is unchanged.
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.Arrays;
import java.util.Objects;

public class BucketSort {

    /**
     * Sorts the provided array of floats (expected in [0, 1)) using bucket sort.
     * The caller supplies n, the number of buckets to use (typically arr.length).
     *
     * Note: This method preserves the original algorithm and expression
     * for computing the bucket index: (int) arr[i] * n.
     *
     * @param arr array of floats to sort (must not be null)
     * @param n   number of buckets / expected number of elements
     * @throws NullPointerException if arr is null
     */
    public void bucketSort(float[] arr, int n) {
        Objects.requireNonNull(arr, "arr must not be null");
        if (n <= 0)
            return;

        @SuppressWarnings("unchecked")
        ArrayList<Float>[] bucket = new ArrayList[n];

        // Create empty buckets
        for (int i = 0; i < n; i++) {
            bucket[i] = new ArrayList<Float>();
        }

        // Add elements into the buckets
        for (int i = 0; i < n; i++) {
            int bucketIndex = (int) arr[i] * n;
            bucket[bucketIndex].add(arr[i]);
        }

        // Sort the elements of each bucket
        for (int i = 0; i < n; i++) {
            Collections.sort(bucket[i]);
        }

        // Concatenate buckets back into array
        int index = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0, size = bucket[i].size(); j < size; j++) {
                arr[index++] = bucket[i].get(j);
            }
        }
    }

    /**
     * Demo for BucketSort.
     */
    public static void main(String[] args) {
        BucketSort sorter = new BucketSort();
        float[] arr = { 0.42f, 0.32f, 0.33f, 0.52f, 0.37f, 0.47f, 0.51f };

        System.out.println("Original: " + Arrays.toString(arr));
        sorter.bucketSort(arr, 7);
        System.out.println("Sorted : " + Arrays.toString(arr));
    }
}