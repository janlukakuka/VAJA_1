
def jePrastevilo(a):
    p = 1    
    for i in range(2, int((a/2)+1)): 
        if (a % i) == 0: 
            p = 0
    return p
 

# Funkcija, vzame za parameter število, do katerega želimo poiskati vsa praštevila. Vrne list praštevil do podanega števila
def prastevila(input):
    out = []
    for n in range(2, input+1): 
        if(jePrastevilo(n)):
            out.append(n)
    return out

print(prastevila(50))