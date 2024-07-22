inp = open("INPUT.TXT")
n = int(inp.readline())
inp.close()
out = open("OUTPUT.TXT","w")
l = 1
res = 1
b = False 
for i in range(2,int(n**(0.5))):
    if n % i==0:
        b = True
        break
if b:
    while True:
        mas = list(str(l))
        pr = 1
        for i in mas:
            pr*=int(i)
        if pr==n:
            res = n
            break
else:
    out.write("-1")
out.close()