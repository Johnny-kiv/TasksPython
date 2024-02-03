inp = input()
nums = "1234567890"
inq=
res = 0
l=0
plus = False
minus = False
for i in inp:
    if i in nums:
        mas.append(int(i))
        if plus:
            res+=int(i)
        if minus:
            res=res-int(i)
        minus = False
        plus = False
    elif i == "+":
        minus = False
        plus = True
    elif i == "-":
        plus = False
        minus = True
print(res)