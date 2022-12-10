l=0
p = "мама мыла раму"
masi = []
for i in range(len(p)):
    if p[i]=="а":
        masi.append(i)
    if p[i]=="м":
        masi.append(i)
    if p[i]=="а" or p[i]=="м":
        l+=1
print(int(l/2))
print(masi)