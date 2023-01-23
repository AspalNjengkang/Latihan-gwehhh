import random

b = 1
while b == 1:
    ready = str(input("Ready kidz?"))
    if ready == "ndak":
        print("hmm yowes")
        b = 0 
    elif ready == "y":
        i = 0
        while i == 0:
            kita = str(input('Jaaaaaaaaannn..... Keeeeeeennnnn..... "batu" atau "kertas" atau "gunting" \n'))
            pilihan = (["batu", "kertas", "gunting"])
            komp = random.choice(pilihan)
            print (f"komputer mengeluarkan {komp}")

            if kita == komp :
                print ('Komputer : "imbang cooook"')
            elif (kita == 'batu' and komp == 'gunting') or (kita == 'kertas' and komp == 'batu') or (kita == 'gunting' and komp == 'batu'):
                print ('Komputer : "Hoki cok hokiiii"')
            elif (kita == 'gunting' and komp == 'batu') or (kita == 'batu' and komp == 'kertas') or (kita == 'batu' and komp == 'gunting'):
                print ('Komputer : "yahaa kalahannnnn"')
            else:
                print ('Komputer : "Malah ngopooo"')

            break
