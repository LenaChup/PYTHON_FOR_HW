# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые –
# гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть
import random
n, o, g = int(input("Введите число: ")), 0, 0
for i in range(n):
    a = [random.randint(0, 1)]
    print(*a, end=" ")

    for i in range(len(a)):
        if a[i] == 0:
            o += 1
        else:
            g += 1
if o < g:
    print('\n'f'нужно перевернуть {o} орлов')
elif g < o:
    print('\n'f'нужно перевернуть {g} гербов')
elif o == g:
    print('\n'f'переверните {o} орлов или {g} гербов')

# 2 способ
# import random
# n = int(input('введите число монеток:  '))
# Orel = 0
# Resh = 0
# coin = 0
# for i in range(n):
#    coin = random.randint(0, 1)
#    print(coin)
#    if coin == 0:
#       Orel += 1
#    elif coin == 1:
#       Resh += 1

# print(f'Орел - {Orel}, Решка - {Resh}')
      
# if Orel < Resh:
#    print(f'{Orel} - монетки нужно перевернуть')
# elif Orel > Resh:
#    print(f'{Resh} - монетки нужно перевернуть')
# elif Orel == Resh:
#    print(f'Количество монет равно, можно перевернуть любую из монет {Orel} раз')