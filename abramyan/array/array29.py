"""
 Дан массив A размера N. Найти максимальный элемент из его элементов с нечетными номерами: A1, A3, A5, . . . .
"""
mas = []
n = int(input("Enter the number N: "))
for i in range(n):
    inp = int(input("Enter the number: "))
    mas.append(inp)
f = mas[0]
for i in range(0,len(mas),2):
    if mas[i]>f:
        f=mas[i]
print(f)