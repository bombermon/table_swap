import csv, pickle

temp_data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}, 'clear': ['dada']
}

def save_table(data, type = 'csv'):
    if type == 'csv':
        with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
            names = []
            for i in data:
                names.append(i)
            file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=names)
            file_writer.writeheader()
            temp = {}
            for i in data:
                for j in data[i]:

                    temp[i] = j
                    print(temp)
                    file_writer.writerow(temp)
                    temp.clear()

    if type == 'pickle':
        with open('NewFile' + '.pickle') as f:
            data = data
        f.close()

    if type == 'txt':
        with open('NewFile' + '.txt') as f:
            data = data
        f.close()

save_table(temp_data)


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

