inp = open("INPUT.TXT")
f = inp.read().split(" ")
inp.close()
out = open("OUTPUT.TXT","w")
if int(f[0])*int(f[1])==int(f[2]):
    out.write("YES")
else:
    out.write("NO")
out.close()