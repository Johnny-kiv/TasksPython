"""
Дан массив размера N и целые числа K и L (1 ≤ K ≤ L ≤ N). Найти
сумму элементов массива с номерами от K до L включительно
"""
mas = []
n = int(input("Enter the number N: "))
k = int(input("Enter the number K: "))
l = int(input("Enter the number L: "))
for i in range(n):
    inp = input("Enter something: ")
    mas.append(inp)
for i in range(k-1,l):
    print(mas[i],end=" ")