import polars as pl

df = pl.read_csv("../polars/Files/Sample_Superstore.csv")

# Filtering rows
df = df.filter(pl.col("Profit") > 1000)

print(df.head(3))

# AND/OR conditions
# df = df.filter(
#     (pl.col("Quantity") == 5) | (pl.col('Profit') >= 500)
# ).select(["Row_ID","Profit","Sales", "Quantity"])

# print(df)

# BETWEEN

df = df.filter(
    pl.col('Profit').is_between(1000, 2000)
).select("Customer_Name", "Profit")

print(df.head(3))