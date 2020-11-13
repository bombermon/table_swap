import csv, pickle

temp_data = {}

def save_table(data, type = 'csv'):
    if type == 'csv':
       ''' with open('NewFile' + '.csv', mode= 'w', encoding='UTF-8') as f:
            #writer = csv.writer(f, delemiter = ',', lineterminator = '\r')
            names = []
            for i in data:
                names.append(i)
            writer = csv.DictWriter(f, delimiter=",", lineterminator="\r", fieldnames=names)
            writer.writeheader()
            writer.writerow({"Имя": "Саша", "Возраст": "6"})
            writer.writerow({"Имя": "Маша", "Возраст": "15"})
            writer.writerow({"Имя": "Вова", "Возраст": "14"})
            '''

       with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
           file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
           file_writer.writerow(["Имя", "Класс", "Возраст"])
           file_writer.writerow(["Женя", "5", "10"])
           file_writer.writerow(["Саша", "5", "12"])
           file_writer.writerow(["Маша", "11", "18"])
           w_file.close()

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

