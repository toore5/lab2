# -*- coding: cp1251 -*-
from mod import sum_of_digits
n = int(input("Введіть число n, щоб порахувати суму його цифр: "))
while n <= 0:
    n = int(input("Число n повинно бути невід'ємним. Введіть число n ще раз: "))
print("Сума цифр числа n =", sum_of_digits(n))