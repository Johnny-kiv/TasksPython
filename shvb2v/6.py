n = int(input())
mas = []
m = int(input())
mas.append(m)
for i in range(n-1):
    inp = int(input())
    if m<inp:
        m=inp
    if not inp in mas:
        mas.append(inp)
l=0
for i in mas:
    if m/4 > i:
        l+=1
print(l)