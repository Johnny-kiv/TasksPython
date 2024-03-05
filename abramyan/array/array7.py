"""
 Дан массив размера N. Вывести его элементы в обратном порядке.
"""
mas = []
n = int(input("Enter the number N: "))
for i in range(n):
    inp = input("Enter something: ")
    mas.append(inp)
for i in range(n-1,-1,-1):
    print(mas[i],end=" ")