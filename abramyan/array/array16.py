""" 
Дан массив A размера N. Вывести его элементы в следующем порядке:
A1, AN , A2, AN−1, A3, AN−2, . . . .
"""
mas = []
n = int(input("Введите число N: "))
for i in range(n):
    inp = input("Введите что-нибудь: ")
    mas.append(inp)
l = len(mas)
for i in range(l):
    print(mas[i],mas[-i-1],end=" ")
