import pandas as pd

# Load coffee data
df = pd.read_csv("../data/psd_coffee.csv")

# Keep only metrics we need
required_metrics = [
    "Production",
    "Domestic Consumption",
    "Imports",
    "Exports",
    "Beginning Stocks",
    "Ending Stocks"
]

coffee = df[
    df["Attribute_Description"].isin(required_metrics)
].copy()

# Keep required columns
coffee = coffee[
    [
        "Country_Name",
        "Country_Code",
        "Market_Year",
        "Attribute_Description",
        "Value"
    ]
]

# Pivot
coffee_clean = coffee.pivot_table(
    index=[
        "Country_Name",
        "Country_Code",
        "Market_Year"
    ],
    columns="Attribute_Description",
    values="Value",
    aggfunc="sum"
).reset_index()

# Clean column names
coffee_clean.columns.name = None

coffee_clean.columns = [
    col.lower().replace(" ", "_")
    for col in coffee_clean.columns
]

print(coffee_clean.head())
print("\nShape:")
print(coffee_clean.shape)

# Save output
coffee_clean.to_csv(
    "../data/coffee_clean.csv",
    index=False
)

print("\nSaved coffee_clean.csv")