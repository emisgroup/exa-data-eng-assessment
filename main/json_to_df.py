# -*- coding: utf-8 -*-
"""
This  is a task as part of my application to emis_health

The script does the following:
    
-converts json files to pandas dataframe format. 
-Upload the data to mysql database.
-Containerise data pipeline using docker image/ docker-compose.

"""
import json
import pandas as pd

def getJsonToDF(json_path):
    """First look at json files"""
    with open(json_path) as f:
        df = json.load(f)
        
    # load data using Python JSON module
    with open('json_path','r') as f:
        data = json.loads(f.read())
    # Flatten data
    df_nested_list = pd.json_normalize(data)
    return df, data, df_nested_list



if __name__ == '__main__':
    json_path = 'C:\Sandbox\Emis_Task\data\Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.json'
