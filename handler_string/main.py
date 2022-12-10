"""l=0
p = "мама мыла раму"
masi = []
for i in range(len(p)):
    if p[i]=="а":
        masi.append(i)
    if p[i]=="м":
        masi.append(i)
    if p[i]=="а" or p[i]=="м":
        l+=1
b=True
for i in masi:
    if b==True:
        print(p[i]+p[i+1],p[i])
        b=False
    else:
        b=True"""
l=0
p = "мама мыла раму"
masi = []
for i in range(len(p)):
    if p[i]=="а":
        print(p[i-1]+p[i]+p[i+1])
