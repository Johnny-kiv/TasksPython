"""
Дано целое число N (> 2). Сформировать и вывести целочисленный
массив размера N, содержащий N первых элементов последовательности
чисел Фибоначчи FK:
F1 = 1, F2 = 1, FK = FK−2 + FK−1, K = 3, 4, . . . .
"""
array = [1,1]
n = int(input("Enter the number N: "))
for i in range(2,n):
    f = array[i-2]+array[i-1]
    array.append(f)
for i in array:
    print(i,end=" ")