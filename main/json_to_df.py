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
import os
import glob

"""Import json files from a folder"""
def get_files(files_path):
    all_files = []
    for root, dirs, diles in os.walk(files_path):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))
            
    return all_files

if __name__ == '__main__':
    """Import json files from a folder, then convert json to dataframe"""
    #Path to all json files
    files_path = 'C:\Sandbox\Emis_Task\data'
    #
    json_data = get_files(files_path)