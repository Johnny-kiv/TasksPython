"""
Дан массив размера N и целые числа K и L (1 < K ≤ L ≤ N). Найти
сумму всех элементов массива, кроме элементов с номерами от K до L
включительно.
"""
mas = []
sum = 0
n = int(input("Enter the number N: "))
k = int(input("Enter the number K: "))
l = int(input("Enter the number L: "))
for i in range(n):
    inp = int(input("Enter the number: "))
    mas.append(inp)
for i in range(0,k-1):
    sum+=mas[i]
for i in range(l,n):
    sum+=mas[i]
print(sum)