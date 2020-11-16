import csv,pickle


temp_data = {'No': ['1','2','3','4'], 'Company': ['Ferrari','Lamba'], 'Car Model': ['488 GTB','phantom']}

with open('NewFile' + '.pickle', 'wb') as f:
    pickle.dump(temp_data, f)