# Searching Arrays
""" You can search an array for a certain value, and return the indexes that get a match.

To search an array, use the where() method. """
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x) # (array([3, 5, 6]),)




arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x) #(array([1, 3, 5, 7]),)



# Search Sorted
""" There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.

The searchsorted() method is assumed to be used on sorted arrays. """

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x) # 1