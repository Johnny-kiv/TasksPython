"""
Дано целое число N (> 1), а также первый член A и знаменатель D
геометрической прогрессии. Сформировать и вывести массив размера N,
содержащий N первых членов данной прогрессии:
A, A·D, A·D^2, A·D^3, . . . .
"""
n = int(input("Enter the number N: "))
a = int(input("Enter the number A: "))
d = int(input("Enter the number D: "))
arr = []
for i in range(n):
    num = a*(d**(i))
    arr.append(num)
for i in arr:
    print(i,end=" ")