m = int(input())
n = input()
l=0
b=False
ind=0
for i in range(m):
    if int(n[i])%2==0:
        b=True
        ind = i
    elif b!=True:
        b= False
    l+=int(n[i])
if l%3!=0 or b==False:
    res=-1
else:
    res = len(n[ind+1:])
print(res)