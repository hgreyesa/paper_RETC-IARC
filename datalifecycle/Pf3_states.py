import pandas as pd


def get_state_name():
    print("Get states names")
    dataset_file = "results/stage4/facilities-2004-2022.csv"
    facilities_data = pd.read_csv(dataset_file, encoding="utf-8-sig", low_memory=False)
    facilities_data = facilities_data.sort_values(by=["estado"], ascending=True)
    states_list = list(facilities_data["estado"].unique())
    df_states = pd.DataFrame(columns=["dataset_state", "cve_ent", "state"])
    
    for state in states_list:
        df_states.loc[len(df_states.index)] = {
            "dataset_state": state,
            "cve_ent": "",
            "state": ""
        }
        
    df_states.to_csv("results/stage5/states_list.csv", encoding="utf-8-sig", index=False)

#Get unique names (automatic)
get_state_name()

# updated the inconsistencies (manually)
dataset_file = "results/stage5/facilities-2004-2022.csv"
facilities_data = pd.read_csv(dataset_file, encoding="utf-8-sig", low_memory=False)

#Read and apply the changes in the states list detected for the research team
states_file = "management/states_list.csv"
states_list = pd.read_csv(states_file, encoding="utf-8-sig", dtype={"cve_ent":str},low_memory=False)


for index, row in states_list.iterrows():
    print(f"\t{row["state"]}")
    
    if row["dataset_state"] != row["state"]:
        print(f"Update '{row["dataset_state"]}' to '{row['state']}'")
        facilities_data.loc[facilities_data["estado"] == row["dataset_state"],"estado"] = row["state"]

    facilities_data.loc[facilities_data["estado"] == row["state"],"cve_ent"] = row["cve_ent"]
    
  
facilities_data.to_csv("results/stage5/facilities-2004-2022_v1.csv", encoding="utf-8-sig", index=False)

