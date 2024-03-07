"""
Дан массив A ненулевых целых чисел размера 10. Вывести значение
первого из тех его элементов AK, которые удовлетворяют неравенству
AK < A10. Если таких элементов нет, то вывести 0.
"""
mas = []
for i in range(10):
    inp = int(input("Enter the number: "))
    mas.append(inp)
for i in mas:
    if i<mas[-1]:
        print(i,end=" ")
    else:
        print(0,end=" ")