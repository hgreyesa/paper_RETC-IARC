import pandas as pd
import geopandas as gpd
from shapely.geometry import Point


dataset_file = "results/stage6/Dfv5.csv"
facilities_data = pd.read_csv(dataset_file, encoding="utf-8-sig", dtype={"cve_ent":str, "cve_mun":str},low_memory=False)

facilities_data["inmexico"] = False
facilities_data["instate"] = False
facilities_data["cve_ent_cc"] = "00"

facilities_records = len(facilities_data.index)
count_inmexico = 0
count_outmexico = 0
count_instate = 0
count_outstate = 0


shapeStates = "management/states_shape/dest2019gw.shp"
poly = gpd.read_file(shapeStates)

for index, row in facilities_data.iterrows():
    point = Point(row['lng'],row['lat'])
    for index2,row2 in poly.iterrows():
        r = row2.geometry.contains(point)
        if r:
            msj = "\t\tThe facility is located in the state '%s'" % row2.NOM_ENT
            count_inmexico += 1
            facilities_data.at[index,"inmexico"] = True
            print(msj)

            facilities_data.at[index,"cve_ent_coor"] = row2.CVE_ENT
            if row2.CVE_ENT == row["cve_ent"]:
                # print(f"\t\tOK_ENT {index} {row["nombre"]} {row["estado"]}")
                facilities_data.at[index,"instate"] = True
                count_instate += 1
                break
            else:
                #print(f"\t\tNO_ENT {index} {row["nombre"]} {row["estado"]}")
                count_outstate += 1
                break
    if facilities_data.at[index,"inmexico"] == 0:
        count_outmexico += 1
        #print(f"\tNO_MEX {index} {row["nombre"]} {row["estado"]}")

    #pass
    
print("RESUMEN:")
print("\tFacilities records in the RETC:" + str(facilities_records))
print("\t\tRecords in Mexico " + str(count_inmexico)  + "/" + str(facilities_records))
print("\t\tRecords outside Mexico " + str(count_outmexico)  + "/" + str(facilities_records))
print("\t\tRecords in the correct state: " + str(count_instate)  + "/" + str(facilities_records))
print("\t\tRecords in different states that metadata indicates: " + str(count_outstate)  + "/" + str(facilities_records))

facilities_data.to_csv("results/stage6/Dfv6_v0.csv", encoding="utf-8-sig", index=False)
