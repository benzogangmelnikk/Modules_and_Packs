# -*- coding: utf-8 -*-
from pprint import pprint

import district.central_street.house1.room1 as central_h1_r1
import district.central_street.house1.room2 as central_h1_r2
import district.central_street.house2.room1 as central_h2_r1
import district.central_street.house2.room2 as central_h2_r2
import district.soviet_street.house1.room1 as soviet_h1_r1
import district.soviet_street.house1.room2 as soviet_h1_r2
import district.soviet_street.house2.room1 as soviet_h2_r1
import district.soviet_street.house2.room2 as soviet_h2_r2

all_folks = []

def list_create(module_name):
	for new_folk in module_name.folks:
		all_folks.append(new_folk)


list_create(central_h1_r1)
list_create(central_h1_r2)
list_create(central_h2_r1)
list_create(central_h2_r2)
list_create(soviet_h1_r1)
list_create(soviet_h1_r2)
list_create(soviet_h2_r1)
list_create(soviet_h2_r2)

all_folks_str = ", ".join(all_folks)
pprint("На районе живут: " + all_folks_str)

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join





