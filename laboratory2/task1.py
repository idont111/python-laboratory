print("""Черниш Аліна Андріївна\nКМ-93\nЛабораторна робота№2 \nВаріант 22
Організація циклу за допомогою оператора for""")
"""Знайти суму ( ( 2*х + 1)**і/ (х - 1)))"""

import re

re_integer = re.compile("^[-+]{0,1}\d+$")
re_float = re.compile("^[-+]{0,1}\d+[.]?\d*$")

def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def int_validator(prompt):
    number = int(validator(re_integer, prompt))
    return number

def float_validator(prompt):
    number = float(validator(re_float, prompt))
    return number

i = 1
n = int_validator("Введіть натуральне число: ")
while n < 1 :
    n=int_validator("Введіть число більше за 0: ")
x = float_validator("Введіть значення числа x: ")
while x == 1 :
    x = float_validator("Введіть число більше за 1: ")
result=0
for i in range(i,n+1) :
    result += ( (2*x + 1)**i) / ( x - 1 )
    i += 1
print("Результат "+ str( result ))
print("Роботу завершено")