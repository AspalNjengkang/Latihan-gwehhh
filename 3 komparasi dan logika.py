# soal
    # -----0+++++5------8++++++11------
    # +++++0-----5++++++8------11++++++

# Jawaban

# 1
    # -----0+++++5------8++++++11------

inputUser = float(input("Masukkan angka : "))

Pls1 = inputUser > 0 and inputUser < 5  
Pls2 = inputUser > 8 and inputUser < 11
Hasil = Pls1 or Pls2
print(Hasil)

# 2 
    # +++++0-----5++++++8------11++++++

inputUser2 = float(input("Masukkan angka : "))

Pls12 = inputUser2 < 0
Pls22 = inputUser2 > 5 and inputUser2 < 8 
Pls32 = inputUser2 > 11
Hasil2 = Pls12 or Pls22 or Pls32
print(Hasil2)
