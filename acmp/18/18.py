inp = open("INPUT.TXT")
f = inp.read()
inp.close()
out=open("OUTPUT.TXT","w")
a = int(f)
c = 1
for i in range(1,a+1):
    c = i * c
out.write(str(c))
out.close()