"""
Дан массив ненулевых целых чисел размера N. Проверить, образуют
ли его элементы геометрическую прогрессию (см. задание Array4). Если
образуют, то вывести знаменатель прогрессии, если нет — вывести 0.
"""
mas = []
n = int(input("Enter the number N: "))
for i in range(n):
    inp = int(input("Enter the number: "))
    mas.append(inp)
a = mas[0]
d = mas[1]-a
for i in range(0,n):
    if not a*d**i==mas[i]:
        d = 0
        break
print(d)