from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://neondb_owner:npg_m6BzOKYuklo5@ep-long-fire-aoze56xh-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))

        for row in result:
            print(row)

    print("Connected Successfully!")

except Exception as e:
    print("Connection Failed")
    print(e)


# import pandas as pd
#
# df = pd.read_csv("../data/countries-codes.csv")
#
# print(df.columns.tolist())
# print(df.head())
# print(df.shape)
