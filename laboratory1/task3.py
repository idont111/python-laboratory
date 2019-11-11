print("""Черниш Аліна Андріївна\nКМ-93\nЛабораторна робота№1 \nВаріант 22
F(x)={9-x, якщо х > 1.1,
      sin(3x)/(x**4+1), якщо х < -1.1}\n""")

import re
import math

re_float = re.compile("^[-+]{0,1}\d+[.]?\d*$")
def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text


def float_validator(prompt):
    number = float(validator(re_float, prompt))
    return number

x = float_validator("Введіть будь-яке число: ")

if x>1.1:
    result = str(9-x)
elif x<-1.1:
    result = str(math.sin(3*x)/(x**4 +1))
else:
    result = str("не існує")

print("Результат " + result)
