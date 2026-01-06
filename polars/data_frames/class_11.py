import polars as pl
csv_file = "../polars/Files/Sample_Superstore.csv"
df = pl.read_csv(csv_file)

print(df.head(3))

print(df.select("Profit").to_series().head(3))