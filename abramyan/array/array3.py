"""
Дано целое число N (> 1), а также первый член A и разность D арифметической прогрессии. Сформировать и вывести массив размера N, содержащий N первых членов данной прогрессии:
A, A + D, A + 2·D, A + 3·D, . . . .
"""
n = int(input("Enter the number N: "))
a = int(input("Enter the number A: "))
d = int(input("Enter the number D: "))
arr = []
for i in range(n):
    num = a+d*i
    arr.append(num)
for i in arr:
    print(i,end=" ")