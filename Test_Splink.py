
import pandas as pd
from splink import block_on
from splink import DuckDBAPI, Linker

# Load your local file
# If the CSV is in the same folder as your script, just use the name:
df = pd.read_csv("/Users/amand/Desktop/python/Splink/PATY-Batismos-csv.csv")

# Clean up any columns if needed (similar to what you did before)
# df = df.drop(columns=["some_column"]) 

print(df.head(5))
from splink.blocking_analysis import count_comparisons_from_blocking_rule

db_api = DuckDBAPI()

br = block_on("Mãe", "senhor_mãe")

counts = count_comparisons_from_blocking_rule(
    table_or_tables=df,
    blocking_rule=br,
    link_type="dedupe_only",
    db_api=db_api,
)

print(counts)

