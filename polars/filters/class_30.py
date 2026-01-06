import polars as pl

df = pl.read_csv("../polars/Files/Sample_Superstore.csv")

# String Columns
df_select_columns = df.select(pl.col("Customer_Name", "Segment")).head(3)
print(df_select_columns)

df_equal = df.filter(
    pl.col("City") == "Henderson"
).select(["Customer_Name", "City", "Profit"])

print(df_equal.head)

# Apply IN condition
df_in = df.filter(
    pl.col("City").is_in(["Henderson", "Los Angeles", "Denver"])
).select(["Row_ID", "City", "Profit"])

print(df_in)

# Apply contain

df_contain = df.filter(
    pl.col("Customer_Name").str.contains("Gene Hale")
).select(["Row_ID", "Customer_Name", "Profit"])

print(df_contain)

# AND/OR
df_and = df.filter(
    (pl.col('Customer_Name') == 'Gene Hale') & (pl.col('Segment') == 'Corporate')
).select('Row_ID', 'Customer_Name', 'Segment', 'Profit')

print(df_and)