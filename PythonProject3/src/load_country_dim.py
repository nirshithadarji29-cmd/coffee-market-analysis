import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://neondb_owner:npg_m6BzOKYuklo5@ep-long-fire-aoze56xh-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

df = pd.read_csv("../data/country_dim_clean.csv")

df.to_sql(
    "dim_country",
    engine,
    if_exists="replace",
    index=False
)

print("dim_country loaded successfully")