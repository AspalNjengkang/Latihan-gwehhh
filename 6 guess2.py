import random

b = 1
while b == 1:
    ready = str(input("Ready kidz?"))
    if ready == "ndak":
        print("hmm")
        b = 0 
    elif ready == "y":
        i = 0
        while i == 0:    
            rentang_min = int(input("Masukin rentang mminimum nomor :"))
            rentang_max = int(input("Masukin rentang maksimal nomor :"))
            nebak = " "
            while nebak != "b":
                if rentang_min != rentang_max:
                    acakan = random.randint(rentang_min, rentang_max)
                else:
                    rentang_min = rentang_max
                nebak = str(input(f"Tak tebak angka pilihanmu {acakan} to?? \nbener rak? bener (b), kekecilan (k), kegedean(g)"))
                if nebak == "k":
                    rentang_min = acakan +1
                elif nebak == "g":
                    rentang_max = acakan -1
                elif nebak == "b":
                    print("yessss!!!")
                else:
                    print(f"woolah ra ceto... baleni baleni.. malah {nebak} ki ngopo le... \
                    \nNak bener ki pencet b, nak kecilikan ki pencet k, nak kepunjulen pencet g")
            break