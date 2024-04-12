inp = open("INPUT.TXT")
f = inp.read().split(" ")
n = int(f[0])
m = int(f[1])
d = [1]+[0]*n*m
print(d)
inp.close()
out = open("OUTPUT.TXT","w")
for i in range(m):
    for j in range(1,n+1):
        d[i+j]+=d[i]
        print(d)
ma = d[0]
for i in d:
   if ma < i:
       ma = i
out.write(str(ma))
out.close()