import polars as pl

file = "../polars/Files/Sample_Superstore.csv"
df = pl.read_csv(file)

print("Select using numeric indexing: ")
print(df[:, 1:6].head(3))

print("Round method: ")
print(df.select(pl.col("Profit").round(0)).head(5))

