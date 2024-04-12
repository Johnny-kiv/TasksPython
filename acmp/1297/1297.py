inp = open("INPUT.TXT")
f = inp.read().split(" ")
m = int(f[0])
n = int(f[1])
inp.close()
out = open("OUTPUT.TXT","w")
p = 0
for i1 in range(m,n+1):
    if m%i1==0:
        p+=1
    if p==2:
        out.write(str(i1)+"\n")
if p == 0:
    out.write("Absent")
out.close()
