import csv, pickle
import re



temp_data = {'No': ['1','2','3','4'], 'Company': ['Ferrari','Lamba'], 'Car Model': ['488 GTB','phantom']}

def save_table(data, type = 'pickle'):
    if type == 'csv':
        with open('NewFile' + '.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile)
           # writer.writeheader()
            writer.writerows(data)

    elif type == 'pickle':
        with open('NewFile' + '.pickle', 'wb') as f:
            pickle.dump(data, f)
        f.close()

    elif type == 'txt':
        with open('NewFile' + '.txt') as f:
            data = data
        f.close()

save_table(temp_data, type='pickle')


def load_table(file, type = "csv"):
    dictionary = {} # Храним таблицу
    if type == "pickle": # Считываем таблицу используя pickle
        dictionary = pickle.load(file)
    elif type == "csv": # Считываем таблицу используя csv
        file_reader = csv.reader(file, delimiter=",") # преобразуем файл в лист листов
        table_key_dictionary = {} # Создаем словарь атрибутов таблицы и записываем их номер
        # Счетчик для подсчета количества строк
        lines_count = 0 # Считаем номер строки
        # Считывание данных из CSV файла
        for row in file_reader: # Проходимся по строкам таблицы
            if lines_count == 0: # В первой строк находяться атрибуты, создаем ключи в словаре
                key_count = 0
                for i in row:
                    dictionary[i] = []
                    table_key_dictionary[key_count] = i
                    key_count += 1
            else:
                key_count = 0
                for i in row:
                    dictionary.get(table_key_dictionary.get(key_count)).append(i) # Записываем нужный столбик нужный элемент
                    key_count += 1
            lines_count += 1
    else:
        return -1
    return dictionary
