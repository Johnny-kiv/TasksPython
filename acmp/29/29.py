from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, "INPUT.TXT")
inp = open(file_path)
global l
l = 0 
a = int(inp.read())
mas = [a]
def recurs():
    mas.append(0)
    if mas[-1]!=mas[-2]:
        mas[0]+=1
        mas[1]-=1
        l+=1
        print(l)
    else:
        recurs()
recurs()
inp.close()
out = open("OUTPUT.TXT","w")
#out.write(str(b))
out.close()
