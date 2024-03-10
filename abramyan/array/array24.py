"""
Дан целочисленный массив размера N, не содержащий одинаковых
чисел. Проверить, образуют ли его элементы арифметическую прогрес-
46 М. Э. Абрамян. Электронный задачник Programming Taskbook 4.4
сию (см. задание Array3). Если образуют, то вывести разность прогрессии,
если нет — вывести 0.
"""
mas = []
n = int(input("Enter the number N: "))
for i in range(n):
    inp = int(input("Enter the number: "))
    mas.append(inp)
a = mas[0]
d = mas[1]-a
for i in range(0,n):
    if not a+i*d==mas[i]:
        d = 0
        break
print(d)