'''
 * @file   CocktailShakerSort.py
 * @author (original python) Tyla Hart, tyla.hart@ufl.edu
 * @date   1 Oct 2024
 * @version 0.1
 * @brief   Cocktail Shaker Sort implementation
'''

class CocktailShakerSort:
    """
    Cocktail Shaker Sort is a variation of Bubble Sort that sorts 
    in both directions on each pass through the list.
    """

    def __init__(self):
        pass

    def sort(self, arr):
        """Sorts the array using Cocktail Shaker Sort algorithm."""
        n = len(arr)
        if n <= 1:
            return arr

        sorted = False
        start = 0
        end = n - 1

        while not sorted:
            sorted = True
            
            # Forward pass
            for i in range(start, end):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    sorted = False

            # If nothing moved, the array is sorted
            if sorted:
                break

            # Decrease end index for the next pass
            end -= 1

            # Backward pass
            for i in range(end, start, -1):
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                    sorted = False
            
            # Increase start index for the next pass
            start += 1

        return arr


if __name__ == '__main__':
    """
    Example usage
    """
    array = [11, 4, 6, 4, 8, -13, 2, 3]
    sorter = CocktailShakerSort()
    sorted_array = sorter.sort(array)
    # Prints:
    # [-13, 2, 3, 4, 4, 6, 8, 11]
    print(sorted_array)
