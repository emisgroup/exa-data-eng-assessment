# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 15:32:27 2022

@author: Youssef

This  is a technical task as part of my application to Emis_Health

The script does the following:
-converts json files to pandas dataframe format. 
-Upload the data to mysql database.
-Containerise data pipeline using docker image/ docker-compose.
"""
import json
import pandas as pd
import os
import glob

def get_files(files_path):
    """Import json files from a folder"""
    #Create empty list
    all_files = []
    for root, dirs, diles in os.walk(files_path):
        #Search all files ending with .json in dir
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            #Append json files to the list
            all_files.append(os.path.abspath(f)) 
    return all_files

#TODO conver or extract json files to dataframes
def readJsonfiles(files_path, all_files):
    """Read json format in pandas dataframes"""
    for t in all_files:
        df = pd.read_json(t)
        df1 = pd.json_normalize(df)
        
    df.head()
    df.info()
    return df

if __name__ == '__main__':
    """Import json files from a folder, then convert json to dataframe"""
    #Path to all json files folder
    files_path = '../data'
    #The links to json files
    all_files = get_files(files_path)
    #Read json files to dataframes
    df = readJsonfiles(files_path, all_files)