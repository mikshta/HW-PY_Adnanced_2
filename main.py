from ast import pattern
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import re
import csv
from itertools import groupby
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

# разбиваем имена по столбцам
for element in contacts_list:
  if len(element[0].split()) > 1:
    split_name = []
    split_name = element[0].split()
    element[0] = split_name[0].strip()
    element[1] = split_name[1].strip()
    if len(split_name) >2:
      element[2] = split_name[2].strip()

for element in contacts_list:
  if len(element[1].split()) > 1:
    split_name2 = []
    split_name2 = element[1].split()
    element[1] = split_name2[0].strip()
    element[2] = split_name2[1].strip()

# преносим данные из дублированных записей
for x in range(0,len(contacts_list)):
  for y in range(0, len(contacts_list)):
    if contacts_list[x][0] == contacts_list[y][0] and contacts_list[x][1] == contacts_list[y][1]:
      for a in range(0,len(contacts_list[0])):
        if not contacts_list[x][a]:
          contacts_list[x][a] = contacts_list[y][a]

# удаляем лишние(дублированные) строки
sorted_list = sorted(contacts_list)
short_list = [el for el, l in groupby(sorted_list)]



# изменяем формат номера телефона
for i in range(1, len(short_list)-1):
  pattern1 = r"(\+7|8)\s?\(?(\d{3})\)?\-?\s?(\d{3})\-?\s?(\d{2})\-?\s?(\d{2})"
  repl = r"+7(\2)\3-\4-\5"
  short_list[i][5] = re.sub(pattern1, repl, short_list[i][5])


for i in range(1, len(short_list)-1):
    pattern2 = r"\(?доб\.?\s?(\d+)\)?"
    repl2 = r'доб.\1'
    short_list[i][5] = re.sub(pattern2, repl2, short_list[i][5])

pprint(short_list)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(short_list)