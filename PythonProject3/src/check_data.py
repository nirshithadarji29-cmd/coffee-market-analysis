# src/check_data.py

import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://neondb_owner:npg_m6BzOKYuklo5@ep-long-fire-aoze56xh-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

for table in ["fact_coffee", "fact_population"]:
    print(f"\n=== {table} ===")
    df = pd.read_sql(
        f"SELECT * FROM {table} LIMIT 5",
        engine
    )
    print(df)