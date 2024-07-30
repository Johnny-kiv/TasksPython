inp = open("INPUT.TXT")
n = int(inp.readline())
inp.close()
out = open("OUTPUT.TXT","w")
l = 1
b = False 
for i in range(2,int(n**(0.5)+1)):
    if n % i==0:
        b = True
        break
if b:
    while True:
        mas = list(str(l))
        print(mas)
        pr = 1
        for i in mas:
            pr*=int(i)
        if pr==n:
            break
        l+=1
else:
    l=-1
out.write(str(l))
out.close()