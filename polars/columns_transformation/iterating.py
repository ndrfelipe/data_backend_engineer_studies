import polars as pl
csv_file = file = "../polars/Files/Sample_Superstore.csv"

df = pl.read_csv(csv_file)

df_frame = pl.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [25, 30, 35, 40, 45]
})

print("Avoid Iterating - use vectorized operations.")
# Polars is optimized for vectorized operations, so iterations is usuallyy unnecessary.
# Instead of looping through rows, apply transformations directly.

df_frame = df_frame.with_columns(
    (df_frame["age"] + 5).alias("age_plus_5")
)
print(df_frame)