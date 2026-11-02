# Task 36 - joining numpy arrays
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.concatenate((a, b)))

# 2d, by rows and by columns
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print(np.concatenate((m1, m2), axis=0))   # stack down
print(np.concatenate((m1, m2), axis=1))   # stack sideways

# stack functions
print(np.stack((a, b), axis=0))
print(np.stack((a, b), axis=1))
print(np.hstack((a, b)))
print(np.vstack((a, b)))
print(np.dstack((a, b)))

# append
print(np.append(a, [7, 8]))

# insert
print(np.insert(a, 1, 99))
