"""
Дан массив A размера N. Вывести его элементы в следующем порядке:
A1, A2, AN , AN−1, A3, A4, AN−2, AN−3, . . . .
"""
mas = []
n = int(input("Enter the number N: "))
for i in range(n):
    inp = input("Enter something: ")
    mas.append(inp)
l = len(mas)
for i in range(0,l,2):
    print(mas[i],mas[i+1],mas[-i-1],mas[-i-2],end=" ")