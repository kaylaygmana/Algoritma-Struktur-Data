import os
import random
os.system('cls')

# ranga besar angka
a= list(range(1,100))

# pemasukkan ke list kosong
angka = random.sample(a,k=10)

def merge_sort (angka):
    if len(angka) > 1:
        angka_pertengahan = len(angka) // 2
        angka_kiri = angka[:angka_pertengahan]
        angka_kanan = angka [angka_pertengahan:]

        # pemanggilan berulang
        merge_sort(angka_kiri)
        merge_sort(angka_kanan)

        
        # deklarasi variable 
		# i = 0 -> indeks untuk angka kiri
		# j = 0 -> indeks untuk angka kanan
		# k = 0 -> indeks untuk gabungan

        i = j = k = 0
        
        # apabila masih ada angka kanan dan kiri untuk dibandingkan
        while i < len(angka_kiri) and j < len(angka_kanan):
            if angka_kiri[i] < angka_kanan[j]:
                angka[k] = angka_kiri[i]
                i += 1
                # k += 1
            else:
                angka[k] = angka_kanan[j]
                j += 1
                # k += 1
            k += 1

        # apabila sisa angka kiri
        while (i < len(angka_kiri)):
            angka[k] = angka_kiri[i]
            i += 1
            k += 1
        
        # apabila sisa angka kanan
        while (j < len(angka_kanan)):
            angka[k] = angka_kanan[j]
            j += 1
            k += 1



print(f"Data sebelum di urutkan {angka}")

merge_sort(angka)

print(f"Data setelah diurutkan {angka}")
