def to14(n):
    res = [0]
    while n>13:
        k= n//14
        o = n%14
        n=k
        res.append(o)
    res[0]=n
    return res

n = int(input())
m = int(input())
l=0
for i in range(n):
    inp = int(input())
    mas = to14(inp)
    s = 0
    for i in mas:
        if i%4==0:
            s+=1
    if m<=s:
        l+=1
print(l)