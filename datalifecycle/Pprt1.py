import pandas as pd
from unidecode import unidecode

metadata_file = "management/SpreadSheetsStructure.csv"
metadata = pd.read_csv(metadata_file, encoding="utf-8-sig")

def prepare_f1():
    years = [2004, 2005]
    print("Preprocessig for the format  1")
    for year in years:
        n_releases = "results/stage2/{}_releases.csv".format(year)
        releases = pd.read_csv(n_releases, encoding="utf-8-sig")
        print("\tRename the headers")

        releases = releases.rename(columns={
            "no.cas":"cas", 
            "descripcion":"sustancia", 
            "reuso":"reutilizacion"
        })

        print("\tIncluding the year field")
        releases.loc[:,"año"] = year
        print("\tIncorporating the missing fields: scian, descripcionscian, subsector y claveambiental")
        releases.loc[:, "gruposustancia"] = "*"
        releases.loc[:, "municipio"] = "*"
        releases = releases[[
            "año",
            "cas",
            "sustancia",
            "gruposustancia",
            "nra",
            "nombre",
            "sector",
            "estado",
            "municipio",
            "unidad",
            "aire",
            "agua",
            "suelo",
            "alcantarillado",
            "coprocesamiento",
            "disposicionfinal",
            "incineracion",
            "reciclado",
            "reutilizacion",
            "tratamiento",
            "otros"]]
        #base = releases.columns

        releases_out = "results/stage3/{}_releases.csv".format(year)
        print(f"almacenando los resultados en {releases_out}")
        releases.to_csv(releases_out, index=False, encoding="utf-8-sig")

def prepare_f2():
    years = [2012]
    print("Preprocessig for the format  2")
    for year in years:
        n_releases = "results/stage2/{}_releases.csv".format(year)
        releases = pd.read_csv(n_releases, encoding="utf-8-sig")
        print("\tRename the headers")
        releases = releases.rename(columns={
            "establecimiento":"nombre", 
            "entidadfederativa":"estado", 
            "otro":"otros"
        })
        print("\tIncluding the year field")
        releases.loc[:,"año"] = year
        releases = releases[[
            "año",
            "cas",
            "sustancia",
            "gruposustancia",
            "nra",
            "nombre",
            "sector",
            "estado",
            "municipio",
            "unidad",
            "aire",
            "agua",
            "suelo",
            "alcantarillado",
            "coprocesamiento",
            "disposicionfinal",
            "incineracion",
            "reciclado",
            "reutilizacion",
            "tratamiento",
            "otros"]]
        releases.to_csv("results/stage3/{}_releases.csv".format(year), index=False, encoding="utf-8-sig")



def prepare_f3():
    years = [
        2006, 2007, 2008, 2009, 2010, 2011, 2013, 2014, 2015, 2016,
        2017, 2018, 2019, 2020, 2021, 2022
    ]

    print("Preprocessig for the format  3")
    for year in years:
        n_releases = "results/stage2/{}_releases.csv".format(year)
        releases = pd.read_csv(n_releases, encoding="utf-8-sig")
        print("\tRename the headers")
        releases = releases.rename(columns={
            "no.cas":"cas", 
            "descripcion":"sustancia", 
            "reuso":"reutilizacion"
        })

        print("\tIncluding the year field")
        releases.loc[:,"año"] = year
        print("\tAñadiento la columna faltante: gruposustancia")
        releases.loc[:, "gruposustancia"] = "*"
        releases = releases[[
            "año",
            "cas",
            "sustancia",
            "gruposustancia",
            "nra",
            "nombre",
            "sector",
            "estado",
            "municipio",
            "unidad",
            "aire",
            "agua",
            "suelo",
            "alcantarillado",
            "coprocesamiento",
            "disposicionfinal",
            "incineracion",
            "reciclado",
            "reutilizacion",
            "tratamiento",
            "otros"]]
        releases.to_csv("results/stage3/{}_releases.csv".format(year), index=False, encoding="utf-8-sig")


prepare_f1()
prepare_f2()
prepare_f3()