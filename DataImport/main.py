import os
import zipfile
import csv
import pandas as pd
from io import StringIO
import glob


data_path = '../Data/'
for filename in os.listdir(data_path):
    if zipfile.is_zipfile(data_path+filename):
        with zipfile.ZipFile(data_path+filename) as current_zip:
            for csv_filename in current_zip.namelist():
                if csv_filename[-4:] != '.csv':
                    continue
                raw_data = pd.read_csv(current_zip.open(csv_filename), encoding='GBK')
                print('read data for ' + csv_filename)
    else:
        continue
