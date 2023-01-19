import random

#nomer = int(input("Tebak angka :"))
#acak = random.randint(1, 25)
#while nomer != acak:
#    nomer = int(input("Tebak angka :"))

b = 1
while b == 1:
    ready = str(input("Ready kidz?"))
    if ready == "ndak":
        print("hmm")
        b = 0 
    elif ready == "y":
        i = 0
        while i == 0:    
            rentang = int(input("Masukin rentang maksimal nomor :"))
            nomor = int(input(f"Tebak Angka antara 1 sampai {rentang} :"))
            acakan = random.randint(1, rentang)
            while nomor != acakan:
                if nomor < acakan:
                    print("Kureng mazseh!!")
                elif nomor > acakan:
                    print("Kepunjulen mazseh!!")
                nomor = int(input(f"Tebak Angka antara 1 sampai {rentang} :"))
            print("btolll")
            break
        

    