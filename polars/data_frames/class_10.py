"""
    Understanding lazy mode in Polars

    
    """
import polars as pl

df = pl.DataFrame({"name": ["Alice", "Bob", "Charlie"], "age": [25, 30, 35]})
lazy_df = df.lazy()
filtered_lazy_df = lazy_df.filter(pl.col("age") > 28)

result = filtered_lazy_df.collect()
print(result)

"""

Lazy mode primeiro planeja a query SQL e depois executa, isso acaba garantindo uma maior velocidade de execução, gerenciamento de memória e
um smart query optimization. 

When to use:
working with large datasets (millions or billions of rows)
running complex queries involving multiple operations
needing efficient memory usage to avoid crashes

"""