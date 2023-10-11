vrednost = []
for i in range(3):
    vrednost.append(input("Vnesi " + str(i+1) + ". vrednost: "))
for i in range(3):
    print("Vrednost " + str(i+1) + " je: " + str(vrednost[i]) + "    Tip: " + str(type(vrednost[i])))



if(vrednost[1] == vrednost[0] and vrednost[2] <= vrednost[0]):
    print("Druga vred. je enaka prvi in tretja vred. je manjsa ali enka prvi.")
else:
    print("Vrednosti ne zadoscajo pogoju.")