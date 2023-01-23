angka_pertama = int(input("Angka pertama : "))
angka_kedua   = int(input("Angka kedua : "))
operasi       = input("operasi : ")

if operasi == "+":
    print("hasil : ", angka_pertama + angka_kedua)
elif operasi == "-":
    print("hasil : ", angka_pertama - angka_kedua)
elif operasi == "*":
    print("hasil : ", angka_pertama * angka_kedua)
elif operasi == "/":
    print("hasil : ", angka_pertama / angka_kedua)
elif operasi == "**":
    print("hasil : ", angka_pertama ** angka_kedua)
elif operasi == "//":
    print("hasil : ", angka_pertama // angka_kedua)
elif operasi == "%":
    print("hasil : ", angka_pertama % angka_kedua)
