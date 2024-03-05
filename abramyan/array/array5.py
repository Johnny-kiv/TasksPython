array = [1,1]
n = int(input("Enter the number N: "))
for i in range(2,n):
    f = array[i-2]+array[i-1]
    array.append(f)
for i in array:
    print(i,end=", ")