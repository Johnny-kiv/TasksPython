alph = "ABCDEFGH"
ns = "12345678"
inp = open("INPUT.TXT")
f = inp.read()

inp.close()
out = open("OUTPUT.TXT","w")
if len(f)==5:
    t = f.split("-")
    if f[0] in alph and f[1] in ns and f[3] in alph and f[4] in ns:
        fir = t[0]
        sec = t[1]
        b = None
        if alph[alph.index(fir[0])-1]+str(int(fir[1])+2) == sec or alph[alph.index(fir[0])+1]+str(int(fir[1])+2) == sec or alph[alph.index(fir[0])+1]+str(int(fir[1])-2) == sec or alph[alph.index(fir[0])-1]+str(int(fir[1])-2):
            b = "YES"
        else:
            b="NO"
    else:
        b = "ERROR"
else:
    b = "ERROR"
out.write(b)
out.close()
