import pandas as pd

# Load file
df = pd.read_csv(
    "../data/API_SP.POP.TOTL_DS2_en_csv_v2_346039.csv",
    skiprows=4
)

# Keep only required columns
id_cols = ["Country Name", "Country Code"]

year_cols = [col for col in df.columns if str(col).isdigit()]

# Convert wide → long
population_long = df.melt(
    id_vars=id_cols,
    value_vars=year_cols,
    var_name="year",
    value_name="population"
)

# Rename columns
population_long = population_long.rename(columns={
    "Country Name": "country_name",
    "Country Code": "country_code"
})

# Remove empty populations
population_long = population_long.dropna(subset=["population"])

print(population_long.head())
print(population_long.shape)

# Save output
population_long.to_csv(
    "../data/population_clean.csv",
    index=False
)

print("Saved successfully!")