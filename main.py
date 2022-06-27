
import requests
import csv

def GetDataAndSave():
    si = requests.get(
        "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json").json()
    vi = requests.get('https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json').json()

    infos = si["data"]["stations"]

    for i in range(len(infos)):
        for j in range(len(vi["data"]["stations"])):
            if vi["data"]["stations"][j]["station_id"] == infos[i]["station_id"]:
                bikeinfosstation = vi["data"]["stations"][j]
                infos[i]["nbMecha"] = bikeinfosstation["num_bikes_available_types"][0]["mechanical"]
                infos[i]["nbElec"] = bikeinfosstation["num_bikes_available_types"][1]["ebike"]
                infos[i]["nbdocklibre"] = bikeinfosstation["num_docks_available"]
                infos[i]["last_reported"] = bikeinfosstation["last_reported"]
                break

    # print(infos[0:3])

    with open("data/" + str(si["lastUpdatedOther"]) + ".csv", 'w', encoding='utf8', newline='\n') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=infos[0].keys(), extrasaction='ignore')
        dict_writer.writeheader()
        dict_writer.writerows(infos)

    #print(datetime.fromtimestamp(si["lastUpdatedOther"]), " encore valable : ", str(si["ttl"]), " s")


if __name__ == '__main__':
    GetDataAndSave()
    #PlotLast()
    #testOSM()
    #testFolium()