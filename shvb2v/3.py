x = int(input())
y = int(input())
a = int(input())
l=0
while a!=0:
    if not (x<=a and a<=y):
        l+=1
    a = int(input())
print(l)