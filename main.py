import csv, pickle

temp_data = {}

def save_table(data, type = 'csv'):
    if type == 'csv':
        with open('NewFile' + '.csv') as f:
            data = data
        f.close()

    if type == 'pickle':
        with open('NewFile' + '.pickle') as f:
            data = data
        f.close()

    if type == 'txt':
        with open('NewFile' + '.txt') as f:
            data = data
        f.close()

