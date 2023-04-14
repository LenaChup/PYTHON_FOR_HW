# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

# 1 способ:
n = int(input("Введите трехзначное число:"))
summa = 0
while n > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
print(summa)

# 2 способ:
# list = [1, 2, 3]
# print (sum (list))

# 3 способ:
# a = [1,2,3]
# sum = 0
# i = 0
# while i < len(a):
#     sum = sum + a[i]
#     i += 1
# print (sum)