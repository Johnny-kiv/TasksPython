n = int(input())
days = input().split(",")
m = int(days[0])
for d in days:
    if int(d)>m:
        m=int(d)
if m%2==1:
    print(m)
else:
    print("-1")
