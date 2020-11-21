import csv, pickle
import re

temp_data = [{'No': ['1999', '2', '3', '4'], 'Company': ['Ferrari', 'Lamborghini', 'porsche', 'BMW'],
              'Car Model': ['488 GTB', 'phantom', 'macan', 'X5']},
             {'No': [float, int, bool, str], 'Company': [float, int, bool, str],
              'Car Model': [float, int, bool, str]}]

temp_spisok = ['1', '2', '3', '4', '5']


def print_table():
    data = temp_data[0]
    len_of_col = {}
    max_l = 0
    for i in data:  # ПЕРЕБОР СЛОВАРЯ ПО ВСЕМ СЛОВАМ И ЗНАЧЕНИЯМ
        if len(i) > max_l:  # НАХОЖДЕНИЕ САМОГО ДЛИННОГО СЛОВА
            max_l = len(i)
        for j in data[i]:
            if len(j) > max_l:
                max_l = len(j)
        len_of_col[i] = max_l

    field_names_len = {}
    for i in len_of_col:  # ФОРМИРОВАНИЕ РОВНЫХ СТОЛБЦОВ
        temp_key = i
        if len(i) < len_of_col[i]:
            while len(i) < len_of_col[temp_key]:
                i = i + ' '
        print(i + '|', end="")
        field_names_len[i] = len_of_col[temp_key]
    print()

    num_str = 0
    while True:
        try:
            for i in data:  # ДОБАВЛЕНИЕ ПРОБЕЛОВ ДЛЯ РОВНЫХ СТОЛБЦОВ
                temp = data[i][num_str]
                if len(temp) < len_of_col[i]:
                    while len(temp) < len_of_col[i]:
                        temp += ' '
                temp += '|'
                print(temp, end='')
            print()
            num_str += 1
        except IndexError:
            break


def save_table(data, type='csv'):
    if type == 'csv':
        temp_table = []
        field_names = data.keys()
        num_of_colums = 0
        for i in field_names:
            num_of_colums = max(num_of_colums, len(data[i]))
        for i in range(0, num_of_colums):
            values = dict.fromkeys(field_names)
            for j in field_names:
                if i < len(data[j]):
                    values[j] = data[j][i]
            temp_table.append(values)
        print(temp_table)
        with open('NewFile' + '.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(temp_table)

    elif type == 'pickle':
        with open('NewFile' + '.pickle', 'wb') as f:
            pickle.dump(data, f)

    elif type == 'txt':
        with open('NewFile' + '.txt', 'w') as f:
            data = temp_data
            len_of_col = {}  # СЛОВАРЬ ДЛЯ ХРАНЕНИЯ ДЛИНЫ СТОЛБЦОВ
            max_l = 0
            for i in data:  # ПЕРЕБОР СЛОВАРЯ ПО ВСЕМ СЛОВАМ И ЗНАЧЕНИЯМ
                if len(i) > max_l:  # НАХОЖДЕНИЕ САМОГО ДЛИННОГО СЛОВА
                    max_l = len(i)
                for j in data[i]:
                    if len(j) > max_l:
                        max_l = len(j)
                len_of_col[i] = max_l  # ЗАПОЛНЕНИЯ СЛОВАРЯ МАКСИМАЛЬНЫМИ ДЛИНАМИ

            field_names_len = {}
            for i in len_of_col:  # ФОРМИРОВАНИЕ РОВНЫХ СТОЛБЦОВ
                temp_key = i
                if len(i) < len_of_col[i]:
                    while len(i) < len_of_col[temp_key]:
                        i = i + ' '
                print(i + '|', file=f, end="")
                field_names_len[i] = len_of_col[temp_key]
            print(file=f)

            num_str = 0
            while True:
                try:
                    for i in data:  # ДОБАВЛЕНИЕ ПРОБЕЛОВ ДЛЯ РОВНЫХ СТОЛБЦОВ
                        temp = data[i][num_str]
                        if len(temp) < len_of_col[i]:
                            while len(temp) < len_of_col[i]:
                                temp += ' '
                        temp += '|'
                        print(temp, file=f, end='')
                    print(file=f)
                    num_str += 1
                except IndexError:
                    break


def load_table(file, type="csv"):
    global temp_data
    dictionary = {}  # Храним таблицу
    try:
        if type == "pickle":  # Считываем таблицу используя pickle
            dictionary = pickle.load(file)
        elif type == "csv":  # Считываем таблицу используя csv
            file_reader = csv.reader(file, delimiter=",")  # преобразуем файл в лист листов
            table_key_dictionary = {}  # Создаем словарь атрибутов таблицы и записываем их номер
            # Счетчик для подсчета количества строк
            lines_count = 0  # Считаем номер строки
            # Считывание данных из CSV файла
            for row in file_reader:  # Проходимся по строкам таблицы
                if lines_count == 0:  # В первой строк находяться атрибуты, создаем ключи в словаре
                    key_count = 0
                    for i in row:
                        dictionary[i] = []
                        table_key_dictionary[key_count] = i
                        key_count += 1
                else:
                    key_count = 0
                    for i in row:
                        dictionary.get(table_key_dictionary.get(key_count)).append(
                            i)  # Записываем нужный столбик нужный элемент
                        key_count += 1
                lines_count += 1
    except ValueError:
        print('Fail')
    temp_data[0] = dictionary


def set_values(values, column=0):
    try:
        data = temp_data[0]
        typer = temp_data[1]
        field_names = []
        flag = False
        for i in data:
            field_names.append(i)
        for k in values:
            flag = False
            for j in typer[field_names[column]]:
                if type(k) == j:
                    flag = True
            if flag == False:
                print('Оишбка! Вы ввели значения, не подходящие данному столбцу(', typer[field_names[column]], ')')
                return

        data[field_names[column]] = values
    except IndexError:
        print('Ошибка: номер столбца выбран неверно!')

def get_rows_by_number():
    with open('table.csv') as csv_file:
        csv_reader = list(csv.reader(csv_file))
        number_1 = int(input('Введите номер первой строчки: '))
        number_2 = int(input('Введите номер второй строчки: '))
        print(csv_reader[number_1-1:number_2])

# ЗОНА ТЕСТОВ НАЧАЛО ЗОНА ТЕСТОВ НАЧАЛО ЗОНА ТЕСТОВ НАЧАЛО ЗОНА ТЕСТОВ НАЧАЛО ЗОНА ТЕСТОВ НАЧАЛО ЗОНА ТЕСТОВ НАЧАЛ

set_values(temp_spisok)

save_table(temp_data[0], type='csv')
print_table()

# ЗОНА ТЕСТОВ КОНЕЦ ЗОНА ТЕСТОВ КОНЕЦ ЗОНА ТЕСТОВ КОНЕЦ ЗОНА ТЕСТОВ КОНЕЦ ЗОНА ТЕСТОВ КОНЕЦ ЗОНА ТЕСТОВ КОНЕЦ ЗОНА
