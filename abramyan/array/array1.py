"""
 Дано целое число N (> 0). Сформировать и вывести целочисленный
массив размера N, содержащий N первых положительных нечетных чисел:
1, 3, 5, . . . .
"""
n = int(input("Enter the number n: "))
arr = []
for i in range(1,n):
    if i%2==1:
        arr.append(i)
for i in arr:
    print(i,end=" ")