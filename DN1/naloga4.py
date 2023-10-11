def izpisi_trikotnik(visina):
    for i  in range(1, visina+1):
        print("*" * (i))

# Vnos višine trikotnika
visina = int(input("\nPodaj višino željenega trikotnika: "))

# Izris rezultata
if(visina >= 0):
    print("\nVaš trikotnik: \n")
    izpisi_trikotnik(visina)
else:
    print("\nNeveljaven vnos!\n")