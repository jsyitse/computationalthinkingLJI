# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 11:45:52 2019

@author: Jessica Tse
"""

import pandas as pd

import os
directory = r'C:\Users\Jessica Tse\Desktop\Computational Thinking\2018'

## crap ##
'''
filenames = []
for filename in os.listdir(directory):
    filenames.append(filename)
print(filenames)

for name in filenames:
    if 'csv' in name:
        name = pd.read_csv(filename)
    #for num in range(len(directory)):
        
        #if '.csv' in filename:
         #   df = pd.read_csv(filename)
'''        
            
            
            
## gets all the data into a dictionary of the names and data ##
mydir = r'H:\2018'
os.chdir(mydir)

def createDict():
    file_names = []
    mydir = r'H:\2018'
    for filename in os.listdir(mydir):
        if '.csv' in filename:
            file_names.append(filename)
    dict1 = {}
    for filename in os.listdir(mydir):
        if '.csv' in filename:
            data = pd.read_csv(filename, header = 0)
            filename = filename[19:]
            filename = filename[:-4]
            dict1[filename] = data
    return dict1
print(createDict())


## the non function part of it trying to create and name dfs ##
mydir = r'H:\2018'
os.chdir(mydir)


file_names = []
mydir = r'H:\2018'
for filename in os.listdir(mydir):
    if '.csv' in filename:
        file_names.append(filename)
dict1 = {}
for filename in os.listdir(mydir):
    if '.csv' in filename:
        data = pd.read_csv(filename, header = 0)
        filename = filename[19:]
        filename = filename[:-4]
        dict1[filename] = data




for key in dict1:
    exec(f'{key} = pd.DataFrame()')
           
    
    
