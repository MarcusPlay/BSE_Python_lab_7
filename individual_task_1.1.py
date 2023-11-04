#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов, найти сумму элементов, больших 2 и меньших 20
# и кратных 8, их количество и вывести результаты на экран.

import sys


if __name__=="__main__":
    while True:
        a = list(map(int, input("Введите 10 значений через пробел: ").split()))
        if not a:
            print("Заданный список пуст", file=sys.stderr)
            exit(1)
        
        if len(a) == 10:
            break
        else:
            print("Количество элементов одномерного массива не равно 10.\n")

    sum_num = 0
    count = 0
    for num in a:
        if (num > 2) and (num < 20) and (num % 8 == 0):
            sum_num += num
            count += 1

    print(sum_num, count)

    



    

    