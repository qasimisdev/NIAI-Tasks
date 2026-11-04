# Task 38 - searching numpy arrays
import numpy as np

a = np.array([1, 2, 3, 4, 5, 4, 4])

# where gives positions
print(np.where(a == 4))
print(np.where(a % 2 == 0))

# where with 3 args works like if/else for every item
print(np.where(a > 3, "big", "small"))

# searchsorted works on a sorted array
s = np.array([6, 7, 8, 9])
print(np.searchsorted(s, 7))
print(np.searchsorted(s, 7, side="right"))
print(np.searchsorted(s, [2, 4, 10]))

# argmax and argmin
print("max at", a.argmax(), "min at", a.argmin())

# any and all
print((a > 3).any(), (a > 0).all())

# count matches
print((a == 4).sum())

# is a value in the array
print(4 in a, 99 in a)

# 2d
m = np.array([[1, 9], [5, 3]])
print(np.where(m > 4))
