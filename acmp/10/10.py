inp = open("INPUT.TXT")
f = inp.readline().split(" ")
inp.close()
out = open("OUTPUT.TXT","w")
a = int(f[0])
b = int(f[1])
c = int(f[2])
d = int(f[3])
res = ""
for x in range(-100,101):
    if a*(x**3)+b*(x**2)+c*x+d==0:
        res+=str(x)+" "
out.write(res)
out.close()