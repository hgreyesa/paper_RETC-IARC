import pandas as pd
from unidecode import unidecode

metadata_file = "management/SpreadSheetsStructure.csv"
metadata = pd.read_csv(metadata_file, encoding="utf-8-sig")

inputPath = 'datasource/'

for index, row in metadata.iterrows():
    n_prt = "results/stage1/{}_releases.csv".format(row["año"])
    print(f"Reading PRT {n_prt}")
    df_prtr = pd.read_csv(n_prt, encoding="utf-8-sig")
    cols = df_prtr.columns
    print(f"\tPreparing headers")

    for col in cols:
        print("\t\tRemoving black spaces")
        newcol = col.replace(" ", "")    
        print("\t\tRemoving accents")
        newcol = unidecode(newcol)
        print("\t\tTransform to lower case")
        newcol = newcol.lower()
        print("\tUpdated header name")

        df_prtr=df_prtr.rename(columns={
            col:newcol
        })

    n_prt_out = "results/stage2/{}_releases.csv".format(row["año"])
    print(f"Save the PRT data {n_prt_out}")
    print("#############################################################")
    
    df_prtr.to_csv(n_prt_out, index=False, encoding="utf-8-sig")


    n_facilities = "results/stage1/{}_facilities.csv".format(row["año"])
    print(f"Reading facilities {n_facilities}")

    df_facilities = pd.read_csv(n_facilities, encoding="utf-8-sig")
    cols = df_facilities.columns
    print(f"\tPreparing headers")

    for col in cols:
        print("\t\tRemoving black spaces")
        newcol = col.replace(" ", "")    
        print("\t\tRemoving accents")
        newcol = unidecode(newcol)
        print("\t\tTransform to lower case")
        newcol = newcol.lower()
        print("\tUpdated header name")

        df_facilities=df_facilities.rename(columns={
            col:newcol
        })


    n_facilities_out = "results/stage2/{}_facilities.csv".format(row["año"])
    print(f"Save the Facilities data {n_facilities_out}")
    print("#############################################################")
    
    df_facilities.to_csv(n_facilities_out, index=False, encoding="utf-8-sig")

