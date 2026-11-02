# Task 37 - splitting numpy arrays
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])

parts = np.array_split(a, 3)
print(parts)
print(parts[0], parts[1], parts[2])

# uneven split still works with array_split
print(np.array_split(a, 4))

# split needs it to divide evenly
print(np.split(a, 2))

# 2d
m = np.arange(1, 13).reshape(4, 3)
print(m)
for p in np.array_split(m, 2):
    print(p)
    print("--")

# split by column
for p in np.array_split(m, 3, axis=1):
    print(p)
    print("--")

print(np.hsplit(m, 3))
print(np.vsplit(m, 2))

# split at specific positions
print(np.split(a, [2, 4]))

# delete
print(np.delete(a, 0))
