def to16(n):
    res = [0]
    while n>15:
        k= n//16
        o = n%16
        n=k
        res.append(o)
    res[0]=n
    return res 
n16 = list(input())
def usl(i):
    if i=="a":
        i=10
    elif i=="b":
        i=11
    elif i=="c":
        i=12
    elif i=="d":
        i=13
    elif i=="e":
        i=14
    elif i=="f":
        i=15
    else:
        i=int(i)
    return i
def summ(n):
    l=0
    for i in range(len(n)):

        n[i]=usl(n[i])
        l+=n16[i]
    return l
s = summ(n16)
while len(str(s))>1:
    s=sum(to16(s))
print(s)