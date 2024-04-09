inp = open("INPUT.TXT")
f = inp.read().split(" ")
inp.close()
out = open("OUTPUT.TXT","w")
one = int(f[0])
for i in f:
    if int(i)>one:
        one = int(i)
out.write(str(one))
out.close()