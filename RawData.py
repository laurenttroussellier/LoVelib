from dataclasses import dataclass
from dataclasses_json import dataclass_json

import requests
import pandas as pd
import holoviews as hv

hv.extension('bokeh')
from bokeh.plotting import show
import json

from holoviews.ipython import display

#
data = requests.get('https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json').json()
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
si = requests.get(
    "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json").json()


#
# df=pd.DataFrame.from_dict(data["data"]["stations"])
# dff=pd.DataFrame.from_dict(si["data"]["stations"])
#
# mdf = df.merge(dff, how='inner', on='station_id')
#
#
# mdf.to_csv("data/"+str(si["lastUpdatedOther"]))
def getinfo(i):
    stationsid = data["data"]["stations"][i]["stationCode"]
    nbMecha = data["data"]["stations"][i]["num_bikes_available_types"][0]["mechanical"]
    nbElec = data["data"]["stations"][i]["num_bikes_available_types"][1]["ebike"]
    nbdocklibre = data["data"]["stations"][i]["num_docks_available"]
    last_reported = data["data"]["stations"][i]["last_reported"]

    print(getstationinfo(stationsid))

    print(stationsid, nbMecha, nbElec, nbdocklibre, last_reported)


def getstationinfo(stationcode):
    for i in range(len(si["data"]["stations"])):
        if si["data"]["stations"][i]["stationCode"] == stationcode:
            return si["data"]["stations"][i]


getinfo(10)
getinfo(145)

# print(getinfo(12))
# mdf = pd.read_csv("data/1656229490")
#
# earthquakes = hv.Points(mdf, kdims=['lon', 'lat'],
#                             vdims=['name'])
#
# show( hv.render(earthquakes) )
