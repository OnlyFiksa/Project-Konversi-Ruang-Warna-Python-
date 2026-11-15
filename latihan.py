print("================= Program Menghitung Bangun Ruang =====================")


pi = 3.14
#Perhitungan bangun tabung
r_tabung = float(input("Masukkan jari-jari tabung (cm): "))
t_tabung = float(input("Masukkan tinggi tabung (cm): "))

volumetabung = pi * (r_tabung ** 2) * t_tabung

print(f"Volume tabung adalah: {volumetabung}")


#Perhitungan bangun kerucut
r_kerucut = float(input("\n Masukkan jari-jari kerucut: "))
t_kerucut = float(input("Masukkan tinggi kerucut: "))

volumekerucut = 1/3 * pi * (r_kerucut**2) * t_kerucut
print(f"Volume kerucut adalah: {volumekerucut}")

#Perhitungan bangun bola
r_bola = float(input("\n Masukkan jari-jari bola: "))

volumebola = 4/3 * pi * (r_bola**2)
print(f"Volume Bola adalah: {volumebola}")

#Perhitungan prisma
a_segitiga = float(input("\n Masukkan alas segitiga: "))
t_segitiga = float(input("Masukkan tinggi segitiga: "))
t_prisma = float(input("Masukkan tinggi prisma: "))

Luas_alas_segitiga = 1/2 * a_segitiga * t_segitiga
volume_prisma = Luas_alas_segitiga * t_prisma
print(f"Volume prisma adalah: {volume_prisma}")

#Perhitungan Limas
a_segiempat = float(input("\n Masukkan alas segiempat: "))
t_segiempat = float(input("Masukkan tinggi segiempat: "))
l_segiempat = float(input("Masukkan lebar segiempat: "))

Luas_alas_segiempat = a_segiempat * l_segiempat
volume_limas = 1/3 * Luas_alas_segiempat * t_segiempat
print(f"Volume Limas adalah: {volume_limas}")
