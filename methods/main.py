def CL(i):
    r = 0
    res = i.split(" ")
    b = len(res[0]) > len(res[1])
    if b:
        r = res[0]
    else:
        r = res[1]
    return r
i = input("Введите словечко: ")
print(CL(i))

