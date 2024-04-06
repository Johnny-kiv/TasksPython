"""
Даны два целых числа: A, B. Проверить истинность высказывания:
«Числа A и B имеют одинаковую четность».
"""
A = int(input("Enter the number A: "))
B = int(input("Enter the number B: "))
print("The inequality is",(A%2==1) == (B%2==1))