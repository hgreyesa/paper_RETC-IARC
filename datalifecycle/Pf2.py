import pandas as pd

metadata_file = "management/SpreadSheetsStructure.csv"
metadata = pd.read_csv(metadata_file, encoding="utf-8-sig")

df_csv_fac_append = pd.DataFrame()

for index, row in metadata.iterrows():
    print(row["año"])
    n_facilities = "results/stage3/{}_facilities.csv".format(row["año"])
    df_facilities = pd.read_csv(n_facilities, encoding="utf-8-sig")
    df_csv_fac_append = df_csv_fac_append._append(df_facilities, ignore_index=True)


df_csv_fac_append.to_csv("results/stage4/facilities-2004-2022.csv", header=True, index=False, encoding="utf-8-sig")