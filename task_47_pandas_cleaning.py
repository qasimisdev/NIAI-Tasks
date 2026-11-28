# Task 47 - cleaning messy data with pandas
import numpy as np
import pandas as pd

# deliberately messy data
df = pd.DataFrame({
    "name": ["ali", "sara", None, "bilal", "sara", "hina", "omar"],
    "age": [21, 23, 25, np.nan, 23, 250, 22],
    "city": ["lahore", "Karachi", "lahore", "LAHORE", "Karachi", "multan", None],
    "joined": ["2023-01-05", "2023-02-10", "not a date", "2023-03-15", "2023-02-10", "2023-04-01", "2023-05-20"],
})
print("original")
print(df)

# 1. missing values
print("\nmissing per column")
print(df.isnull().sum())

# 2. fill or drop
df["age"] = df["age"].fillna(df["age"].median())
df["city"] = df["city"].fillna("unknown")
df = df.dropna(subset=["name"])

# 3. duplicates
print("\nduplicates:", df.duplicated().sum())
df = df.drop_duplicates()

# 4. fix text (same city written different ways)
df["city"] = df["city"].str.lower().str.strip()

# 5. fix wrong dates
df["joined"] = pd.to_datetime(df["joined"], errors="coerce")

# 6. impossible values (age 250)
df.loc[df["age"] > 100, "age"] = df["age"].median()

# 7. fix types
df["age"] = df["age"].astype(int)

print("\ncleaned")
print(df)
print(df.dtypes)
