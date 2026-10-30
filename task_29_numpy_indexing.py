# Task 29 - numpy indexing
import numpy as np

a = np.array([10, 20, 30, 40, 50])
print(a[0], a[-1], a[2])

# 2d indexing
m = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10]])
print(m[0, 1])      # row 0, col 1
print(m[1, -1])     # last item of second row
print(m[1])         # whole second row
print(m[:, 2])      # whole third column

# 3d
t = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(t[0, 1, 2])

# true / false selection
nums = np.array([3, 8, 1, 9, 4, 7])
print(nums > 5)
print(nums[nums > 5])
print(nums[(nums > 2) & (nums < 8)])

# fancy indexing (pick positions)
print(nums[[0, 2, 4]])
