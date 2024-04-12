inp = open("INPUT.TXT")
f = inp.read().split("\n")
c1 = f[0].split(" ")
c2 = f[1].split(" ")
inp.close()
out = open("OUTPUT.TXT","w")
r1 = int(c1[2])
r2 = int(c2[2])
r = ((int(c1[0])-int(c2[0]))**2+(int(c1[1])-int(c2[1]))**2)**(0.5)
b = "NO"
if r1+r2>=r and r1<=r2+r and r2<=r1+r:
    b="YES"
out.write(b)
out.close()
