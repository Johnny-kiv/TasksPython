import time

def printm(mas,res):
    for i in mas:
        res+=str(i)+" "
    return res
if __name__=="__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    start_time = time.time()
    mas1 = [a,b,c]
    mas2 = []
    for i in mas1:
        f = i
        for j in mas1:
            if f>j:         
                f=j
        mas2.append(f)
        mas1.remove(f)
        print(len(mas1))
    mas2.append(mas1[0])
    mas1.pop(0)

            
                
    print(mas2)
    res = ""

    a1 = mas2[1]-mas2[0]
    g1 = mas2[1]/mas2[0]
    a2 = mas2[2]-mas2[1]
    g2 = mas2[2]-mas2[1]
    if a1 == a2:
        res+="A "
        print(printm(mas2,res))
    elif g1 == g2:
        res+="G "    
        print(printm(mas2,res))  
    else:
        print("No") 
            
print("Process finished --- %s seconds ---" % (time.time() - start_time))
        
