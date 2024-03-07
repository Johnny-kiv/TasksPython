"""
 Дан целочисленный массив A размера 10. Вывести порядковый номер
последнего из тех его элементов AK, которые удовлетворяют двойному
неравенству A1 < AK < A10. Если таких элементов нет, то вывести 0.
"""
mas = []
for i in range(10):
    inp = int(input("Enter the number: "))
    mas.append(inp)
for i in range(len(mas)):
    if mas[0]<mas[i]<mas[-1]:
        print(i+1,end=" ")
    else:
        print(0,end=" ")