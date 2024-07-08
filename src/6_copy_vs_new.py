import numpy as np

# The view SHOULD be affected by the changes made to the original array.

arr = np.array([1, 2, 3, 4, 5])
y = arr.copy()
x = arr.view()
arr[0] = 42

print(arr)
print(x)
print(y)
# [42  2  3  4  5]
# [42  2  3  4  5]
# [1 2 3 4 5]


# The original array SHOULD be affected by the changes made to the view.

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)# [31  2  3  4  5]
print(x) # [31  2  3  4  5]




# Check if Array Owns its Data
""" As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
Every NumPy array has the attribute base that returns None if the array owns the data.
Otherwise, the base  attribute refers to the original object. """

# The copy returns None.
# The view returns the original array.

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base) # NOne
print(y.base) # [1,2,3,4,5]
