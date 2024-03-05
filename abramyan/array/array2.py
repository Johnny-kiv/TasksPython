"""
Дано целое число N (> 0). Сформировать и вывести целочисленный
массив размера N, содержащий степени двойки от первой до N-й: 2, 4,
8, 16, . . . .
"""
n = int(input("Enter the number N: "))
arr = []
for i in range(1,n+1):
    num = 2**(i)
    arr.append(num)
for i in arr:
    print(i,end=" ")