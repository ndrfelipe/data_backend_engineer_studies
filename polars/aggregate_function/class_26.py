"""
Aggregate Function Class 26
- aggregate on dataframe
- aggregate on expression 
"""


import polars as pl
csv_file = file = "../polars/Files/Sample_Superstore.csv"

df = pl.read_csv(csv_file)

# mean function
print(df.mean())

# max
print(df.max())

# min
print(df.min())

# count
print(df.count())

# sum
print(df.sum())

# aggregate on expression
agg_df = df.select(
    pl.col('Profit').mean().alias('avg_profit'),
    pl.col('Sales').sum().alias('total_sales'),
    pl.col('Quantity').max().alias('max_quantity'),
    pl.col('Discount').min().alias('min_discount'),
    pl.col('Order_ID').count().alias('order_count'),
)

print(agg_df)
