e = "01234567"
inp = input()
res = 'YES'
for i in inp:
    if not i in e:
        res = 'NO'
        break
if res=="YES":
    if int(inp)%7!=0:
        res='NO'
print(res)
