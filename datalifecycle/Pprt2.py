import pandas as pd

metadata_file = "management/SpreadSheetsStructure.csv"
metadata = pd.read_csv(metadata_file, encoding="utf-8-sig")

df_csv_prt_append = pd.DataFrame()

for index, row in metadata.iterrows():
    print(row["año"])
    n_prt = "results/stage3/{}_releases.csv".format(row["año"])
    df_prt = pd.read_csv(n_prt, encoding="utf-8-sig")
    df_csv_prt_append = df_csv_prt_append._append(df_prt, ignore_index=True)




df_csv_prt_append.to_csv("results/stage4/releases-2004-2022.csv", header=True, index=False, encoding="utf-8-sig")