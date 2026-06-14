# import pandas as pd
#
# df = pd.read_csv("../data/countries-codes.csv")
#
# print("Columns:")
# print(df.columns.tolist())
#
# print("\nShape:")
# print(df.shape)
#
# print("\nSample:")
# print(df.head())

file_path = "../data/countries-codes.csv"

with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    for i in range(5):
        print(f.readline())