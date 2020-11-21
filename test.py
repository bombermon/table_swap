import csv
import pickle
import re


class Table:
    __data = {'No': ['1999', '2', '3', '4'], 'Company': ['Ferrari', 'Lamborghini', 'porsche', 'BMW'],
              'Car Model': ['488 GTB', 'phantom', 'macan', 'X5']}
    __type_list = {'No': str, 'Company': str,
                   'Car Model': str}

    # ФУНКЦИЯ ИЗМЕНЕНИЯ ЗНАЧЕНИЙ В ОПРЕДЕЛЕННОМ СТОЛБИКЕ НАЧАЛО
    def set_values(self, values, column=0):
        try:
            data = self.__data
            typer = self.__type_list
            field_names = []
            flag = False
            for i in data:
                field_names.append(i)
            for k in values:
                flag = False
                if type(k) == typer[field_names[column]]:
                    flag = True
                if flag == False:
                    print('Оишбка! Вы ввели значения, не подходящие данному столбцу(', typer[field_names[column]], ')')
                    return

            data[field_names[column]] = values
        except IndexError:
            print('Ошибка: номер столбца выбран неверно!')
    # ФУНКЦИЯ ИЗМЕНЕНИЯ ЗНАЧЕНИЙ В ОПРЕДЕЛЕННОМ СТОЛБИКЕ НАЧАЛО

    # ФУНКЦИЯ ВЫВОДА ТАБЛИЦЫ В КОНСОЛЬ НАЧАЛО
    def print_table(self):
        data = self.__data
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

    # ФУНКЦИЯ ВЫВОДА ТАБЛИЦЫ В КОНСОЛЬ НАЧАЛО

    # ФУНКЦИЯ СОХРАНЕНИЯ ТАБЛИЦЫ В НОВЫЙ ФАЙЛ НАЧАЛО
    def save_table(self, type='csv'):
        data = self.__data
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
            with open('NewFile' + '.csv', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(temp_table)

        elif type == 'pickle':
            with open('NewFile' + '.pickle', 'wb') as f:
                pickle.dump(data, f)

        elif type == 'txt':
            with open('NewFile' + '.txt', 'w') as f:
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
    # ФУНКЦИЯ СОХРАНЕНИЯ ТАБЛИЦЫ В НОВЫЙ ФАЙЛ КОНЕЦ

    # ФУНКЦИЯ ВЫГРУЗКИ ТАБЛИЦЫ ИЗ ФАЙЛА НАЧАЛО
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

    # ФУНКЦИЯ ВЫГРУЗКИ ТАБЛИЦЫ ИЗ ФАЙЛА КОНЕЦ

    def get_column_types(self, by_number = True): #Получаем словарь с типами столбцов
        if by_number: # если надо нумеруем от одного
            type_list = {}
            counter = 1
            for i in self.__type_list:
                type_list.update({counter : self.__type_list[i]})
                counter += 1
            return type_list
        else: # иначе по названию колонки
            return self.__type_list

