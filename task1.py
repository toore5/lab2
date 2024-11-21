# -*- coding: cp1251 -*-
from math import exp
def expression(x):
    z = exp(x) + x ** 0.5
    return z
def sum_of_digits(n):
    summa = 0
    while n > 0:
        summa += n % 10 
        n = n // 10  
    return summa
x = int(input("Введіть значення x: "))
print ("Значення виразу z =", expression(x)) 
n = int(input("Введіть число n, щоб порахувати суму його цифр: "))
while n <= 0:
    n = int(input("Число n повинно бути невід'ємним. Введіть число n ще раз: "))
print("Сума цифр числа n =", sum_of_digits(n))