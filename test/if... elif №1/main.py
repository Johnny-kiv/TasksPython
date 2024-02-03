inp=open("input.txt")
inpf=inp.read()
inp.close()
out=open("output.txt","w")
if (inpf=='1'):
    out.write("плохо")
elif (inpf=='2'):
    out.write("неудоротворительно")
elif (inpf=='3'):
    out.write("удоротворительно")
elif (inpf=='4'):
    out.write("хорошо") 
elif (inpf=='5'):
    out.write("отлично") 
else:
    out.write("ошибка")
out.close()