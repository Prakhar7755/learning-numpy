""" 
Data Types in Python
By default Python have these data types:

strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
integer - used to represent integer numbers. e.g. -1, -2, -3
float - used to represent real numbers. e.g. 1.2, 42.42
boolean - used to represent True or False.
complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j
"""


""" 
Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype) #int64


arr2 = np.array(['apple', 'banana', 'cherry'])
print(arr2.dtype) # <U6



# ARRAY WITH DEFINED DATATYPE - dtype arg


arr = np.array([1, 2, 3, 4], dtype='S')

print(arr) #  [b'1' b'2' b'3' b'4']
print(arr.dtype) #  |S1


# For i, u, f, S and U we can define size as well.

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)
# [1 2 3 4]
# int32

""" What if a Value Can Not Be Converted?
If a type is given in which elements can't be casted then NumPy will raise a ValueError.

ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.

Example
A non integer string like 'a' can not be converted to integer (will raise an error):
 """
# arr = np.array(['a', '2', '3'], dtype='i')
 
 
 
 
#   CONVERTING AN EXISTING ARR TO A NEW TYPE - astype()

newarr1 = arr.astype('i')

newarr2 = arr.astype(int)
newarr3 = arr.astype(float)
newarr4 = arr.astype(bool)


print(newarr1)
print(newarr2)
print(newarr3)
print(newarr4)
#  [1 2 3 4]
#  [1 2 3 4]
#  [1. 2. 3. 4.]
#  [ True  True  True  True]
