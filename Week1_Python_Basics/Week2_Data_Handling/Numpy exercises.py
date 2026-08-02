"""
Week 2 - NumPy Exercises
Covers: array creation, indexing, broadcasting, vectorized operations
"""

import numpy as np

print("=== 1. Array Creation ===")
arr1 = np.array([1, 2, 3, 4, 5])
print("1D array:", arr1)

arr2 = np.zeros((3, 3))
print("3x3 zeros:\n", arr2)

arr3 = np.ones((2, 4))
print("2x4 ones:\n", arr3)

arr4 = np.arange(0, 20, 2)
print("Range with step 2:", arr4)

arr5 = np.linspace(0, 1, 5)
print("Linspace (5 points between 0 and 1):", arr5)

arr6 = np.random.randint(1, 100, size=(3, 3))
print("Random 3x3 array:\n", arr6)


print("\n=== 2. Indexing & Slicing ===")
arr = np.array([10, 20, 30, 40, 50, 60])
print("Original:", arr)
print("First 3 elements:", arr[:3])
print("Last element:", arr[-1])
print("Every other element:", arr[::2])

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nMatrix:\n", matrix)
print("Element at row 1, col 2:", matrix[1, 2])
print("First row:", matrix[0, :])
print("Second column:", matrix[:, 1])
print("Sub-matrix (top-left 2x2):\n", matrix[:2, :2])


print("\n=== 3. Broadcasting ===")
a = np.array([1, 2, 3])
b = 10
print(f"{a} + {b} =", a + b)

matrix2 = np.array([[1, 2, 3], [4, 5, 6]])
row_vector = np.array([10, 20, 30])
print("Matrix + row vector (broadcast):\n", matrix2 + row_vector)

col_vector = np.array([[1], [2]])
print("Matrix + column vector (broadcast):\n", matrix2 + col_vector)


print("\n=== 4. Vectorized Operations ===")
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])

print("Element-wise addition:", x + y)
print("Element-wise multiplication:", x * y)
print("Square of x:", x ** 2)
print("Square root of y:", np.sqrt(y))
print("Sum of x:", np.sum(x))
print("Mean of y:", np.mean(y))
print("Max of x:", np.max(x))
print("Standard deviation of y:", np.std(y))

# Dot product
print("Dot product of x and y:", np.dot(x, y))

# Boolean masking (vectorized filtering)
print("Elements of y greater than 25:", y[y > 25])

# Vectorized conditional (np.where)
print("Replace values > 25 with 0, else keep:", np.where(y > 25, 0, y))