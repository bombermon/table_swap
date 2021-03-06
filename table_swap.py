import csv
import pickle
import re
import os.path


class Table:
    _data = {}
    _type_list = {}

    # ФУНКЦИЯ ИЗМЕНЕНИЯ ЗНАЧЕНИЙ В ОПРЕДЕЛЕННОМ СТОЛБИКЕ НАЧАЛО
    def set_values(self, values, column=0):
        try:
            data = self._data
            types = self._type_list
            field_names = []
            for i in data:  # ПЕРЕВОДИМ ПЕРВУЮ СТРОКУ В ЛИСТ
                field_names.append(i)
            if type(column) == str:
                column = field_names.index(column)

            for k in values:
                flag = False
                if type(k) == types[field_names[column]]:  # СВЕРЯЕМ ПРАВИЛЬНОСТЬ ТИПА НОВОГО ЗНАЧЕНИЯ
                    flag = True
                if not flag:
                    print('Оишбка! Вы ввели значения типа %(t_value)s, не подходящие данному столбцу (%(t_true)s)' %
                          {'t_value': type(k), 't_true': types[field_names[column]]})
                    return
            if len(data[field_names[column]]) == len(values):  # ПРОВЕРЯЕМ СКОЛЬКО НАМ НУЖНО ЗАМЕНИТЬ ЗНАЧЕНИЙ ИЗ ЛИСТА
                data[field_names[column]] = values
            else:
                n = 0
                for j in values:
                    if n == len(values):
                        return
                    data[field_names[column]][n] = j  # ЗАМЕНЯЕМ ПРОШЛЫЙ ЛИСТ В НОВЫЙ ЛИСТ
                    n += 1
        except IndexError:  # ЕСЛИ УКАЗАН НОМЕР, КОТОРОГО НЕ СУЩЕСТВУЕТ В СЛОВАРЕ
            print('Ошибка: номер столбца выбран неверно!')
        except ValueError:  # ЕСЛИ НЕПРАВИЛЬНО УКАЗАЛИ ТЕКСТОВОЕ ЗНАЧЕНИЕ
            print('Ошибка: имя столбца указано неверно')

    def set_value(self, value, column=0):
        try:
            data = self._data
            types = self._type_list
            field_names = []
            for i in data:  # ПЕРЕВОДИМ ПЕРВУЮ СТРОКУ В ЛИСТ
                field_names.append(i)
            if type(column) == str:
                column = field_names.index(column)
            flag = False
            if type(value) == types[field_names[column]]:  # СВЕРЯЕМ ПРАВИЛЬНОСТЬ ТИПА НОВОГО ЗНАЧЕНИЯ
                flag = True
            if not flag:
                print('Оишбка! Вы ввели значение типа %(t_value)s, не подходящие данному столбцу (%(t_true)s)' %
                      {'t_value': type(value), 't_true': types[field_names[column]]})
                return
            self._data[field_names[column]][0] = value
        except IndexError:  # ЕСЛИ УКАЗАН НОМЕР, КОТОРОГО НЕ СУЩЕСТВУЕТ В СЛОВАРЕ
            print('Ошибка: номер столбца выбран неверно!')
        except ValueError:  # ЕСЛИ НЕПРАВИЛЬНО УКАЗАЛИ ТЕКСТОВОЕ ЗНАЧЕНИЕ
            print('Ошибка: имя столбца указано неверно')

    # ФУНКЦИЯ ИЗМЕНЕНИЯ ЗНАЧЕНИЙ В ОПРЕДЕЛЕННОМ СТОЛБИКЕ КОНЕЦ

    # ФУНКЦИЯ СЧИТЫВАНИЯ ЗНАЧЕНИЙ ИЗ ВНУТРЕННЕГО ПРЕДСТАВЛЕНИЯ ТАБЛИЦЫ НАЧАЛО
    def get_values(self, column=0):
        try:
            new_values = []
            if type(column) == str:
                new_values = self._data[column]
            elif type(column) == int:
                field_names = []
                for i in self._data:
                    field_names.append(i)
                new_values = self._data[field_names[column]]
            return new_values
        except IndexError:  # ЕСЛИ УКАЗАН НОМЕР, КОТОРОГО НЕ СУЩЕСТВУЕТ В СЛОВАРЕ
            print('Ошибка: номер столбца выбран неверно!')
        except ValueError:  # ЕСЛИ НЕПРАВИЛЬНО УКАЗАЛИ ТЕКСТОВОЕ ЗНАЧЕНИЕ
            print('Ошибка: имя столбца указано неверно')

    def get_value(self, column=0):
        try:
            new_value = None
            field_names = []
            for i in self._data:  # ПЕРЕВОДИМ ПЕРВУЮ СТРОКУ В ЛИСТ
                field_names.append(i)
            if type(column) == str:
                column = field_names.index(column)
            new_value = self._data[field_names[column]][0]
            return new_value
        except IndexError:  # ЕСЛИ УКАЗАН НОМЕР, КОТОРОГО НЕ СУЩЕСТВУЕТ В СЛОВАРЕ
            print('Ошибка: номер столбца выбран неверно!')
        except ValueError:  # ЕСЛИ НЕПРАВИЛЬНО УКАЗАЛИ ТЕКСТОВОЕ ЗНАЧЕНИЕ
            print('Ошибка: имя столбца указано неверно')

    # ФУНКЦИЯ СЧИТЫВАНИЯ ЗНАЧЕНИЙ ИЗ ВНУТРЕННЕГО ПРЕДСТАВЛЕНИЯ ТАБЛИЦЫ КОНЕЦ

    # ФУНКЦИЯ ВЫВОДА ТАБЛИЦЫ В КОНСОЛЬ НАЧАЛО
    def print_table(self):
        try:
            data = self._data
            len_of_col = {}
            full_len = 0
            max_l = 0
            for i in data:  # ПЕРЕБОР СЛОВАРЯ ПО ВСЕМ СЛОВАМ И ЗНАЧЕНИЯМ
                if len(i) > max_l:  # НАХОЖДЕНИЕ САМОГО ДЛИННОГО СЛОВА
                    max_l = len(i)
                for j in data[i]:
                    if type(j) == bool:
                        j = str(j)
                    if len(j) > max_l:
                        max_l = len(j)
                len_of_col[i] = max_l
                full_len += max_l
            print('┌', end='')
            for j in range(full_len + 2):
                print('-', end='')
            print('┐')
            field_names_len = {}
            print('|', end='')
            for i in len_of_col:  # ФОРМИРОВАНИЕ РОВНЫХ СТОЛБЦОВ
                temp_key = i
                if len(i) < len_of_col[i]:
                    while len(i) < len_of_col[temp_key]:
                        i = i + ' '
                print(i + '|', end="")
                field_names_len[i] = len_of_col[temp_key]
            print()

            num_str = 0
            try:
                while True:
                    if not any(data):
                        print('Данных нет!')
                        return
                    cheek_bool = True
                    for i in data:  # ДОБАВЛЕНИЕ ПРОБЕЛОВ ДЛЯ РОВНЫХ СТОЛБЦОВ
                        temp = data[i][num_str]
                        if type(temp) == bool:
                            temp = str(temp)
                        if cheek_bool:
                            print('|', end='')
                            cheek_bool = False
                        if len(temp) < len_of_col[i]:
                            while len(temp) < len_of_col[i]:
                                temp += ' '
                        temp += '|'
                        print(temp, end='')
                    print()
                    num_str += 1
            except IndexError:
                print('└', end='')
                for j in range(full_len + 2):
                    print('-', end='')
                print('┘')
                return
        except AttributeError:
            print('Таблица неверно записана!')
        except TypeError:
            print('В вашей таблице есть пустые значения!')
    # ФУНКЦИЯ ВЫВОДА ТАБЛИЦЫ В КОНСОЛЬ КОНЕЦ

    # ФУНКЦИЯ СОХРАНЕНИЯ ТАБЛИЦЫ В НОВЫЙ ФАЙЛ НАЧАЛО
    def save_table(self, name):
        try:

            data = self._data

            namelist = re.split('\.', name)  # ОТДЕЛЯЕМ ИМЯ И ТИП ФАЙЛА
            file_type = namelist[-1]
            namelist.pop(-1)
            name = ''
            for z in namelist:
                name += z
                name += '.'
            name = name[:-1]

            if file_type == 'csv':  # ПРОВЕРЯЕМ ТИП ФАЙЛА
                temp_table = []
                field_names = data.keys()
                num_of_columns = 0
                for i in field_names:
                    num_of_columns = max(num_of_columns, len(data[i]))
                for i in range(0,
                               num_of_columns):  # ПРЕОБРАЗУЕМ НАШЕ ПРЕДСТАВЛЕНИЕ В ПРЕДСТАВЛЕНИЕ УДОБНОЕ DictWriter CSV
                    values = dict.fromkeys(field_names)
                    for j in field_names:
                        if i < len(data[j]):
                            values[j] = data[j][i]
                    temp_table.append(values)
                with open(name + '.csv', 'w') as csv_file:  # ОТКРЫВАЕМ (ИЛИ СОЗДАЕМ ФАЙЛ CSV НА ЗАПИСЬ СЛОВАРЯ)
                    writer = csv.DictWriter(csv_file, fieldnames=field_names)
                    writer.writeheader()
                    writer.writerows(temp_table)

            elif file_type == 'pickle':
                with open(name + '.pickle', 'wb') as f:  # ОТКРЫВАЕМ ФАЙЛ В ФОРМАТЕ .pickle на чтение в битах
                    pickle.dump(self, f)  # ЗАПИСЫВАЕМ НАШ СЛОВАРЬ В ФАЙЛ .pickle

            elif file_type == 'txt':  # ЗАПИСЬ В ФАЙЛ .txt ТАКАЯ ЖЕ КАК ВЫВОД ТАБЛИЦЫ В КОНСОЛЬ
                with open(name + '.txt', 'w', encoding='UTF-8') as f:
                    len_of_col = {}  # СЛОВАРЬ ДЛЯ ХРАНЕНИЯ ДЛИНЫ СТОЛБЦОВ
                    max_l = 0
                    full_len = 0
                    for i in data:  # ПЕРЕБОР СЛОВАРЯ ПО ВСЕМ СЛОВАМ И ЗНАЧЕНИЯМ
                        if len(i) > max_l:  # НАХОЖДЕНИЕ САМОГО ДЛИННОГО СЛОВА
                            max_l = len(i)
                        for j in data[i]:
                            if type(j) == bool:
                                j = str(j)
                            if len(j) > max_l:
                                max_l = len(j)
                        len_of_col[i] = max_l  # ЗАПОЛНЕНИЯ СЛОВАРЯ МАКСИМАЛЬНЫМИ ДЛИНАМИ
                        full_len += max_l
                    print('┌', file=f, end='')
                    for j in range(full_len + 2):
                        print('-', file=f, end='')
                    print('┐', file=f)
                    field_names_len = {}
                    print('|', file=f, end='')
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
                            while True:
                                if not any(data):
                                    print('Данных нет!')
                                    return
                                cheek_bool = True
                                for i in data:  # ДОБАВЛЕНИЕ ПРОБЕЛОВ ДЛЯ РОВНЫХ СТОЛБЦОВ
                                    temp = data[i][num_str]
                                    if type(temp) == bool:
                                        temp = str(temp)
                                    if cheek_bool:
                                        print('|', file=f, end='')
                                        cheek_bool = False
                                    if len(temp) < len_of_col[i]:
                                        while len(temp) < len_of_col[i]:
                                            temp += ' '
                                    temp += '|'
                                    print(temp, file=f, end='')
                                print(file=f)
                                num_str += 1
                        except IndexError:
                            print('└', file=f, end='')
                            for j in range(full_len + 2):
                                print('-', file=f, end='')
                            print('┘', file=f)
                            return
            else:
                raise Exception('Вы ввели неверный тип файла!')
        except FileNotFoundError:
            print('Вы ввели неподдерживаемое имя файла!')

    # ФУНКЦИЯ СОХРАНЕНИЯ ТАБЛИЦЫ В НОВЫЙ ФАЙЛ КОНЕЦ

    def get_column_types(self, by_number=True):  # Получаем словарь с типами столбцов
        try:
            if by_number:  # если надо нумеруем от одного
                type_list = {}
                counter = 1
                for i in self._type_list:
                    type_list.update({counter: self._type_list[i]})
                    counter += 1
                return type_list
            else:  # иначе по названию колонки
                return self._type_list
        except IndexError:
            print('Введены неверные значения!')
        except ValueError:
            print('Введены неверные значения!')
        except AttributeError:
            print('Таблица неверно записана!')

    def set_column_types(self, type_dict, by_number=True):  # Считываем словарь с типами столбцов
        try:
            if type(type_dict) != dict:  # Проверка на соответствующий тип дл type_dict
                raise BaseException("type_dict не является словарем")
            if len(self._type_list) != len(type_dict):  # Проверка на размер таблицы
                raise BaseException("Несоответствующее количество колонок таблицы и слов в type_dict словаре")
            if by_number:
                temp = {}
                for i in range(1, len(type_dict) + 1):
                    if type_dict.get(i) == None:  # Проверка на нурмерацию таблицы при by_number = True
                        raise BaseException("Неправильно пронумерован type_dict словарь")
                counter = 1
                for i in self._type_list.keys():  # Переводим type_dict как при by_number = False
                    temp.update({i: type_dict[counter]})
                    counter += 1
            else:
                for i in type_dict.keys():
                    if self._type_list.get(i) == None:  # Проверка на нурмерацию таблицы при by_number = False
                        raise BaseException("В таблице нет названия колонки которая есть в type_dict словаре")
            for i in type_dict.keys():
                if not (type_dict[i] == str or type_dict[i] == int or type_dict[i] == float or type_dict[i] == bool):
                    raise BaseException("Неверный тип объекта")  # Проверка на разрешенные типы обЪектов
                if self._type_list[i] != type_dict[i]:
                    if type_dict[i] == str:  # Переводим в str
                        for j in range(0, len(self._data[i])):
                            if self._data[i][j] != None:
                                self._data[i][j] = str(self._data[i][j])
                    elif type_dict[i] == bool:  # Переводим в bool
                        for j in range(0, len(self._data[i])):
                            if self._data[i][j] != None:
                                self._data[i][j] = bool(self._data[i][j])
                    elif type_dict[i] == int:  # Переводим в int, если можно
                        for j in range(0, len(self._data[i])):
                            if self._data[i][j] != None and self._type_list[i] != str:
                                self._data[i][j] = int(self._data[i][j])
                            else:
                                self._data[i][j] = None
                    else:
                        for j in range(0, len(self._data[i])):  # Переводим в float, если можно
                            if self._data[i][j] != None and self._type_list[i] != str:
                                self._data[i][j] = float(self._data[i][j])
                            else:
                                self._data[i][j] = None
        except IndexError:
            print('Введены неверные значения!')
        except ValueError:
            print('Введены неверные значения!')
        except AttributeError:
            print('Таблица неверно записана!')
        except KeyError:
            print('Неправильно собран словарь!')

    def get_rows_by_index(self, *values, copy_table=False):
        try:
            field_names = []
            new_table = Table()
            for i in self._data:  # ПЕРЕВОДИМ ПЕРВУЮ СТРОКУ В ЛИСТ
                field_names.append(i)
                new_table._data[i] = []
            for n in values:  # ИЩЕМ ЗНАЧЕНИЯ В ТАБЛИЦЕ
                new_table._data[field_names[0]].append(n)
                v_index = self._data[field_names[0]].index(n)
                for j in self._data:  # ПРОВЕРКА НА СОВПАДЕНИЕ ТАБЛИЦЫ
                    if j == field_names[0]:
                        continue
                    new_elem = self._data[j][v_index]
                    new_table._data[j].append(new_elem)  # ЗАПОЛНЕНИЕ ТАБЛИЦЫ НОВЫМИ ЭЛЕМЕНТАМИ
            new_table._type_list = self._type_list
            return new_table
        except ValueError:
            print('Такого значения не существует')
            return

    def get_rows_by_number(self, start, stop, copy_table=False):
        try:
            field_names = []
            if start <= stop:  # ДЕЛАЕМ ПРЕОБРАЗОВАНИЯ
                if start <= 0:
                    start = 1
            else:
                print('Интвервал должен идти по возрастанию!')
                return
            start -= 1
            new_table = Table()
            for i in self._data:  # ПЕРЕВОДИМ ПЕРВУЮ СТРОКУ В ЛИСТ
                field_names.append(i)
                new_table._data[i] = []
            for j in range(start, stop):  # ПРОХОДИМСЯ ПО ВСЕМУ ИНТЕРВАЛУ
                for k in field_names:
                    temp = self._data[k][j]  # ВЫТАСКИВАЕМ ПО НОМЕРУ СТРОКИ ЭЛЕМЕНТ
                    new_table._data[k].append(temp)
            new_table._type_list = self._type_list
            return new_table
        except IndexError:
            print('Введены неверные значения!')
        except ValueError:
            print('Введены неверные значения!')
        except AttributeError:
            print('Таблица неверно записана!')


# ФУНКЦИЯ ВЫГРУЗКИ ТАБЛИЦЫ ИЗ ФАЙЛА НАЧАЛО
def load_table(*files):
    counter = 0
    table = Table()  # Храним таблицу
    for file in files:
        state_file = os.path.isfile(file)
        if not state_file:
            raise Exception("Такого файла не существует, необходимо выбрать другой.")
        file_type = re.split('\.', file)
        file_type = file_type[-1]

        try:
            dictionary = {}
            type_list = {}
            if file_type == "pickle":  # Считываем таблицу используя pickle
                with open(file, "rb") as f:
                    temp = pickle.load(f)
                    dictionary = temp._data
                    type_list = temp._type_list
            elif file_type == "csv":  # Считываем таблицу используя csv
                with open(file, "r") as f:
                    file_reader = csv.reader(f, delimiter=",")  # преобразуем файл в лист листов
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
            for i in dictionary:
                temp = dictionary[i][0]
                type_list[i] = type(temp)
            if counter == 0:
                table._type_list = type_list
                table._data = dictionary
            else:
                if table._type_list == type_list:
                    for i in type_list.keys():
                        table._data[i] += dictionary[i]
                else:
                    raise Exception("В файлах разные таблицы")

            counter += 1
        except ValueError:
            print('Неверные значения в таблице!')
    return table
