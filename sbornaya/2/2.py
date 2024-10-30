n = input()
k = int(input())
p = int(input())
s = 0
m = 1
res = 0
for j in range(4):
    for i in range(k):
        num = n*m
        s +=int(num)
        m+=1
    if s>=p:
        res = "1"
        break
if res!="1":
    res = "0"
print(res)