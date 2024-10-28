def to_12(n):
    l=0
    if n ==0:
        l=1
    else:
        while n!=0:
            s = n%12
            n=int(n/12)
            if s%4==0:
                l+=1
    return l
n = int(input())
m = int(input())
s = 0
for i in range(n):
    el = int(input())
    id = to_12(el)
    if id>=m:
        s+=1
print(s)