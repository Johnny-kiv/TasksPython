n = int(input())
ans = 0
st = 1
while n > 0:
    c = n % 8
    if c in [1,2,4,7]:
        ans = -1
    n //= 8
    c = c // 2
    ans += c * st
    st *= 4
print(ans)