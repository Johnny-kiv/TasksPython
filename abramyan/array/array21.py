"""
Дан массив размера N и целые числа K и L (1 ≤ K ≤ L ≤ N).
Найти среднее арифметическое элементов массива с номерами от K до L
включительно
"""
mas = []
sum = 0
n = int(input("Enter the number N: "))
k = int(input("Enter the number K: "))
l = int(input("Enter the number L: "))
kol=0
for i in range(n):
    inp = int(input("Enter the number: "))
    mas.append(inp)
for i in range(k-1,l):
    sum+=mas[i]
    kol+=1
print(sum/kol)