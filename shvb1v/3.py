a = int(input())
n = int(input())
mas = []
for i in range(n):
    el = int(input())
    if el != a:
        el = abs(el-a)
        mas.append(el)
res1 = max(mas)
res2 = mas.count(res1)
print(res1,res2)