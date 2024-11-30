n,q = map(int,input().split(" "))
mas1 = []
mas2 = []
for i in range(n):
    mas1.append(input())
for i in range(q):
    inp = input()
    for q in mas1:
        l=len(q)-1
        print(q[0:l]==inp[0:l])

    mas2.append(inp)
