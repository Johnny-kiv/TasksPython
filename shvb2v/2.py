n = int(input())
sum1 = 0
sum2 = 0
for i in range(n):
    inp = int(input())
    if inp>100 and inp%4!=0:
        sum1 +=inp
    else:
        sum2 +=inp
res = max(sum1,sum2)*3+min(sum1,sum2)*2
print(res)