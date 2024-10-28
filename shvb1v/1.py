i = input().split(" ")
k = int(i[0])
m = int(i[1])
t = int(i[2])
x = int(i[3])
d = m-x
l = 0
n = 0
s = 0
if 7*k<t:
    print(-1)
else:
    while s<d:
        l+=1
        n+=1
        s+=k
        if l==7:
            l=0
            s-=t
    print(n)