import re
name = 'Priv.et.txt'
namelist = re.split('\.', name)
file_type = namelist[-1]
namelist.pop(-1)
name = ''
for z in namelist:
    name += z
    name += '.'
name = name[:-1]
print(name)