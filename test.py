import csv
import pickle
import re

class Table:
    __data = {'No': ['1999', '2', '3', '4'], 'Company': ['Ferrari', 'Lamborghini', 'porsche', 'BMW'],
              'Car Model': ['488 GTB', 'phantom', 'macan', 'X5']}
    __type_list = {'No': str, 'Company': str,
              'Car Model': str}

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
                for j in typer[field_names[column]]:
                    if type(k) == j:
                        flag = True
                if flag == False:
                    print('Оишбка! Вы ввели значения, не подходящие данному столбцу(', typer[field_names[column]], ')')
                    return

            data[field_names[column]] = values
        except IndexError:
            print('Ошибка: номер столбца выбран неверно!')

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

    def save_table(self, type='csv'):
        data = self.
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
