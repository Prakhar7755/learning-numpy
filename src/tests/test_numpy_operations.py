# Example test file: src/tests/test_numpy_operations.py
import numpy as np
import unittest

class TestNumpyOperations(unittest.TestCase):

    def test_array_creation(self):
        arr = np.array([1, 2, 3])
        self.assertEqual(arr.shape, (3,))
    
    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()
