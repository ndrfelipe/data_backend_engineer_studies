"""
Select multiple columns
"""
import polars as pl
import polars.selectors as cs

file = "../polars/Files/Sample_Superstore.csv"
df = pl.read_csv(file)

print(df)

print("Select all the columns: ")
print(df.select(pl.all().head(3)))

print("Removing columns: ")
print(df.select(pl.exclude('Order_Date', 'Quantity').head(3)))

print("Using regex: ")
print(df.select("^P.*$").head(3))

print("Selecting colors by the data type: ")
print(df.select(pl.col(pl.Utf8)).head(5))

print("Selecting colors by the data type (int and float): ")
print(df.select(pl.col([pl.Int64, pl.Float64])).head(5))