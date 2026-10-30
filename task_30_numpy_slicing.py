# Task 30 - numpy slicing
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7])

print(a[1:5])
print(a[4:])
print(a[:4])
print(a[-3:-1])
print(a[::2])
print(a[::-1])

# 2d slicing
m = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15]])

print(m[1, 1:4])        # from second row take cols 1 to 3
print(m[0:2, 2])        # first two rows, third column
print(m[0:2, 1:4])      # block
print(m[:, ::2])        # every second column
print(m[::2, :])        # every second row

# slices share memory with the original
part = m[0, :3]
part[0] = 999
print(m[0])   # original changed too
