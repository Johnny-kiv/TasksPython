A = int(input())
B = int(input())
ans = max(A,B)
while (ans%A==1 and ans%B==B-1):
    ans+=1
print(ans)