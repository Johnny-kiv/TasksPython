mas = []
n = int(input("Enter the number N: "))
for i in range(n):
    inp = int(input("Enter the number: "))
    mas.append(inp)
fam = []
for i in range(n):
    if mas[i]!=mas[0] and mas[i]!=mas[-1]:
        if mas[i]<mas[i+1] and mas[i]<mas[i-1]:
            fam.append(mas[i])
    if mas[i]==mas[0]:
        if mas[i]<mas[i+1]:
            fam.append(mas[i])
    if mas[i]==mas[-1]:
        if mas[i]<mas[i-1]:
            fam.append(mas[i])
f = fam[0]
for i in fam:
    if f<i:
        f = i
if f!=fam[0]:
    print(f)
else:
    print(0)