


mkas = int(input(""))

judul1 = "SEGITIGA".center(mkas)
print ("'",judul1,"'")
jumlah = 1
space = int(mkas/2)
while jumlah < mkas:
    if (jumlah%2):
        print (" "*space, "*"*jumlah)   
        jumlah += 1
        space -= 1

    else:
        jumlah += 1
        continue


print("\n\n")

judul2 = "KUPAT".center(mkas)
print ("'",judul2,"'")

jumlah = 1
space = int(mkas/2)
while jumlah < mkas:
    if (jumlah%2):
        print (" "*space, "*"*jumlah)   
        jumlah += 1
        space -= 1

    else:
        jumlah += 1
        continue

while jumlah != 1:
    if (jumlah%2):
        print (" "*space, "*"*jumlah)   
        jumlah -= 1
        space += 1

    else:
        jumlah -= 1
        continue
    
print(" "*space, "*")
