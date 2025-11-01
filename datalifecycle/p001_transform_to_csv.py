import pandas as pd

metadata_file = "management/SpreadSheetsStructure.csv"
print("Read metadata descriptor for datasets")
metadata = pd.read_csv(metadata_file, encoding="utf-8-sig")

#You must to download the dataset and uncompress in the folder "datasource/RETC_2004-2024"
inputPath = 'datasource/'
limit2023 = "{}{}".format(inputPath, "RETC_2004-2022/")

for index, row in metadata.iterrows():
    cname = f"retc {row["año"]}.xlsx"
    cpath1 = f"{limit2023}{cname}"
    print(f"Read the file {cpath1}")
    print(f"\tObtain the data {row["emisiones"]}")
    data_releases = pd.read_excel(cpath1, sheet_name=row["emisiones"], skiprows=range(row["nc_inicio"], row["nc_fin"]))
    cpath_out1 = f"results/stage1/{row["año"]}_releases.csv"
    print(f"\tSave the csv {cpath_out1}")
    data_releases.columns = data_releases.columns.str.replace('\n', ' ')
    data_releases.columns = data_releases.columns.str.replace('  ', ' ')
    print(data_releases.columns)
    data_releases.to_csv(cpath_out1, index=False, encoding="utf-8-sig")

    del data_releases
    print(f"\tRead the file {row["emisoras"]}")
    data_facilities = pd.read_excel(cpath1, sheet_name=row["emisoras"], skiprows=range(row["nc_inicio"], row["nc_fin"]))
    cpath_out2 = f"results/stage1/{row["año"]}_facilities.csv"
    print(f"\tsave the file {cpath_out1}")
    print(data_facilities.columns)
    data_facilities.columns = data_facilities.columns.str.replace('\n', ' ')
    data_facilities.columns = data_facilities.columns.str.replace('  ', ' ')
    data_facilities.to_csv(cpath_out2, index=False, encoding="utf-8-sig")
    del data_facilities

