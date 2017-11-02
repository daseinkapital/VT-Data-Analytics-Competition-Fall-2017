# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 17:40:57 2017

@author: Andrew
"""

import csv
import os

def convert_data_to_cleaned_list(data, all_headers):
    master_list = []
    for line in data:
        row = data[line]
        new_list = []
        for h in all_headers:
            if h in row:
                new_list.append(row[h])
            else:
                new_list.append('NQ')
        master_list.append(new_list)
    return master_list


path = os.path.join(os.getcwd(), 'csv_files')
first_file = True
all_headers = []
all_headers.append('seqn')
for root, dirs, files in os.walk(path):
    for file in files:
        if ("DR1IFF" in file) or ("DR2IFF" in file):
            continue
        print(file)
        if first_file:
            f = open(os.path.join(path, file), 'r')
            reader = csv.DictReader(f, delimiter=",")
            headers = next(reader)
            data = {}
            csv_data = {}
            for h in headers:
                csv_data[h] = {}
            for row in reader:
                for h in headers:
                    csv_data[h] = row[h]
                data[row['seqn']] = csv_data
                csv_data = {}
            first_file = False
                        
        else:
            f = open(os.path.join(path, file), 'r')
            reader = csv.DictReader(f, delimiter=",")
            headers = next(reader)
            current_headers = []
            csv_data = {}
            for h in headers:
                if h != "seqn":
                    current_headers.append(h)
                    csv_data[h] = {}
            for row in reader:
                for h in current_headers:
                    csv_data[h] = row[h]
                if row['seqn'] in data:
                    data[row['seqn']].update(csv_data)
                else:
                    data[row['seqn']] = csv_data
                csv_data = {}
            all_headers += current_headers
    
        

master = convert_data_to_cleaned_list(data, all_headers)

with open('master_cleaned.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(all_headers)
    writer.writerows(master)