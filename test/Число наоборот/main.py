def naoborot(inp):
    res=''
    for i in range(len(inp)-1,-1,-1):
        res+=inp[i]
    return res
inp1 = input()
inp2 = int(input())
sogl = "йфцчвскмпнртгьшлбщдзжхъЙФЦЧВСКМПНРТГЬШЛБЩДЗХЪЖ"
l = 0
for i in inp1:
    if sogl.find(i):
        l+=1
if l>=inp2:
    print(naoborot(inp1))
else:
    print("Ошибка:/")