import pandas as pd

df = pd.read_csv(
    "../data/countries-codes.csv",
    sep=";",
    usecols=[
        "ISO2 CODE",
        "ISO3 CODE",
        "LABEL EN"
    ]
)

df.columns = [
    "iso2_code",
    "iso3_code",
    "country_name"
]

df = df.drop_duplicates()

print(df.head())
print(df.shape)

df.to_csv(
    "../data/country_dim_clean.csv",
    index=False
)

print("country_dim_clean.csv created")