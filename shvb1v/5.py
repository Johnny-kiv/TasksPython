n = int(input())
m=[]
for i in range(1,n+1):
    s = 0
    for y in range(i,n+1):
        s=s+y
        if s == n:
            m.append(s)
        elif s>n:
            break
print(len(m))