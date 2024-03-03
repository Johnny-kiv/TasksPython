mas = []
while True:
    inp = input("Введите что-нибудь: ")
    if inp == "break":
        break
    mas.append(inp)
l = len(mas)
for i in range(l):
    print(mas[i])
    if not l-i<0:
        print(mas[l-(i+1)])