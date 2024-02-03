i = list(input())
mas = []
for ind in range(len(i)-1,-1,-1):
    mas.append(list(i)[ind])
print("".join(mas))