n = int(input())
s1 = 0
s2 = 0
for i in range(n):
    el = int(input())
    if el%2==0:
        s1+=el
    else:
        s2+=el
if s1%3==0:
    s1 *=2
else:
    s1 *=3
if s2%3==0:
    s2 *=2
else:
    s2 *=3
res = s1+s2
print(res)
