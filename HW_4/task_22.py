# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих 
# наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество эл-ов первого множества:  "))
n1, m1 = set(), set()
for i in range(n):
    n1.add(input("Введите первые множества:  "))
m = int(input("Введите количество эл-ов второго множества:  "))
for i in range(m):
    m1.add(input("Введите второго множества:  "))
sort_nm = sorted(n1.intersection(m1))
print(*sort_nm)