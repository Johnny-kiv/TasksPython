n = int(input())
mas = map(int,input().split(" "))
print(mas)
l=1
s=0
def rekurs(m,s):
    if len(m)<3:
        return 0 
    m1=m[0:l]
    m2=m[l:-1]
    s = s+(sum(m1)+sum(m2))*mas[l]
    print(s)
    rekurs(m1,s)
    rekurs(m2,s)
    return s
    
    
rekurs(mas,s)