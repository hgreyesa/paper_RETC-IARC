import pandas as pd


def get_municipalities_names():
    print("Get states names")
    dataset_file = "results/stage5/facilities-2004-2022_v1.csv"
    facilities_data = pd.read_csv(dataset_file, encoding="utf-8-sig", dtype={"cve_ent":str},low_memory=False)
    #facilities_data = facilities_data.sort_values(by=["estado"], ascending=True)
    sub_data = facilities_data[["cve_ent", "estado", "municipio"]]
    
    gdata = sub_data.groupby(by=["cve_ent", "estado", "municipio"])
    df_mun = pd.DataFrame(columns=["cve_ent", "state", "cve_mun", "municipality"])
    
    for name, group in gdata:
        df_mun.loc[len(df_mun.index)] = {
            "state": group["estado"].iloc[0],
            "cve_ent": group["cve_ent"].iloc[0],
            "cve_mun": "DEFAULT",
            "municipality": group["municipio"].iloc[0],
            
        }
        
        
    df_mun.to_csv("results/stage5/municipalities_list.csv", encoding="utf-8-sig", index=False)

#Get unique names (automatic)
#get_municipalities_names()

# updated the inconsistencies (manually)
dataset_file = "results/stage5/facilities-2004-2022_v1.csv"
facilities_data = pd.read_csv(dataset_file, encoding="utf-8-sig", dtype={"cve_ent":str, "cve_mun":str}, low_memory=False)

# #Read and apply the changes in the states list detected for the research team
municipalietes_file = "management/municipalities_inconsistencies.csv"
municipalietes_list = pd.read_csv(municipalietes_file, encoding="utf-8-sig", dtype={"cve_ent":str},low_memory=False, sep="\t")
facilities_data["cve_mun"] = "NOAPLICA"

print("Solve inconsistencies")

for index, row in municipalietes_list.iterrows():
    print(f"\t{row["municipality"]}")
    facilities_data.loc[(facilities_data["municipio"] == row["dataset_municipality"]) & (facilities_data["estado"] == row["state"]),"municipio"] = row["municipality"]
    
print("Add cve_mun")
municipalietes_file = "management/cve_ent_mun_list_v1.csv"
municipalietes_list = pd.read_csv(municipalietes_file, encoding="utf-8-sig", dtype={"cve_ent":str},low_memory=False)

for index, row in municipalietes_list.iterrows():
    print(f"\t{row["state"]} {row['municipality']}")
    facilities_data.loc[(facilities_data["cve_ent"] == row["cve_ent"]) & (facilities_data["municipio"] == row["municipality"]),"cve_mun"] = row["cve_mun"]
    
    
facilities_data.to_csv("results/stage5/facilities-2004-2022_v2.csv", encoding="utf-8-sig", index=False)

