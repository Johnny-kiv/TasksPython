inp = open("INPUT.TXT")
f = int(inp.read())
inp.close()
out = open("OUTPUT.TXT","w")
n = 0
for i in range(1,f+1):
    if f%i == 0:
        n+=i
out.write(str(n))
out.close()
