import csv
import pickle
import re

class Table:
    __data = {'No': ['1999', '2', '3', '4'], 'Company': ['Ferrari', 'Lamborghini', 'porsche', 'BMW'],
              'Car Model': ['488 GTB', 'phantom', 'macan', 'X5']}
    __type_list = {'No': [float, int, bool, str], 'Company': [float, int, bool, str],
              'Car Model': [float, int, bool, str]}


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

    def get_column_types(self, by_number = True):
        if by_number:
            type_list = {}
            counter = 1
            for i in self.__type_list:
                type_list.update({counter : self.__type_list[i]})
                counter += 1
            return type_list
        else:
            return self.__type_list


