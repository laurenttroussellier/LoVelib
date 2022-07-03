
from glob import glob
import numpy as np
import pandas as pd
from datetime import datetime


def AggregateCurrentData():


    # Get the list of all the csv files in data path
    csv_flist = glob( "data/*.csv")
   # i=0
    df_list = []
    for _file in csv_flist:
        # if i == 2:
        #     break
        # else:
        #     i=i+1
        # get the file name from the data path
        file_name = _file.split("\\")[-1]
        #print(_file)
        #print(file_name)
        # extract the date from a file name, e.g. "data.2018-06-01.csv"
        date = datetime.fromtimestamp(int(file_name[:-4]))

        # read the read the data in _file
        df = pd.read_csv(_file)

        # add a column date knowing that all the data in df are recorded at the same date
        df["date"] = np.repeat(date, df.shape[0])
        df["date"] = df.date.astype("datetime64[ns]")  # reset date column to a correct date format

        #print(df.head())
        # append df to df_list
        df_list.append(df)

        #print(df_list)
    #print(df.columns)

    df_all = pd.concat(df_list, ignore_index=True).sort_index()
    data = df_all.set_index(["station_id","date"]).sort_index()
    xds = data.to_xarray()
    print(xds)
    xds.to_netcdf("dataNetCdf/test.nc")

if __name__ == '__main__':
    AggregateCurrentData()
