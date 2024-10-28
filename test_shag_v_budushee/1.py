"""mas = input().split(" ")
a,c,m,x,n = int(mas[0]),int(mas[1]),int(mas[2]),int(mas[3]),int(mas[4])
s = 0
for i in range(n):
    x = (a*x+c) % m
    s+=x
s/=n
print('%.4f'%s)
"""
n = input().split(" ")
x = int(n[0])
y = int(n[1])
a = int(n[2])
b = int(n[3])
t = 0
l = 0
while x>y:
    if l == 0:
        y+=a
        l=1
    else:
        x+=b
        l=0
    t+=1
print(t)