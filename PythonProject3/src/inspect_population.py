import pandas as pd

df = pd.read_csv(
    "../data/API_SP.POP.TOTL_DS2_en_csv_v2_346039.csv",
    skiprows=4
)

print(df.head())
print(df.shape)









# import pandas as pd
#
# df = pd.read_csv(
#     "data/API_SP.POP.TOTL_DS2_en_csv_v2_346039.csv",
#     skiprows=4
# )
#
# print(df.head())
# print(df.columns.tolist())
# print(df.shape)



