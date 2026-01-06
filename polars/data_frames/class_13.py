"""
Numerical dtypes and precision. 

Dtypes are efficient handling of numerical data types to optimize performance and memory usage.

- Use .cast() to change numerical types.


"""

print("Checking numerical data types in Polars: ")
 
import polars as pl
 
df = pl.DataFrame({
    "integer_column": [1, 2, 3, 4, 5],  # Default: Int64
    "float_column": [1.1, 2.2, 3.3, 4.4, 5.5]  # Default: Float64
})
 
print("DataFrame:")
print(df)
 
print("\nData Types:")
print(df.schema)

print()
print("Changing numerical Data Types: ")

df = df.with_columns([
    df["integer_column"].cast(pl.Int32),
    df["float_column"].cast(pl.Float32)
])
 
print("\nUpdated Data Types:")
print(df.schema)

print()

df_large = pl.DataFrame({
    "big_number": [10**12, 10**13, 10**14]  # Large integers
}).with_columns(pl.col("big_number").cast(pl.Int64))
 
print("\nLarge Number Data Types:")
print(df_large.schema)