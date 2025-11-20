import pandas as pd


dataset_file = "results/stage5/facilities-2004-2022_v2.csv"
facilities_data = pd.read_csv(dataset_file, encoding="utf-8-sig", dtype={"cve_ent":str, "cve_mun":str},low_memory=False)


facilities_data["lat"] = 0.0
facilities_data["lng"] = 0.0
facilities_data["dmsformat"] = False
facilities_data["dmsdefault"] = False


computedDD = 0
ddformat = 0
withdefaultvalue = 0

#Iterate all the records
for index, row in facilities_data.iterrows():
    
    newlat = 0.0
    newlon = 0.0
    
    print("\t\tOriginal: " + str(index) + "\tlat:\t" + str(row['latitudnorte']) + "\tlng:\t"+ str(row['longitudoeste']))
    
    try:
        lat = float(row['latitudnorte'])
        lng = float(row['longitudoeste'])
        ddformat += 1

        facilities_data.loc[index,'lat'] = lat
        facilities_data.loc[index,'lng'] = lng
        print("\t\t\tAlready in DD format")
    
    except ValueError:
        print("\t\tRemove the blanck spaces")
        lat = str(row['latitudnorte']).replace(" ", "")
        lng = str(row['longitudoeste']).replace(" ", "")
        
        print("\t\tDetect all default values")
        if "0°0'0\"" in lat or "0°0'0\"" in lng or "°0'0\"" in lat or "°0'0\"" in lng or "º0'0\"" in lat or "º0'0\"" in lng or "°'\"" in lat or "°'\"" in lng:
            row['lat'] = 0
            row['lng'] = 0
            row['dmsformat'] = True
            row['dmsdefault'] = True
            
            facilities_data.loc[index,'dmsformat']= True
            facilities_data.loc[index,'dmsdefault']= True
            withdefaultvalue += 1

            print("\t\t\tIt is a default value")

        
        else:
            print("\t\tApply transformation")

            if "°" in lat or "°" in lng:
                print("\t\tDetecting special characters")

                print("\t\t\tReaplace spetial characters A")
                lat = lat.replace("°", " ")
                lat = lat.replace("'", " ")
                lat = lat.replace("\"", " ")
                lng = lng.replace("°", " ")
                lng = lng.replace("'", " ")
                lng = lng.replace("\"", " ")
                arr1 = lat.split(" ")
                arr2 = lng.split(" ")

                facilities_data.loc[index,'dmsformat'] = True
                computedDD += 1

                if (arr2[0].startswith('0.')):
                    arr2[0] = float(arr2[0])*100
                else:
                    arr2[0] = float(arr2[0])
                
                if (arr1[0].startswith('0.')):
                    arr1[0] = float(arr1[0])*100
                else: 
                    arr1[0] = float(arr1[0])

                
                if(float(arr2[0])>0 and float(arr1[0]) > 0):
                    newlat = 1 * ( int (arr1[0]) + float(arr1[1])/60 + float(arr1[2])/3600)
                    newlon = -1 * ( int(arr2[0]) + float(arr2[1])/60 + float(arr2[2])/3600)
                else:
                    newlat = 1 * ( int (arr1[0]) + float(arr1[1])/60 + float(arr1[2])/3600)
                    newlon = -1 * ( int(arr2[0]) + float(arr2[1])/60 + float(arr2[2])/3600)
                    newlon = newlon * -1
                
                
                facilities_data.loc[index,'lat'] = newlat
                facilities_data.loc[index,'lng'] = newlon

                
                print("\t\t\t\tComputed values: " + "\tlat:\t" + str(row['lat']) + "\tlng:\t"+ str(row['lng']))

            else: 
                
                if "º" in lat or "º" in lng:

                    print("\t\t\tReaplace spetial characters B")
                    
                    print("Detected inconsistencies for specific errors")
                    if row["latitudnorte"] == "25º 42 46.97\"" and row["longitudoeste"] == "100º 20 7.29\"":
                        lat = "25 42 46"
                        lng = "100 20 7"
                    if row["latitudnorte"] == "25º52'18.88\"" and row["longitudoeste"] == "100º'13'39.1\"":
                        lat = "25 52 18"
                        lng = "100 13 39"
                    if row["latitudnorte"] == "25ª42'46.97\"" and row["longitudoeste"] == "100º20'07.29\"":
                        lat = "25 42 46"
                        lng = "100 20 7"
                    if row["latitudnorte"] == "25º 42 46.97\" " and row["longitudoeste"] == "100º 20 7.29\" ":
                        lat = "25 42 46"
                        lng = "100 20 7"
                    
                    lat = lat.replace("º", " ")
                    lat = lat.replace("'", " ")
                    lat = lat.replace("\"", " ")
                    lng = lng.replace("º", " ")
                    lng = lng.replace("'", " ")
                    lng = lng.replace("\"", " ")
                    arr1 = lat.split(" ")
                    arr2 = lng.split(" ")
                    row['dmsformat'] = True

                    facilities_data.loc[index,'dmsformat'] = True
                    computedDD += 1
                    
                    

                    if (arr2[0].startswith('0.')):
                        arr2[0] = float(arr2[0])*100
                    else:
                        arr2[0] = float(arr2[0])
                    
                    if (arr1[0].startswith('0.')):
                        arr1[0] = float(arr1[0])*100
                    else: 
                        arr1[0] = float(arr1[0])


                    
                    if(float(arr2[0])>0 and float(arr1[0]) > 0):
                        newlat = 1 * ( int (arr1[0]) + float(arr1[1])/60 + float(arr1[2])/3600)
                        newlon = -1 * ( int(arr2[0]) + float(arr2[1])/60 + float(arr2[2])/3600)
                    else:
                        newlat = 1 * ( int (arr1[0]) + float(arr1[1])/60 + float(arr1[2])/3600)
                        newlon = -1 * ( int(arr2[0]) + float(arr2[1])/60 + float(arr2[2])/3600)
                        newlon = newlon * -1


                    facilities_data.loc[index,'lat'] = newlat
                    facilities_data.loc[index,'lng'] = newlon


print("RESUME:")
total_rows = len(facilities_data.index)
print(f"\tFacilities: {total_rows}" )
print(f"\tWith DD fotmat: {ddformat}/{total_rows}")
print(f"\tComputed: {computedDD}/{total_rows}")
print(f"\tWith default value: {withdefaultvalue}/{total_rows}")
#print("\tmapa:" + str(mapa) +"/"+ str(contador))
mitotal = ddformat + computedDD + withdefaultvalue
print("\ttotal:" + str(mitotal) +"/"+ str(total_rows))

facilities_data.to_csv("results/stage6/Dfv5.csv", encoding="utf-8-sig", index=False)
