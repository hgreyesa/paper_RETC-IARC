import pandas as pd
from unidecode import unidecode

metadata_file = "management/SpreadSheetsStructure.csv"
metadata = pd.read_csv(metadata_file, encoding="utf-8-sig")

f_2012 = 2012


def prepare_f1():
    years = [2004, 2005]
    print("Preprocessing stage for format  1")
    for year in years:
        n_facilities = "results/stage2/{}_facilities.csv".format(year)
        facilities = pd.read_csv(n_facilities, encoding="utf-8-sig")
        print("\tRename the headers")

        facilities = facilities.rename(columns={
            "parqueopuertoindustrial":"parqueindustrial",
            "delegacion\municipio":"municipio",
            "no.exterior":"numeroexterior",
            "no.interior":"numerointerior",
        })

        print("\tIncorpotating the year field")
        facilities.loc[:,"año"] = year
        print("\tIncorporating the missing fields: scian, descripcionscian, subsector y claveambiental")
        facilities.loc[:, "scian"] = "*"
        facilities.loc[:, "descripcionscian"] = "*"
        facilities.loc[:, "subsector"] = "*"
        facilities.loc[:, "claveambiental"] = "*"
        facilities = facilities[[
                    "año",
                    "nra",
                    "nombre",
                    "sector",
                    "subsector",
                    "scian",
                    "descripcionscian",
                    "claveambiental",
                    "actividadprincipal",
                    "actividadprincipalsemarnat",
                    "estado",
                    "municipio",
                    "parqueindustrial",
                    "localidad",
                    "colonia",
                    "codigopostal",
                    "calle",
                    "numeroexterior",
                    "numerointerior",
                    "entrecalle1",
                    "entrecalle2",
                    "latitudnorte",
                    "longitudoeste",
                    "coordenadautmx",
                    "coordenadautmy"]]

        facilities_out = "results/stage3/{}_facilities.csv".format(year)
        print(f"almacenando los resultados en {facilities_out}")
        facilities.to_csv(facilities_out, index=False, encoding="utf-8-sig")

def prepare_f2():
    years = [2012]
    print("Preprocessing stage for format  2")
    for year in years:
        n_facilities = "results/stage2/{}_facilities.csv".format(year)
        facilities = pd.read_csv(n_facilities, encoding="utf-8-sig")
        print("\tRename the headers")
        facilities = facilities.rename(columns={
            "establecimiento":"nombre", 
            "entidadfederativa":"estado", 
            "scian":"descripcionscian", 
            "numeroscian":"scian",
            "nombreparqueindustrial":"parqueindustrial"
        })
        print("\tIncorpotating the year field")
        facilities.loc[:,"año"] = year
        print("\tIncorporating the missing fields: coordenadautmx, coordenadautmy, actividadprincipalsemarnat, subsector")

        facilities.loc[:,"coordenadautmx"] = "*"
        facilities.loc[:,"coordenadautmy"] = "*"
        facilities.loc[:,"actividadprincipalsemarnat"] = "*"
        facilities.loc[:,"subsector"] = "*"
        facilities = facilities[[
                    "año",
                    "nra",
                    "nombre",
                    "sector",
                    "subsector",
                    "scian",
                    "descripcionscian",
                    "claveambiental",
                    "actividadprincipal",
                    "actividadprincipalsemarnat",
                    "estado",
                    "municipio",
                    "parqueindustrial",
                    "localidad",
                    "colonia",
                    "codigopostal",
                    "calle",
                    "numeroexterior",
                    "numerointerior",
                    "entrecalle1",
                    "entrecalle2",
                    "latitudnorte",
                    "longitudoeste",
                    "coordenadautmx",
                    "coordenadautmy"]]

        facilities.to_csv("results/stage3/{}_facilities.csv".format(year), index=False, encoding="utf-8-sig")



def prepare_f3():
    years = [
        2006, 2007, 2008, 2009, 2010, 2011, 2013, 2014, 2015, 2016,
        2017, 2018, 2019, 2020, 2021, 2022
    ]

    print("Preprocessing stage for format  3")
    for year in years:
        n_facilities = "results/stage2/{}_facilities.csv".format(year)
        facilities = pd.read_csv(n_facilities, encoding="utf-8-sig")
        print("\tRename the headers")
        facilities = facilities.rename(columns={
            "principalactividadproductiva":"actividadprincipal", 
            "c.p.":"codigopostal",
            "num.ext":"numeroexterior", 
            "num.int":"numerointerior"
        })

        print("\tIncorpotating the year field")
        facilities.loc[:,"año"] = year
        print("\tIncorporating the missing fields: actividadprincipalsemarnat, entrecalle1 y entrecalle2")
        facilities.loc[:, "actividadprincipalsemarnat"] = "*"
        facilities.loc[:, "entrecalle1"] = "*"
        facilities.loc[:, "entrecalle2"] = "*"
        facilities = facilities[[
                    "año",
                    "nra",
                    "nombre",
                    "sector",
                    "subsector",
                    "scian",
                    "descripcionscian",
                    "claveambiental",
                    "actividadprincipal",
                    "actividadprincipalsemarnat",
                    "estado",
                    "municipio",
                    "parqueindustrial",
                    "localidad",
                    "colonia",
                    "codigopostal",
                    "calle",
                    "numeroexterior",
                    "numerointerior",
                    "entrecalle1",
                    "entrecalle2",
                    "latitudnorte",
                    "longitudoeste",
                    "coordenadautmx",
                    "coordenadautmy"]]
        facilities.to_csv("results/stage3/{}_facilities.csv".format(year), index=False, encoding="utf-8-sig")


prepare_f1()
prepare_f2()
prepare_f3()