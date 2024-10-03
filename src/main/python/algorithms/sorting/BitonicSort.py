'''
 * @file   BitonicSort.py
 * @author (original python) Tyla Hart, tyla.hart@ufl.edu
 * @date   1 Oct 2024
 * @version 0.1
 * @brief   Bitonic sort implementation
'''

class BitonicSort:
    """
    Bitonic Sort is a parallelizable sorting algorithm based on the 
    principle of creating a bitonic sequence and then merging.
    """

    def __init__(self):
        pass

    def sort(self, arr):
        """Sorts the array using Bitonic Sort algorithm."""
        n = len(arr)
        next_pow2 = 1
        while next_pow2 < n:
            next_pow2 *= 2
        arr += [0] * (next_pow2 - n)  # Extend array to the next power of 2
        self.bitonic_sort(arr, 0, len(arr), 1)
        return arr

    def compare_and_swap(self, arr, i, j, direction):
        """Compares and swaps the elements at indices i and j based on the direction."""
        if (direction == 1 and arr[i] > arr[j]) or (direction == 0 and arr[i] < arr[j]):
            arr[i], arr[j] = arr[j], arr[i]

    def bitonic_merge(self, arr, low, cnt, direction):
        """Merges a bitonic sequence in the specified direction."""
        if cnt > 1:
            k = cnt // 2
            for i in range(low, low + k):
                self.compare_and_swap(arr, i, i + k, direction)
            self.bitonic_merge(arr, low, k, direction)
            self.bitonic_merge(arr, low + k, k, direction)

    def bitonic_sort(self, arr, low, cnt, direction):
        """Sorts a bitonic sequence in the specified direction."""
        if cnt > 1:
            k = cnt // 2
            # Sort in ascending order
            self.bitonic_sort(arr, low, k, 1)
            # Sort in descending order
            self.bitonic_sort(arr, low + k, k, 0)
            # Merge the whole sequence in the specified direction
            self.bitonic_merge(arr, low, cnt, direction)


if __name__ == '__main__':
    """
    Example usage
    """
    array = [-10, 4, 6, 4, 8, -13, 2, 3]
    sorter = BitonicSort()
    sorted_array = sorter.sort(array)
    # Prints:
    # [-13, -10, 2, 3, 4, 4, 6, 8]
    print(sorted_array[:len(array)])  # Print only original length
