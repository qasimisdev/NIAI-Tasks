# Task 43 - pandas series (one column of data)
import pandas as pd

a = pd.Series([1, 7, 2])
print(a)
print(a[0])

# custom labels
b = pd.Series([10, 20, 30], index=["x", "y", "z"])
print(b)
print(b["y"])

# from a dictionary
calories = {"day1": 420, "day2": 380, "day3": 390}
c = pd.Series(calories)
print(c)

# only some keys
print(pd.Series(calories, index=["day1", "day2"]))

# math works on whole series
print(c * 2)
print(c.mean(), c.max(), c.min(), c.sum())

# filter
print(c[c > 385])

# name it
c.name = "calories"
print(c)

# head / describe
print(c.describe())
