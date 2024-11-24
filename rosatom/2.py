n = int(input())
mas = map(int(),input().split(" "))
l=1
s=0
def rekurs(m):
    if len(m)<3:
        return 0 
    m1=m[0:l]
    m2=m[l:-1]
    s = s+(sum(m1)+sum(m2))*mas[l]
    
    
