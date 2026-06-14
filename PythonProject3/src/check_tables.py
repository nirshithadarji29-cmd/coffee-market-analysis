from sqlalchemy import create_engine
import pandas as pd

DATABASE_URL = "postgresql://neondb_owner:npg_m6BzOKYuklo5@ep-long-fire-aoze56xh-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

query = """
SELECT table_name
FROM information_schema.tables
WHERE table_schema='public';
"""

print(pd.read_sql(query, engine))