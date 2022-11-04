i = input()
scobki = ["(",")"]
o = 0
c = 0
leen = 0
mas = []
for l in i:
    if l==scobki[0]:
        o+=1
    if l==scobki[1]:
        c+=1
        mas.append(leen)
    leen+=1
if o>c:
    print("-1")
elif o<c:
    print(f"Error :/ {mas[-1]}")
else:
    print("0")