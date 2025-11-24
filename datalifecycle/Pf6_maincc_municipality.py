import pandas as pd

#We read the dataset with facilities already located in municipalities
dataset_file = "results/stage6/Dfv6_v1.csv"
facilities_data = pd.read_csv(dataset_file, encoding="utf-8-sig", dtype={"cve_ent":str, "cve_mun":str, "cve_ent_cc":str, "cve_mun_cc":str, "instate":bool, "inmunicipality":bool},low_memory=False)

#We read the default coordinates file created for the research team
mun_file = "management/Default_municipalities_DD_v1.csv"
mun_data = pd.read_csv(mun_file, encoding="utf-8-sig", dtype={"cve_ent":str, "cve_mun":str},low_memory=False)

#We create two new columns for the final lats
facilities_data["finallat"] = [round(finallat, 4) for finallat in facilities_data["lat"]]
facilities_data["finallng"] = [round(finallng, 4) for finallng in facilities_data["lng"]]

#We filtered for data with inconsistencies in their location
for_correction = facilities_data[facilities_data["inmunicipality"] == False]

#We iterate the dataset
for index, row in for_correction.iterrows():
    #We update for the default coordinates for facilities outside mexico, state or municilality
    
    print(f"{index}")
        
    fdata = mun_data[(mun_data["cve_ent"] == row["cve_ent"]) & (mun_data["cve_mun"] == str(row["cve_mun"]).zfill(3))]
    
    if len(fdata.index) > 0:
        facilities_data.at[index, "finallat"] = round(fdata["lat"].iloc[0],4)
        facilities_data.at[index, "finallng"] = round(fdata["lng"].iloc[0],4)
    else:
        print(f"NOT Found: {row['cve_ent']} {row['estado']} {row['cve_mun']} {row["municipio"]}")
            
facilities_data.to_csv("results/stage6/Dfv6_v2.csv", encoding="utf-8-sig", index=False)
