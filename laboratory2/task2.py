print("""Черниш Аліна Андріївна\nКМ-93\nЛабораторна робота№2 \nВаріант 22
Організація циклу за допомогою оператора while""")
"""22) Дано число A(>1). 
Вивести найменше із цілих чисел K, для яких сума 1+1/2+...+1/K буде більше A,
і саму цю суму"""
from validators.validators_library import validator
from validators.validators_library import re_float


A=float(validator(re_float,"Введіть число більше за 1: "))
while A<=1:
    A=float(validator(re_float,"Введіть правильне число: "))
K = 1
sum = 1
while sum <= A:
    K += 1
    sum += 1 / K

print("Отримано cуму: "+ str(sum))
print("Отримано K: " + str(K))