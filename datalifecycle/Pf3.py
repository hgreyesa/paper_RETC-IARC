import pandas as pd


def get_sector_name():
    print("Get sectors names")
    dataset_file = "results/stage4/facilities-2004-2022.csv"
    facilities_data = pd.read_csv(dataset_file, encoding="utf-8-sig", low_memory=False)
    facilities_data = facilities_data.sort_values(by=["sector"], ascending=True)
    sector_list = list(facilities_data["sector"].unique())
    df_sectors = pd.DataFrame(columns=["dataset_industrialsectorname", "industrialsectorname"])
    
    for sector in sector_list:
        df_sectors.loc[len(df_sectors.index)] = {
            "dataset_industrialsectorname": sector,
            "industrialsectorname": ""
        }
        
    #print(sector_list)
    df_sectors.to_csv("results/stage5/facilities-2004-2022_sectors_v0.csv", encoding="utf-8-sig", index=False)

#Get unique names (automatic)
#get_sector_name()

#Identify correct names and updated the inconsistencies (manually)
dataset_file = "results/stage4/facilities-2004-2022.csv"
facilities_data = pd.read_csv(dataset_file, encoding="utf-8-sig", low_memory=False)




#Read and apply the changes in the sectors list detected for the research team
sectors_file = "management/sectors_list.csv"
sectors_list = pd.read_csv(sectors_file, encoding="utf-8-sig", low_memory=False, sep="\t")

facilities_data["industrialsectorname"] = ""
sectors_metadatafile = "management/sectors_metadata.csv"
sectors_metadata = pd.read_csv(sectors_metadatafile, encoding="utf-8-sig", low_memory=False)

for index, row in sectors_list.iterrows():
    print(f"\t{row["industrialsectorname"]}")
    
    
    if row["requires_update"] == 1:
        
        print(f"Update '{row["dataset_industrialsectorname"]}' to '{row['industrialsectorname']}' for these inconsistencies: '{row["note"]}'")
        facilities_data.loc[facilities_data["sector"] == row["dataset_industrialsectorname"],"sector"] = row["industrialsectorname"]
        facilities_data.loc[facilities_data["sector"] == row["dataset_industrialsectorname"],"sector"] = row["industrialsectorname"]
    
    filtered_data = sectors_metadata[sectors_metadata["industrialsectorname"] == row["industrialsectorname"]]#
    current_name = filtered_data["industrialsectorname_en"].iloc[0]
    
    #Add the sector name in English
    facilities_data.loc[facilities_data["sector"] == row["industrialsectorname"], "industrialsectorname"] = current_name
    
facilities_data.to_csv("results/stage5/facilities-2004-2022.csv", encoding="utf-8-sig", index=False)

