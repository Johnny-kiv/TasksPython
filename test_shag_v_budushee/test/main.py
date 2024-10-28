n = input()
k = int(input())
p = int(input())
s = 0
for i in range(k):
    num = n*(i+1)
    s +=int(num)
if s>=p:
    print("1")
else:
    print("0")