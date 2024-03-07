""" 
Дан массив A размера N. Вывести его элементы в следующем порядке:
A1, AN , A2, AN−1, A3, AN−2, . . . .
"""
mas = []
n = int(input("Enter the number N: "))
for i in range(n):
    inp = input("Enter something: ")
    mas.append(inp)
l = len(mas)
for i in range(l):
    print(mas[i],mas[-i-1],end=" ")
