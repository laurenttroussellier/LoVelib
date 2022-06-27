#import pandas as pd
#import holoviews as hv
#from datetime import datetime
#import csv
#hv.extension('bokeh')
#from bokeh.plotting import show
#from OSMPythonTools.api import Api
#import folium

import json

from holoviews.ipython import display
#
# data = requests.get('https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json').json()
# # dff = pd.DataFrame(columns =['Timer', 'ID', 'Station', 'Code Station', 'Type de stations', 'Etat de la station',
# #                                      'Nb bornes disponibles', 'Nombres de bornes en station', 'Nombre vélo en PARK+',
# #                                      'Nb vélo mécanique', 'Nb vélo électrique',
# #                                      'geo'])
# # print(data)
# df = pd.DataFrame.from_dict(data)
# print(df.head)
#
# # OK on a une liste de dict
# # data["data"]["stations"][:][0].keys()
# # dict_keys(['stationCode', 'station_id', 'num_bikes_available', 'numBikesAvailable', 'num_bikes_available_types', 'num_docks_available', 'numDocksAvailable', 'is_installed', 'is_returning', 'is_renting', 'last_reported'])
#
#
#import webbrowser
#from dataclasses import dataclass
#from dataclasses_json import dataclass_json

# si = requests.get("https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json").json()
#
# df=pd.DataFrame.from_dict(data["data"]["stations"])
# dff=pd.DataFrame.from_dict(si["data"]["stations"])
#
# mdf = df.merge(dff, how='inner', on='station_id')
#
#
# mdf.to_csv("data/"+str(si["lastUpdatedOther"]))
# def getinfo(i):
#
#     stationsid = data["data"]["stations"][i]["stationCode"]
#     nbMecha = data["data"]["stations"][i]["num_bikes_available_types"][0]["mechanical"]
#     nbElec = data["data"]["stations"][i]["num_bikes_available_types"][1]["ebike"]
#     nbdocklibre = data["data"]["stations"][i]["num_docks_available"]
#     last_reported = data["data"]["stations"][i]["last_reported"]
#
#     print(getstationinfo(stationsid))
#
#     print(stationsid,nbMecha,nbElec,nbdocklibre,last_reported)
# def getstationinfo(stationcode):
#     for i in range(len(si["data"]["stations"])):
#         if si["data"]["stations"][i]["stationCode"]==stationcode:
#             return si["data"]["stations"][i]
#
# getinfo(10)
# getinfo(145)

# print(getinfo(12))
#mdf = pd.read_csv("data/1656229490")
#
# earthquakes = hv.Points(mdf, kdims=['lon', 'lat'],
#                             vdims=['name'])
#
# show( hv.render(earthquakes) )


def PlotLast():


    mdf = pd.read_csv("data/1656242120.csv")

    stations = hv.Points(mdf,   kdims=['lon', 'lat'],
                                vdims=['name',"nbElec","nbMecha","nbdocklibre"])

    graph = stations.opts(tools=["hover"],
                            width=1000,
                            height=600)

    show( hv.render(graph) )

def testFolium():
    def auto_open(path):
        html_page = f'{path}'
        # open in browser.
        new = 2
        webbrowser.open(html_page, new=new)

    paris = folium.Map(location=[48.856578, 2.351828], zoom_start=12)

    mdf = pd.read_csv("data/1656242120.csv")
    for i in range(len(mdf)):
        print(i)
        # infos = mdf["name"][i]+"\n"+str(mdf["nbElec"][i])+"\n"+str(mdf["nbMecha"][i])+"\n"+str(mdf["nbdocklibre"][i])
        #stations = hv.Points(mdf, kdims=['lon', 'lat'],
                            # vdims=['name', "nbElec", "nbMecha", "nbdocklibre"])
        #hv.save(stations, "test.html")
        html = """
            <iframe src=\"""" +"test.html"+ """\" width="850" height="400"  frameborder="0">    
            """
        popup = folium.Popup(folium.Html(html, script=True))

        folium.Marker([mdf["lat"][i], mdf["lon"][i]], popup=popup, radius=3).add_to(paris)


    paris.save('temp.html')
    auto_open("temp.html")

def testOSM():
    api = Api()


################################
#
# from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Person:
    name: str


person = Person(name='lidatong')
person.to_json()  # '{"name": "lidatong"}' <- this is a string
person.to_dict()  # {'name': 'lidatong'} <- this is a dict
Person.from_json('{"name": "lidatong"}')  # Person(1)
Person.from_dict({'name': 'lidatong'})  # Person(1)

# You can also apply _schema validation_ using an alternative API
# This can be useful for "typed" Python code

Person.from_json('{"name": 42}')  # This is ok. 42 is not a `str`, but
                                  # dataclass creation does not validate types
Person.schema().loads('{"name": 42}')  # Error! Raises `ValidationError`