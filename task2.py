# -*- coding: cp1251 -*-
from mod import sum_of_digits
n = int(input("������ ����� n, ��� ���������� ���� ���� ����: "))
while n <= 0:
    n = int(input("����� n ������� ���� ����'�����. ������ ����� n �� ���: "))
print("���� ���� ����� n =", sum_of_digits(n))