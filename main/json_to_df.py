# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 15:32:27 2022

@author: Youssef

This  is a technical task as part of my application to Emis_Health

The script does the following:
-converts json files to patirnt resources. 
-converts patirnt resources to pandas dataframe format. 
-Upload the data to mysql database.
-Containerise data pipeline using docker image/ docker-compose.
"""
#Imports
import json
import pandas as pd
import os
import glob
import psycopg2
#From psycopg2.extras import extra, extensions
import psycopg2.extras
import psycopg2.extensions
#Import config file
import yaml

def getConfig():
    with open('../config.yml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        return config
    
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

def get_json(filename):
    """Lead json params"""
    with open(filename) as f:
        return json.load(f)

#TODO upload nested fhir resources to postgresql
#TODO add docker file
def jsonToResources(all_files, output_dir):
    """loop through each json file and create seprate resources per patient"""
    for input_file in all_files:
        patient = get_json(input_file)
        resources = {}
        for entry in patient['entry']:
            resource = entry['resource']
            resource_type = resource['resourceType']
            #Get resource type from keys
            if resource_type not in resources.keys():
                resources[resource_type] = []
            #Append resource to list of resources dict
            resources[resource_type].append(resource)
        for key in resources.keys():
            #Print total resources count for this patient
            print(f'{key}: {len(resources[key])}')
            
def create_staging_table(cur):
    # Create a Table to store JSON data:
    cur.execute("""
        DROP TABLE IF EXISTS nested_tweets;
        CREATE UNLOGGED TABLE nested_tweets (
        ID serial NOT NULL PRIMARY KEY,
     fhir jsonb );""")
    return True

def fcn(all_files,table,cur):
    if len(df) > 0:
        df_columns = list(df)
        columns = ",".join(df_columns)
        # create VALUES('%s', '%s",...) one '%s' per column
        values = "VALUES({})".format(",".join(["%s" for _ in df_columns])) 
        #create INSERT INTO table (columns) VALUES('%s',...)
        insert_stmt = "INSERT INTO {} ({}) {}".format(table,columns,values)
        cur.execute("truncate " + table + ";")  #avoiding uploading duplicate data!
        cur = conn.cursor()
        psycopg2.extras.execute_batch(cur, insert_stmt, df.values)
    conn.commit()
    return True

if __name__ == '__main__':
    """Import json files from a folder, then convert json to dataframe"""
    #Get the config params
    params = getConfig()
    #Connection to postgresql
    conn = psycopg2.connect(params['pstsql']) 
    #Open a cursor to perform database operations
    cur = conn.cursor() 
    conn.autocommit = True  
    create_staging_table(cur)
    #Path to all json files folder
    files_path = params['files_path']    
    output_dir = params['output_dir']
    #The links to json files
    all_files = get_files(files_path)
    #Read json files to dataframes
    df = jsonToResources(all_files, output_dir)
    fcn(df,'nested_fhir',cur)
