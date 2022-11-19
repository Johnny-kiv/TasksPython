def CL(i):
    r = 0
    res = i.split(" ")
    b = res[0] > res[1]
    if b:
        r = len(res[0])
    else:
        r = len(res[1])
    return r
i = input("Введите словечко: ")
print(CL(i))

