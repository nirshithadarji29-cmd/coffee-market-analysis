import pandas as pd
from sqlalchemy import create_engine

# Replace with YOUR Neon connection string
DATABASE_URL = "postgresql://neondb_owner:npg_m6BzOKYuklo5@ep-long-fire-aoze56xh-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

# Load files
coffee_df = pd.read_csv("../data/coffee_clean.csv")
population_df = pd.read_csv("../data/population_clean.csv")

# Upload tables
coffee_df.to_sql(
    "fact_coffee",
    engine,
    if_exists="replace",
    index=False
)

population_df.to_sql(
    "fact_population",
    engine,
    if_exists="replace",
    index=False
)

print("Tables loaded successfully!")