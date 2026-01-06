"""
Python way to filter a DataFrame

"""

import polars as pl
csv_file = file = "../polars/Files/Sample_Superstore.csv"
df = pl.read_csv(csv_file)

# Filter rows where 'Profit' > 500
filtered_df = df.filter(df['Profit'] > 500)

print(filtered_df[:3])

print(df[range(2,8)])

import numpy as np
df[np.arange(0, 3)]
print(df[np.arange(0, 3)])