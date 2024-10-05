from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, "INPUT.TXT")
inp = open(file_path)
coun = int(inp.readline())
mas = inp.readline().split(" ")
news = []
som1 = []
som2 = []
for i in range(len(mas)):
    if mas[i]!=mas[0]:
        diff = abs(int(mas[i])-int(mas[i-1]))
        som1.append(diff)
    if mas[i]!=mas[0] and mas[i]!=mas[-1]:
        diff = abs(int(mas[i+1])-int(mas[i-1]))
        som2.append(diff)


routes = []
print(som1,som2)
n = -1
for i in range(0,len(som1),2):
    diff = som2[n]+som1[i]
    routes.append(diff)
    print(som2[n],som1[i])
    n-=1
print(routes)
inp.close()
out = open("OUTPUT.TXT","w")
#out.write(str(b))
out.close()
