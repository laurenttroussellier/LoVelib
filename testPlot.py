import xarray as xr
import matplotlib.pyplot as plt
import webbrowser

import folium
import pandas as pd
import base64
from io import BytesIO

def testFolium():
    def auto_open(path):
        html_page = f'{path}'
        # open in browser.
        new = 2
        webbrowser.open(html_page, new=new)

    paris = folium.Map(location=[48.856578, 2.351828], zoom_start=12)

    #mdf = pd.read_csv("data/1656242120.csv")
    da = xr.open_dataset("dataNetCdf/test.nc")
    for i,idStation in enumerate(da["station_id"].values):

        print(i,idStation)
        SaveHtmlPlotForStation(da,i)
        #print(i)
        # infos = mdf["name"][i]+"\n"+str(mdf["nbElec"][i])+"\n"+str(mdf["nbMecha"][i])+"\n"+str(mdf["nbdocklibre"][i])
        #stations = hv.Points(mdf, kdims=['lon', 'lat'],
                            # vdims=['name', "nbElec", "nbMecha", "nbdocklibre"])
        #hv.save(stations, "test.html")
        html = """
            <iframe src=\"""" +"dataHtml/"+str(idStation)+".html"+ """\" width="850" height="400"  frameborder="0">    
            """
        popup = folium.Popup(folium.Html(html, script=True))

        folium.Marker([da["lat"][i].values[0], da["lon"][i].values[0]], popup=popup, radius=3).add_to(paris)


    paris.save('temp.html')
    auto_open("temp.html")


def aVoir():
    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    html = 'Some html head' + '<img src=\'data:image/png;base64,{}\'>'.format(encoded) + 'Some more html'

    with open('test.html', 'w') as f:
        f.write(html)

def SaveHtmlPlotForStation(da,nb):
    fig = plt.figure(num=1, clear=True)
    da["nbElec"].isel({"station_id": nb}).plot()
    #fig.show()
    a=2
    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    html = 'Some html head' + '<img src=\'data:image/png;base64,{}\'>'.format(encoded) + 'Some more html'
    with open("dataHtml/"+str(da["station_id"][nb].values)+".html", 'w') as f:
        f.write(html)



def plotForStation(da,nb):
    da["nbElec"].isel({"station_id": nb}).plot()
    plt.show()

# da = xr.open_dataset("dataNetCdf/test.nc")
# SaveHtmlPlotForStation(da,357)
# a=2
testFolium()

#plotForStation(2)