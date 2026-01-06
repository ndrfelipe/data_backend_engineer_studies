"""
Docstring for polars.distinct.class_27

"""

import polars as pl

csv_file = file = "../polars/Files/Sample_Superstore.csv"
df = pl.read_csv(csv_file)

print(df.unique(subset=["Customer_Name"]).select(["Customer_Name"]))

print(df.select(pl.col("Customer_Name").unique()))

print("Select distinct two columns: ")
print(df.unique(subset=['Customer_Name', 'Profit']).select(['Customer_Name', 'Profit']))