pip install splink
import splink.comparison_library as cl
from splink.duckdb.duckdb_linker import DuckDBLinker

import pandas as pd
from splink import DuckDBAPI, Linker

# Load your local file
# If the CSV is in the same folder as your script, just use the name:
df = pd.read_csv("PATY-Batismos-csv.csv")

# Clean up any columns if needed (similar to what you did before)
# df = df.drop(columns=["some_column"]) 

print("--- Your Data Preview ---")
print(df.head(5))