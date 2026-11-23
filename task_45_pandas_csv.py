# Task 45 - reading and writing csv files with pandas
import pandas as pd

# make a csv first so the script works on its own
df = pd.DataFrame({
    "name": ["ali", "sara", "bilal", "hina", "omar"],
    "marks": [78, 91, 65, 88, 54],
    "grade": ["B", "A", "C", "B", "D"],
})
df.to_csv("students.csv", index=False)
print("saved students.csv")

# read it back
data = pd.read_csv("students.csv")
print(data)

# first and last rows
print(data.head(2))
print(data.tail(2))

# info about the file
print(data.shape)
print(data.dtypes)

# print everything as a string
print(data.to_string())

# read only some columns
print(pd.read_csv("students.csv", usecols=["name", "marks"]))

# read only first 3 rows
print(pd.read_csv("students.csv", nrows=3))

# use a column as the index
print(pd.read_csv("students.csv", index_col="name"))

# save a filtered version
data[data["marks"] > 70].to_csv("top_students.csv", index=False)
print(pd.read_csv("top_students.csv"))
