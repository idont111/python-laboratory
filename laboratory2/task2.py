print("""Черниш Аліна Андріївна\nКМ-93\nЛабораторна робота№2 \nВаріант 22
Організація циклу за допомогою оператора while""")
"""22) Дано число A(>1). 
Вивести найменше із цілих чисел K, для яких сума 1+1/2+...+1/K буде більше A,
і саму цю суму"""
import re

re_float = re.compile("^[-+]{0,1}\d+[.]?\d*$")

def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def float_validator(prompt):
    number = float(validator(re_float, prompt))
    return number

A=float_validator("Введіть число більше за 1: ")
while A<=1:
    A=float_validator("Введіть правильне число: ")
K = 1
sum = 1
while sum <= A:
    K += 1
    sum += 1 / K

print("Отримано cуму: "+ str(sum))
print("Отримано K: " + str(K))