print("Черниш Аліна Андріївна\nКМ-93\nЛабораторна робота№1 \nВаріант 22")

"""Ввести координати чотирьох точок А1 (х1, у1), А2 (x2, у2), А3 (x3, у3), А4 (х4, у4).          
Визначити, чи будуть вони вершинами паралелограма."""
import re

re_integer = re.compile("^[-+]{0,1}\d+$")


def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text


def int_validator(prompt):
    number = int(validator(re_integer, prompt))
    return number


x_1 = int_validator("Введіть абцису точки А: ")
y_1 = int_validator("Введіть ординату точки А: ")
x_2 = int_validator("Введіть абцису точки В: ")
y_2 = int_validator("Введіть ординату точки В: ")
x_3 = int_validator("Введіть абцису точки С: ")
y_3 = int_validator("Введіть ординату точки С: ")
x_4 = int_validator("Введіть абцису точки D: ")
y_4 = int_validator("Введіть ординату точки D: ")

AB = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 1 / 2
print(AB)
BC = ((x_3 - x_2) ** 2 + (y_3 - y_2) ** 2) ** 1 / 2
print(BC)
CD = ((x_4 - x_3) ** 2 + (y_4 - y_3) ** 2) ** 1 / 2
print(CD)
AD = ((x_4 - x_1) ** 2 + (y_4 - y_1) ** 2) ** 1 / 2
print(AD)
"""                                                                                              
Можна ввести координати (1,-3), (2,-1), (4,-1)                                                   
щоб одержати паралелограм                                                                        
"""
if AB == CD and BC == AD:
    print("ABCD- паралелограм")
elif AB == BC or AB == AD or CD == BC or CD == AD:
    print("ABCD не паралелограм")
else:
    print("ABCD не паралелограм")
