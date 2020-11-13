import csv, pickle

temp_data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

def save_table(data, type = 'csv'):
    if type == 'csv':
        with open('NewFile' + '.csv', mode= 'wb') as f:
            #writer = csv.writer(f, delemiter = ',', lineterminator = '\r')
            names = []
            for i in data:
                names.append(i)
            writer = csv.DictWriter(data, delimiter=",", lineterminator="\r", fieldnames=names)
            writer.writeheader()
            writer.writerow(data)

        f.close()

    if type == 'pickle':
        with open('NewFile' + '.pickle') as f:
            data = data
        f.close()

    if type == 'txt':
        with open('NewFile' + '.txt') as f:
            data = data
        f.close()

save_table(temp_data)
