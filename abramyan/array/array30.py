"""
Дан массив размера N. Найти номера тех элементов массива, которые
больше своего правого соседа, и количество таких элементов. Найденные
номера выводить в порядке их возрастания.
"""
mas = []
n = int(input("Enter the number N: "))
for i in range(n):
    inp = int(input("Enter the number: "))
    mas.append(inp)
f = []
for i in range(len(mas)):
    if mas[i]!=mas[-1]:
        o = mas[i]
        t = mas[i+1]
        if mas[i]>mas[i+1]:
            print(i+1,end=" ")