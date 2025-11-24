import pandas as pd
import geopandas as gpd
from shapely.geometry import Point


dataset_file = "results/stage6/Dfv6_v0.csv"
facilities_data = pd.read_csv(dataset_file, encoding="utf-8-sig", dtype={"cve_ent":str, "cve_mun":str, "instate":bool},low_memory=False)

facilities_data["inmunicipality"] = False
facilities_data["cve_mun_cc"] = "000"

len_municipio = 0
len_no_municipio = 0


shapeMun = "management/municipalities_shape/mun2019gw.shp"
poly = gpd.read_file(shapeMun)

#Filter for facilities in state
facilities_subdata = facilities_data[facilities_data["instate"] == True]
facilities_records = len(facilities_subdata.index)


counter = 0

for index, row in facilities_subdata.iterrows():
    
    #obtain cve_ent and cve_mun for the current group    
    current_cve_ent = row["cve_ent"]
    current_cve_mun = row["cve_mun"]
    
    #Get municipalietes polygon for the current stage
    current_shape = poly[(poly["CVE_ENT"]==current_cve_ent) & (poly["CVE_MUN"]==current_cve_mun)]
    
    #Iterate all the facilities in the current group
    
    counter += 1
    #Coordinates in the facility
    point = Point(row['lng'],row['lat'])
    
    #Check if the facility is in the current cve_mun polygon
    r = current_shape.geometry.contains(point)
    rl = list(r)
        
    #Validate response
    if rl[0] == True:
        #The facility is in the correct municipality
        facilities_data.at[index, "inmunicipality"] = True
        cve_mun = current_shape.CVE_MUN.iloc[0]
        facilities_data.at[index, "cve_mun_cc"] = cve_mun
        len_municipio += 1 
        print(f"{counter} {row['lat']}\t{row['lng']} {len_municipio}\tSI")
        
    else:
        #Get municipalietes polygon for the current stage
        print(f"{counter} {row['lat']}\t{row['lng']} {len_no_municipio}\tNO")
        
        
        len_no_municipio += 1
        current_state_shape = poly[(poly["CVE_ENT"]==current_cve_ent)]
        
        for pol_ind, muns in current_state_shape.iterrows():
            r2 = muns.geometry.contains(point)
            rl2 = list(r)
            
            if rl2[0]:
                
                cve_mun = muns.CVE_MUN.iloc[0]
                
                facilities_data.at[index, "cve_mun_cc"] = cve_mun
                
            

    
print("RESUMEN:")
print("\tFacilities records in the RETC:" + str(facilities_records))
print("\t\tRecords in Municipality " + str(len_municipio)  + "/" + str(facilities_records))
print("\t\tRecords outside Municipality " + str(len_no_municipio)  + "/" + str(facilities_records))

facilities_data.to_csv("results/stage6/Dfv6_v1.csv", encoding="utf-8-sig", index=False)
