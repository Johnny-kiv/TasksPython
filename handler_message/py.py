"""import datetime
import random
pogoda = ["Облачность","Солнечно","Дождь","Гроза"]
while True:
    t = input().lower()
    if t=="привет":
        print("Здравствуй, хозяин!")
    elif t=="как дела?":
        print("Все чики-пуки, хозяин!")
    elif t=="сколько времени?":
        print(datetime.datetime.now().time())
    elif t=="какая погода?":
        print("Температура: "+str(random.randint(-10,10))+"C,",pogoda[random.randint(0,3)],".")
    elif t=="дай бабла!":
        print("Даю -",random.randint(0,1000000000),"$ $)")
    elif t=="0":
        print("Досвидос амигос")
        break
    else:
        print("Error :(")"""
f = open("input.txt","r")
l=0
line = f.read().split("\n")
for i in line:
    l+=1
    print(f"Строка {l}",len(i))