n = int(input())
m=0
for i in range(2,n+1,2):
    s = 0
    for y in range(i,n+1,2):
        s+=y
        if s == n:
            m+=1
        elif s>n:
            break
print(m)