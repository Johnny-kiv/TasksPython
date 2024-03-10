"""
Дан массив размера N. Найти номера тех элементов массива, которые
больше своего левого соседа, и количество таких элементов. Найденные
номера выводить в порядке их убывания.
"""
mas = []
n = int(input("Enter the number N: "))
for i in range(n):
    inp = int(input("Enter the number: "))
    mas.append(inp)
for i in range(n):
    if mas[i]!=mas[0] and mas[i]!=mas[-1]:
        if mas[i]<mas[i+1] and mas[i]<mas[i-1]:
            print(i+1)
            break
    if mas[i]==mas[0]:
        if mas[i]<mas[i+1]:
            print(i+1)
            break
    if mas[i]==mas[-1]:
        if mas[i]<mas[i-1]:
            print(i+1)   
            break