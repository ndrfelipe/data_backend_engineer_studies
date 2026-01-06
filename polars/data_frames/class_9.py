"""
Docstring for polars.data_frames.class_9

Create data frame using multiple methods

"""
import polars as pl
# Dictionary

data = {
    "Id": 1,
    "name": "Andre",
    "Profission": "Software Engineer",
    "Age": 21
}

df = pl.DataFrame(data)

print(df)
print(df.columns)
print(type(df))
print(len(df))

# List
data_list = [
                [1, "andre", 21],
                [2, "andre27", 22],
                [3, "andre28", 23],
                [4, "andre29", 24],
             ]
df_list   = pl.DataFrame(data_list, schema=["Id", "Name", "Age"])
print(df_list)

# List + Dictionary

data = {
    'Name': ['Alice', 'Bob', 'Andre'],
    'Age': [25, 20, 21],
    'Scores': [[85,90,84], [78, 82, 93], [90, 93, 98]],
    'Details': [
        {'City': 'New York', 'job': 'Rapper'},
        {'City': 'London', 'job': 'Doctor'},
        {'City': 'Toronto', 'job': 'Software Engineer'}
    ]
}

print(data)
df = pl.DataFrame(data)
print(df)

# using pandas
print("\nusing pandas")

import pandas as pd

df_pandas = pd.DataFrame(data)
print(df_pandas)

# Convert df_pandas to polars

print("\nConvert df_pandas to polars")
df_polars_from_pandas = pl.from_pandas(df_pandas)
print(df_polars_from_pandas)

print("\n Convert pandas to polars using .to_pandas()")

df_pandas_from_polars = df.to_pandas()
print(df_polars_from_pandas)