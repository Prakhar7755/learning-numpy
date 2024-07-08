import numpy as np

arr = np.array([2, 2, 3, 4, 5])

print(arr)

print(type(arr)); """ <class 'numpy.ndarray'> """


arr0 = np.array(33);
print("0-D array ",arr0) 

arr1 = np.array([1, 2, 3, 4, 5])

print("1-D array",arr1)


arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("2-D array",arr2)


print(arr.ndim)
print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)