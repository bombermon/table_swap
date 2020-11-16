import csv, pickle
import re

field_names = ['No', 'Company', 'Car Model'] #СЮДА ЗАПИСЫВАЕМ КЛЮЧИ

temp_data = [
{'No': 1, 'Company': 'Ferrari', 'Car Model': '488 GTB'},
{'No': 2, 'Company': 'Porsche', 'Car Model': '918 Spyder'},
{'No': 3, 'Company': 'Bugatti', 'Car Model': 'La Voiture Noire'},
{'No': 4, 'Company': 'Rolls Royce', 'Car Model': 'Phantom'},
{'No': 5, 'Company': 'BMW', 'Car Model': 'BMW X7'},
]  # СЛОВАРИ С ДАННЫМИ

def save_table(data, file, type = 'csv'):
    if type == 'csv':
        with open(file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(data)

    if type == 'pickle':
        with open('NewFile' + '.pickle') as f:
            for i in data:
                pickle.dumps(i, f)
        f.close()

    if type == 'txt':
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
