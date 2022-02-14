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
import sys, getopt
import pathlib
from pathlib import Path
from fhir.resources.patient import Patient
from fhirclient.models.bundle import BundleEntrySearch
from fhirclient.models.humanname import HumanName

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
    """Lead json file"""
    with open(filename) as f:
        return json.load(f)

#TODO add config file 
#TODO create tables for each resource linked to the patient
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
            #Save resource files to dir
            with open(f'{output_dir}/{str(resource_type).lower()}_{len(resources[resource_type])}.json', 'w') as enc:
                enc.write(json.dumps(resource))
            #Append resource to list of resources dict
            resources[resource_type].append(resource)
        for key in resources.keys():
            #Print total resources count for this patient
            print(f'{key}: {len(resources[key])}')

if __name__ == '__main__':
    """Import json files from a folder, then convert json to dataframe"""
    #Path to all json files folder
    files_path = '../data'
    output_dir = r'C:\Sandbox\Emis_Task\patient_resources'
    #The links to json files
    all_files = get_files(files_path)
    #Read json files to dataframes
    df = jsonToResources(all_files, output_dir)