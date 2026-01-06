"""

"""

import polars as pl

file = "../polars/Files/Third.json"

df = pl.read_json(file)
print('Result 1: ', df)

df = df.explode('friends')
print('Result 2: ', df)

df = df.with_columns(
    pl.col('friends').struct.field('name').alias('friend_name'),
    pl.col('friends').struct.field('hobbies').alias('friend_hobbies')
)

print('Result 3: ', df)
