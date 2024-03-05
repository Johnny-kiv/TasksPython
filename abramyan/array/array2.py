n = int(input("Enter the number n: "))
arr = []
for i in range(1,n+1):
    num = 2**(i)
    arr.append(num)
for i in arr:
    print(i,end=" ")