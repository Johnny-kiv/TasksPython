inp = open("INPUT.TXT")
line = inp.read()
inp.close()
out = open("OUTPUT.TXT","w")
mas = ["<--<<",">>-->"]
b = mas[0] in line or mas[1] in line
out.write(str(b))
out.close()
