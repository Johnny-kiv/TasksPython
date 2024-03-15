"""
Дан целочисленный массив размера N. Проверить, чередуются ли в
нем четные и нечетные числа. Если чередуются, то вывести 0, если нет,
то вывести порядковый номер первого элемента, нарушающего закономерность.
"""
mas = []
n = int(input("Enter the number N: "))
for i in range(n):
    inp = int(input("Enter the number: "))
    mas.append(inp)
res = 0
for i in range(0,n):
    if i+1<=len(mas)-1:
        zn1=mas[i]%2==0
        zn2=mas[i+1]%2==0
        if zn1==zn2:
            res=i+1
print(res)
