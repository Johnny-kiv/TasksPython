"""
Даны целые числа N (> 2), A и B. Сформировать и вывести целочисленный массив размера N, первый элемент которого равен A, второй
равен B, а каждый последующий элемент равен сумме всех предыдущих
"""
array = []
n = int(input("Enter the number N: "))
a = int(input("Enter the number A: "))
b = int(input("Enter the number B: "))
array.append(a)
array.append(b)
for i in range(2,n):
    f = array[i-2]+array[i-1]
    array.append(f)
for i in array:
    print(i,end=" ")