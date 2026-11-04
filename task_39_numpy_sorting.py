# Task 39 - sorting numpy arrays
import numpy as np

a = np.array([3, 2, 0, 1, 9, 4])
print(np.sort(a))
print(a)             # original untouched

# sort in place
a.sort()
print(a)

# descending
print(np.sort(a)[::-1])

# strings and booleans
print(np.sort(np.array(["banana", "apple", "cherry"])))
print(np.sort(np.array([True, False, True])))

# 2d sorts each row
m = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(m))
print(np.sort(m, axis=0))     # each column

# argsort gives the order of indexes
names = np.array(["ali", "sara", "bilal"])
marks = np.array([70, 95, 82])
order = np.argsort(marks)
print(order)
print(names[order])            # names from lowest to highest marks
print(names[order][::-1])      # highest first
