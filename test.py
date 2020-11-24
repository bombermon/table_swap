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
        data = self._data
        len_of_col = {}
        full_len = 0
        max_l = 0
        for i in data:  # ПЕРЕБОР СЛОВАРЯ ПО ВСЕМ СЛОВАМ И ЗНАЧЕНИЯМ
            if len(i) > max_l:  # НАХОЖДЕНИЕ САМОГО ДЛИННОГО СЛОВА
                max_l = len(i)
            for j in data[i]:
                if len(j) > max_l:
                    max_l = len(j)
            len_of_col[i] = max_l
            full_len += max_l
        print('|', end='')
        for j in range(full_len + 2):
            print('-', end='')
        print('|')
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
                print('|', end='')
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
            for j in range(full_len+2):
                print('-', end='')
            print('|')
            return

    # ФУНКЦИЯ ВЫВОДА ТАБЛИЦЫ В КОНСОЛЬ НАЧАЛО

    # ФУНКЦИЯ СОХРАНЕНИЯ ТАБЛИЦЫ В НОВЫЙ ФАЙЛ НАЧАЛО
    def save_table(self, name, file_type='csv'):
        data = self._data

        if file_type == 'csv':  # ПРОВЕРЯЕМ ТИП ФАЙЛА
            temp_table = []
            field_names = data.keys()
            num_of_columns = 0
            for i in field_names:
                num_of_columns = max(num_of_columns, len(data[i]))
            for i in range(0, num_of_columns):  # ПРЕОБРАЗУЕМ НАШЕ ПРЕДСТАВЛЕНИЕ В ПРЕДСТАВЛЕНИЕ УДОБНОЕ DictWriter CSV
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
                pickle.dump(data, f)  # ЗАПИСЫВАЕМ НАШ СЛОВАРЬ В ФАЙЛ .pickle

        elif file_type == 'txt':  # ЗАПИСЬ В ФАЙЛ .txt ТАКАЯ ЖЕ КАК ВЫВОД ТАБЛИЦЫ В КОНСОЛЬ
            with open(name + '.txt', 'w') as f:
                len_of_col = {}  # СЛОВАРЬ ДЛЯ ХРАНЕНИЯ ДЛИНЫ СТОЛБЦОВ
                max_l = 0
                full_len = 0
                for i in data:  # ПЕРЕБОР СЛОВАРЯ ПО ВСЕМ СЛОВАМ И ЗНАЧЕНИЯМ
                    if len(i) > max_l:  # НАХОЖДЕНИЕ САМОГО ДЛИННОГО СЛОВА
                        max_l = len(i)
                    for j in data[i]:
                        if len(j) > max_l:
                            max_l = len(j)
                    len_of_col[i] = max_l  # ЗАПОЛНЕНИЯ СЛОВАРЯ МАКСИМАЛЬНЫМИ ДЛИНАМИ
                    full_len += max_l
                print('|', file=f, end='')
                for j in range(full_len + 2):
                    print('-', file=f, end='')
                print('|', file=f)
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
                        print('|', file=f, end='')
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
                        for j in range(full_len + 2):
                            print('-', file=f, end='')
                        print('|', file=f)
                        break

    # ФУНКЦИЯ СОХРАНЕНИЯ ТАБЛИЦЫ В НОВЫЙ ФАЙЛ КОНЕЦ

    def get_column_types(self, by_number=True):  # Получаем словарь с типами столбцов
        if by_number:  # если надо нумеруем от одного
            type_list = {}
            counter = 1
            for i in self._type_list:
                type_list.update({counter: self._type_list[i]})
                counter += 1
            return type_list
        else:  # иначе по названию колонки
            return self._type_list

    def get_rows_by_index(self):  # не могу записать в другой файл
        self.index = str(input('Введите название столбца: '))
        self.dict = str([])
        with open("table.csv", mode='r', newline='') as csv_file:
            self.reader = csv.DictReader(csv_file, delimiter=";")
            for row in self.reader:
                self.output_raw = row[self.index]
                print(self.output_raw)

        def get_rows_by_number(self):  # ещё не сохраняет в другой файл и тд, нужно дополнить по условиям
            with open('table.csv') as csv_file:
                self.csv_reader = list(csv.reader(csv_file))
                self.number = int(input('Введите номер первой строчки: '))
                self.number_2 = int(input('Введите номер второй строчки: '))
                print(self.csv_reader[self.number - 1:self.number_2])


# ФУНКЦИЯ ВЫГРУЗКИ ТАБЛИЦЫ ИЗ ФАЙЛА НАЧАЛО
def load_table(file):
    table = Table()  # Храним таблицу
    state_file = os.path.isfile(file)

    if not state_file:
        raise Exception("Такого файла не существует, необходимо выбрать другой.")
    file_type = re.split('\.', file)
    file_type = file_type[-1]

    try:
        if file_type == "pickle":  # Считываем таблицу используя pickle
            with open(file, "rb") as f:
                table = pickle.load(f)
        elif file_type == "csv":  # Считываем таблицу используя csv
            dictionary = {}
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
            table._data = dictionary
            type_list = {}
            for i in dictionary:
                temp = dictionary[i][0]
                type_list[i] = type(temp)
            table._type_list = type_list
        return table
    except ValueError:
        print('Неверные значения в таблице!')


vova = '1'
table = load_table("NewFile.csv")
table.set_value(vova)
vova = table.get_value(column=0)
print('get value = %s' % vova)
table.print_table()
table.save_table('NewTable1', file_type='txt')
