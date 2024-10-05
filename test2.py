l=0
def check_data(d,m,y,l):
    if y-2000==d+m:
        l+=1
    return l 
for y in range(2002,2043):
    for m in range(1,13):
        if m%2==1:
            for d in range(30):
                l=check_data(d,m,y,l)
        elif m==2:
            if m % 4 == 0:
                for d in range(29):
                    l=check_data(d,m,y,l)
            else: 
                for d in range(28):
                    l=check_data(d,m,y,l)
        else:
            for d in range(30):
                l=check_data(d,m,y,l)
print(l)