"""
 Дан массив ненулевых целых чисел размера N. Проверить, чередуются ли в нем положительные и отрицательные числа. Если чередуются,
то вывести 0, если нет, то вывести порядковый номер первого элемента,
нарушающего закономерность.
"""
mas = []
n = int(input("Enter the number N: "))
for i in range(n):
    inp = int(input("Enter the number: "))
    mas.append(inp)
res = 0
for i in range(0,n):
    if i+1<=len(mas)-1:
        zn1=mas[i]>0 
        zn2=mas[i+1]>0 
        if zn1==zn2:
            res=i+1
print(res)