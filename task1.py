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
x = int(input("������ �������� x: "))
print ("�������� ������ z =", expression(x)) 
n = int(input("������ ����� n, ��� ���������� ���� ���� ����: "))
while n <= 0:
    n = int(input("����� n ������� ���� ����'�����. ������ ����� n �� ���: "))
print("���� ���� ����� n =", sum_of_digits(n))