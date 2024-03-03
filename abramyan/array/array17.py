mas = []
while True:
    inp = input("Введите что-нибудь: ")
    if inp == "break":
        break
    mas.append(inp)
l = len(mas)-1
for i in range(0,l,2):
    print(mas[i])
    if not l-i<0:
        print(mas[l-(i)])