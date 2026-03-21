/**
 * Heap sort example (in-place, comparison-based) with minor API/format
 * improvements for readability. The observable behaviour (sorted output)
 * is unchanged.
 */
public class HeapSort {

    /**
     * Sorts the provided array in ascending order using heap sort.
     * The input array is modified in-place.
     *
     * @param arr array to sort (must be non-null)
     * @throws IllegalArgumentException if {@code arr} is null
     */
    public void sort(int[] arr) {
        if (arr == null)
            throw new IllegalArgumentException("arr must not be null");
        final int n = arr.length;

        // Build max heap
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }

        // Extract elements from heap one by one
        for (int i = n - 1; i >= 0; i--) {
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            // Heapify root element to maintain max-heap property
            heapify(arr, i, 0);
        }
    }

    /**
     * Heapify subtree rooted at index {@code i} for heap size {@code n}.
     */
    private static void heapify(int[] arr, int n, int i) {
        int largest = i; // Initialize largest as root
        int l = 2 * i + 1; // left = 2*i + 1
        int r = 2 * i + 2; // right = 2*i + 2

        if (l < n && arr[l] > arr[largest])
            largest = l;

        if (r < n && arr[r] > arr[largest])
            largest = r;

        // If largest is not root
        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;

            // Recursively heapify the affected subtree
            heapify(arr, n, largest);
        }
    }

    /**
     * Print array elements separated by a space (keeps original demo output).
     *
     * @param arr array to print (must be non-null)
     */
    static void printArray(int[] arr) {
        if (arr == null)
            return;
        final int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver code (keeps original sample)
    public static void main(String[] args) {
        int[] arr = { 1, 12, 9, 5, 6, 10 };

        HeapSort hs = new HeapSort();
        hs.sort(arr);

        System.out.println("Sorted array is");
        printArray(arr);
    }
}