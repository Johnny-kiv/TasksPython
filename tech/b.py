"""n = int(input())
for k in range(n):
    s = input()
    for i in range(len(s)):
        f = s[i]
        p = s[len(s)-(i+1)]
        print(f,p)"""
b = True
l = -1
i=0
s = "00"
sr = len(s)/2-1
while True:
    print(s)
    if i>sr and f!=p:
        break
    f = s[i]
    p = s[len(s) - i-1]
    if i>sr and f!=p:
        l=-1
        break
    elif f == p:
        l=0
        break
    else:
        i += 1
        l+=1
        s = s[i:]
print(l)