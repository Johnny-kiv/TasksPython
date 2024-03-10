"""
 Дан массив A размера N. Найти минимальный элемент из его элементов с четными номерами: A2, A4, A6, . . . .
"""
mas = []
n = int(input("Enter the number N: "))
for i in range(n):
    inp = int(input("Enter the number: "))
    mas.append(inp)
f = mas[1]
for i in range(1,len(mas),2):
    if mas[i]<f:
        f=mas[i]
print(f)