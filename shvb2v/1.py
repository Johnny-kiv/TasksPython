st = input().split(" ")
p = int(st[0])
m = int(st[1])
k = int(st[2])
x = int(st[3])
z = int(st[4])
s = x+k-m
d = 0
n = 0
if p+m>=k*7:
    res=-1
else:
    while s<z:
        d+=1
        s+=k
        if d==6:
            s-=p
        if d==7:
            s-=m
            d=0
            n+=1
        
    res = n*7+d+1
print(res)