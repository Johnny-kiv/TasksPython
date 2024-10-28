"""e = "01234567"
inp = input()
res = 'YES'
for i in inp:
    if not i in e:
        res = 'NO'
        break
if res=="YES":
    if int(inp)%7!=0:
        res='NO'
print(res)
"""
i1 = input().split(" ")
i2 = input().split(" ")
r1 = range(int(i2[0]),int(i2[1]))
a = i1[0]
b = i2[1]
s1 = int(a[0])+int(a[1])+int(a[2])
s2 = int(b[0])+int(b[1])+int(b[2])
mas1 = []
mas2 = []
for i in r1:
    n = str(i)
    n = n[1:]
    if n[0]=="0":
        n = n[1:]
    n = int(n)    
    if n==s1 and int(a)<i and i<int(b):
        mas1.append(i)
        mas2.append("L")
    elif n==s2 and int(a)<i and i<int(b):
        mas1.append(i)
        mas2.append("R")
if mas2!=[]:
    res1 = min(mas1)
    res = mas2[mas1.index(res1)]+str(res1)
    
else:
    res = 0
print(res)