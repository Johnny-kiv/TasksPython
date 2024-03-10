"""
Дан массив размера N. Найти номер его последнего локального максимума (локальный максимум — это элемент, который больше любого из
своих соседей).
"""
mas = []
n = int(input("Enter the number N: "))
for i in range(n):
    inp = int(input("Enter the number: "))
    mas.append(inp)
for i in range(n):
    if mas[i]!=mas[0] and mas[i]!=mas[-1]:
        if mas[i]>mas[i+1] and mas[i]>mas[i-1]:
            print(mas.index(mas[i])+1)
            break
    if mas[i]==mas[0]:
        if mas[i]>mas[i+1]:
            print(mas.index(mas[i])+1)
            break
    if mas[i]==mas[-1]:
        if mas[i]>mas[i-1]:
            print(mas.index(mas[i])+1)   
            break