import random
import string
from tes import katakata

b = 1
while b == 1:
    ready = str(input("Ready kidz? (Y/N)"))
    if ready == "N":
        print("hmm yowes")
        b = 0 
    elif ready == "Y":
        i = 0
        while i == 0:    
            def soal_tebakan():
                tebakan = random.choice(katakata)
                while '-' in tebakan or ' ' in tebakan:
                    tebakan = random.choice(katakata)
                
                return tebakan.upper()

            def game():
                tebakan = soal_tebakan()
                hurup_tebakan = set(tebakan)
                abjad = set(string.ascii_uppercase)
                udah_ketebak = set()
                
                nyawa = 7
                print(f"\nkamu punya nyawa : {nyawa}")

                while len(hurup_tebakan) > 0 and nyawa > 0:

                    lis_tebakan = [letter if letter in udah_ketebak else '-' for letter in tebakan]
                    print("Soal tebakan : ", ' '.join(lis_tebakan))
                    print("huruf yg udh dipake : ", ' '.join(udah_ketebak))

                    tebakanmu = input("Tebak hurupnya apa (1 aje)\n").upper()
                    if tebakanmu in abjad - udah_ketebak:
                        udah_ketebak.add(tebakanmu)
                        if tebakanmu in hurup_tebakan:
                            hurup_tebakan.remove(tebakanmu)
                            print('\n---weh kok bener---\n')
                    
                        else:
                            print("\n---salah gessss---\n")
                            nyawa = nyawa - 1
                            print("\nNyawamu berkurang ges...")
                            print(f"sisa nyawa : {nyawa}\n")

                    elif tebakanmu in udah_ketebak:
                        print("\n---udeeeh tadiii---\n")
                        nyawa = nyawa - 1
                        print("\nNyawamu berkurang ges...")
                        print(f"sisa nyawa : {nyawa}\n")
                    
                    else:
                        print("\n---malah ngopo---\n")
                        nyawa = nyawa - 1
                        print("\nNyawamu berkurang ges...")
                        print(f"sisa nyawa : {nyawa}\n")

                if nyawa == 0:
                    print("modar")
                    print(f"\nJawaban yang benar : {tebakan}\n")

                else:
                    print(f"jir gg bat lu banh\nJawaban : {tebakan}\nsisa nyawa : {nyawa}\n")

            game()
            break
    else:
        print("nek gak niat mending aku tak minggat wae\n")
        break