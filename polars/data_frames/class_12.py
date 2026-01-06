"""
How to work with NumPy and pandas with polars
"""

import polars as pl
import numpy  as np
import pandas as pd

csv_file = "../polars/Files/Sample_Superstore.csv"
df = pl.read_csv(csv_file)
print(df.head(3))

print("\nConvert 'df' to numpy object: ")

arr = df.to_numpy()
print("\nNumpy object: ", arr)
print("Type: ", type(arr))

print("Selecting only the 64 bit floating point columns for conversion")
floats_array = (
    df
    .select(
        pl.col(pl.Float64)
    )
    .to_numpy()
)

print("Result of floats_array: ", floats_array)
print("Type of floats_array: ", type(floats_array))
print()

print("Converting Numpy to a DataFrame")
data_list = floats_array.tolist()
# df = pl.DataFrame(data_list)

# print("Result: ", df)
# print("Type: ", type(df))

print()
print("Converting a Series to Numpy")
s = (
    df['Profit']
    .head()
    .to_numpy()
)
print("Result: ", s)

"""
    Why zero-copy is important?
    It remove duplicate data. Also, minimizes memory usages and speeds up workflows.
    It good for performance critical applications.

"""

arr = (
    df['Profit']
    .head()
    .to_numpy(allow_copy=False)
)

print()
print("Result with allow_copy = False: ", arr)