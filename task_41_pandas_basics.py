# Task 41 - pandas basics
import pandas as pd

# a tiny table
data = {
    "name": ["ali", "sara", "bilal", "hina"],
    "age": [21, 23, 22, 24],
    "city": ["lahore", "karachi", "lahore", "multan"],
}
df = pd.DataFrame(data)
print(df)

print("\nversion:", pd.__version__)
print("\nshape:", df.shape)
print("\ncolumns:", list(df.columns))

# one column
print("\n", df["name"])

# filter rows
print("\n", df[df["age"] > 21])
print("\n", df[df["city"] == "lahore"])

# new column
df["age_next_year"] = df["age"] + 1
print("\n", df)

# quick stats
print("\naverage age:", df["age"].mean())
print("oldest:", df.loc[df["age"].idxmax(), "name"])

# sort
print("\n", df.sort_values("age", ascending=False))
