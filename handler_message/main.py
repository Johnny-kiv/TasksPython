import datetime
while True:
    t = input().lower()
    if t=="привет":
        print("Здравствуй, хозяин!")
    elif t=="как дела?":
        print("Все чики-пуки, хозяин!")
    elif t=="сколько времени?":
        print(datetime.datetime.now().time())
    elif t=="0":
        print("Досвидос амигос")
        break
    else:
        print("Error :(")