f = open("input.txt")
sdvig = int(f.readline())
text = f.read()
znakprep = "!\"'?,.:;()\n\t "
letter = "АБВГДЕЁЖЗИЙКЛМНОПРСТУХФЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстухфцчшщъыьэюя"
l = 0
res = ''
for i in text:
    if not i in znakprep:
        let = letter.find(i)
        if letter[let]=="Я":
            res += letter[sdvig-1]
        elif letter[let]=="я":
            res += letter[33+sdvig-1]
        else:
            res += letter[let + sdvig]
    else:
        res += i
    l+=1
out = open("output.txt","w")
out.write(res)
out.close()