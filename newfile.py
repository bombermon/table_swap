data = {'No': ['1999','2','3','4'], 'Company': ['Ferrari','Lamborghini','porsche', 'BMW'],
             'Car Model': ['488 GTB', 'phantom', 'macan', 'X5']}

with open('NewFile.txt', 'w') as f:
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
