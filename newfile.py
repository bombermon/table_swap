temp_data = {'No': ['1999','2','3','4'], 'Company': ['Ferrari','Lamba'], 'Car Model': ['488 GTB','phantom']}

def print_table(data):
    len_of_col = {}
    max_l = 0
    for i in data:              # ПЕРЕБОР СЛОВАРЯ ПО ВСЕМ СЛОВАМ И ЗНАЧЕНИЯМ
        if len(i) > max_l:      # НАХОЖДЕНИЕ САМОГО ДЛИННОГО СЛОВА
            max_l = len(i)
        for j in data[i]:
            if len(j) > max_l:
                max_l = len(j)
        len_of_col[i] = max_l

    print(len_of_col)

    field_names_len = {}
    for i in len_of_col:        # ФОРМИРОВАНИЕ РОВНЫХ СТОЛБЦОВ
        temp_key = i
        if len(i) < len_of_col[i]:
            while len(i) < len_of_col[temp_key]:
                i = i + ' '
        print(i + '|', end="")
        field_names_len[i] = len_of_col[temp_key]




print_table(temp_data)