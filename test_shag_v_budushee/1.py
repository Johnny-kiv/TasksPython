mas = input().split(" ")
a,c,m,x,n = int(mas[0]),int(mas[1]),int(mas[2]),int(mas[3]),int(mas[4])
s = 0
for i in range(n):
    x = (a*x+c) % m
    s+=x
s/=n
print('%.4f'%s)