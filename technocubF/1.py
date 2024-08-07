import time

if __name__=="__main__":
    a = 0
    b = 1
    c = 2
    start_time = time.time()
    mas1 = [a,b,c]
    mas2 = []
    for i in mas1:
        if a<i:
            mas2.append(i)

    a1 = mas2[1]-mas2[1-1]
    g1 = mas2[1]/mas2[1-1]
    is_g = True
    is_a = True
    res = ""
    for i in range(1,len(mas2)):
        a2 = mas2[i]-mas2[i-1]
        g2 = mas2[i]/mas2[i-1]
        if a1 != a2:
            is_a = False
        elif g1 != g2:
            is_g = False
            break   
            
print("Process finished --- %s seconds ---" % (time.time() - start_time))
        
