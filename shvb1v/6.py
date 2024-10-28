n = int(input())
mas1 = []
mas2 = []
for i in range(n):
    el = int(input())
    if el in mas1:
        mas2[mas1.index(el)]+=1
    else:
        mas1.append(el)
        mas2.append(1)
m = max(mas1)
for i in mas1:
    if i>0.1 * m:
        mas2.pop(mas1.index(i))
        mas1.remove(i)
m = max(mas2)
res = mas1[mas2.index(m)]
print(res)