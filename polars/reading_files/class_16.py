# Write files using polars

import polars as pl

people_data = {
    "Name": ["Alice Johnson", "Bob Smith", "Charlie Davis", "Diana Prince"],
    "Age": [28, 34, 25, 30],
    "Profession": ["Software Engineer", "Data Analyst", "Graphic Designer", "Project Manager"]
}

df = pl.DataFrame(people_data)
print("Data frame: ", df)

print("CSV file")
df.write_csv("output.csv")

print("JSON File")
df.write_json("output.json")

print("Parquet file")
df.write_parquet("output.parquet")