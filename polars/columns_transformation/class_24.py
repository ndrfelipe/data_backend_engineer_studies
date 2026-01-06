import polars as pl
csv_file = file = "../polars/Files/Sample_Superstore.csv"

df = pl.read_csv(csv_file)
print((df.head(3)))

Profits = [Profit for Profit in df['Profit']]
print(Profits[:3])

print()
Customer_Profit = [(row["Customer_Name"], row["Profit"]) for row in df.rows(named=True)]
print(Customer_Profit[:3])
print()
Customer_Profit = [(row["Customer_Name"], row["Profit"]) for row in df.iter_rows(named=True)]
print(Customer_Profit[:3])

new_sales = df.select([pl.col("Sales"), pl.col("Sales").round(0).alias("new_sales")])
print(new_sales.head(3))