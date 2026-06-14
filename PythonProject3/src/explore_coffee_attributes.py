import pandas as pd

df = pd.read_csv("../data/psd_coffee.csv")

print(
    sorted(df["Attribute_Description"].unique())
)