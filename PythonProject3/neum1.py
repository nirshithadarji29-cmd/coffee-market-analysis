# import pandas as pd
#
# file_path = r"data/countries-codes.csv"
#
# with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
#     print("HEADER:")
#     print(f.readline())
#
#     print("\nFIRST DATA ROW:")
#     print(f.readline())


import csv

with open("data/countries-codes.csv", "r", encoding="utf-8", errors="ignore") as f:
    reader = csv.reader(f, delimiter=';')

    for i, row in enumerate(reader):
        print(f"Row {i}:")
        print(row[:15])  # only first 15 columns
        print(f"Number of columns: {len(row)}")
        break