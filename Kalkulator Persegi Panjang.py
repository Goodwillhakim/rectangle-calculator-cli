print("=" *41)
print("       Kalkulator Persegi Panjang")
print( "=" *41)

#INPUT

Panjang = float(input("Masukan Panjang Berupa Cm: "))
Lebar = float(input("Masukan Lebar Berupa Cm: "))

#PENGHITUNGAN

Luas = Panjang * Lebar 
Keliling = 2 * (Panjang + Lebar)
 
#OUTPUT

print(f"Jadi Luas Nya Adalah {Panjang:.2f}")
print(f"dan Keliling Adalah {Keliling:.2f}") 