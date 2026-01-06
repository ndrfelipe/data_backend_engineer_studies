import polars as pl

parquet_file = "../polars/Files/Crime_Data_from_2020_to_Present.parquet"

print("Reading Parquet Files")
parquet_df = pl.read_parquet(parquet_file)

print("Result: ", parquet_df.head(5))
print("Type: ", type(parquet_df))
print("Columns:", parquet_df.columns)
print()
print("Column: ", parquet_df['Weapon Used Cd'])
print("Column: ", parquet_df[['Weapon Used Cd']].dtypes)

print()
print('Using Lazy loading')

df_lazy = pl.scan_parquet(parquet_file).select(["DR_NO",
                                                 "AREA NAME",
                                                 "Vict Age",
                                                 "Vict Sex", 
                                                 "Vict Descent", 
                                                 "Weapon Desc", 
                                                 "Status"])

df_lazy = df_lazy.collect()
print(df_lazy)
