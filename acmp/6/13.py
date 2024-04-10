inp = open("INPUT.TXT")
f = inp.read().split(" ")
inp.close()
out = open("OUTPUT.TXT","w")
b = 0
k = 0
for i in range(4):
    if f[0][i]==f[1][i]:
        b+=1
    elif f[1][i] in f[0]:
        k+=1
res = (str(b)+" "+str(k))
out.write(res)
out.close()
