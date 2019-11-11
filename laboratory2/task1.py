print("""Черниш Аліна Андріївна\nКМ-93\nЛабораторна робота№2 \nВаріант 22
Організація циклу за допомогою оператора for""")
"""Знайти суму ( ( 2*х + 1)**і/ (х - 1)))"""

from validators.validators_library import validator
from validators.validators_library import re_float
from validators.validators_library import re_integer

i = 1
n = int(validator(re_integer,"Введіть натуральне число: "))
while n < 1 :
    n = int(validator(re_integer,"Введіть число більше за 0: "))
x = float(validator(re_float,"Введіть значення числа x: "))
while x == 1 :
    x = float(validator(re_float,"Введіть число більше за 1: "))
result=0
for i in range(i,n+1) :
    result += ( (2*x + 1)**i) / ( x - 1 )
    i += 1
print("Результат "+ str( result ))
print("Роботу завершено")