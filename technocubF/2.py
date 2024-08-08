import datetime
if __name__ == "__main__":
    mas = ["song.mp3", "problem.cfg","problem","picture.png","problem.cfg","sol123.c","data.dat","problem","sol13.c","sol123.c","song.mp3"]

    #n = int(input())
    start = datetime.datetime.now()
    mas_n = []
    mas_f = []
    for i in mas:
        if "." in i:
            mas_n.append(i.split(".")[0])
            mas_f.append(i.split(".")[1])
        else:
            mas_n.append(i)
            mas_f.append("")
    print(mas_n)
    print(mas_f)
    print(datetime.datetime.now()-start)