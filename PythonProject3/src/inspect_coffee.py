import pandas as pd

df = pd.read_csv("../data/psd_coffee.csv")

print("Columns:")
print(df.columns.tolist())

print("\nShape:")
print(df.shape)

print("\nSample:")
print(df.head())