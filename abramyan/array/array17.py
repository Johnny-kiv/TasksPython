"""Дан массив A размера N. Вывести его элементы в следующем порядке:
A1, A2, AN , AN−1, A3, A4, AN−2, AN−3, . . . .
"""
mas = []
n = int(input("Введите число N: "))
for i in range(n):
    inp = input("Введите что-нибудь: ")
    mas.append(inp)
l = len(mas)
for i in range(0,l,2):
    print(mas[i],mas[i+1],mas[i],end=" ")