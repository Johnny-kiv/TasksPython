"""
Даны два целых числа: A, B. Проверить истинность высказывания: «Ровно одно из чисел A и B нечетное».
"""
A = int(input("Enter the number A: "))
B = int(input("Enter the number B: "))
print("The inequality is",A%2==1 or B%2==1)