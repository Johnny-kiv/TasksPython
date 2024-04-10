inp = open("INPUT.TXT")
f = inp.read().split(" ")
inp.close()
out=open("OUTPUT.TXT","w")
a = int(f[0])
b = int(f[1])
x,y = a,b
while x!=y:
    if x>y:
        x = x-y
    else:
        y = y-x
c = int(a*b/x)
out.write(str(c))
out.close()