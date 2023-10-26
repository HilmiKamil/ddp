nama = "Muhamad Hilmi Kamil"
nim = "0110223293"
kelas = "TI09"
no_telp = "085933519783"
alamat = "Jl. Jatijajar II"

print("Nama :", nama)
print("Nim :", nim)
print("Kelas :", kelas)
print("No. Telephone :", no_telp)
print("Alamat :", alamat)

print("========================")

Nama = "Ilyas Abdul Aziz"
Nim = "0110223292"
Kelas = "TI09"
No_telp = "085797257153"
Alamat = "Jl. Beringin, Margonda, Depok"

print("Nama :", Nama)
print("Nim :", Nim)
print("Kelas :", Kelas)
print("No. Telephone :", No_telp)
print("Alamat :", Alamat)

print("============================")

berat_badan = float(input("Masukkan berat badan Anda (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan Anda (m): "))
bmi = berat_badan / (tinggi_badan * tinggi_badan)

if bmi < 18.5:
    print("Berat badan Anda kurang dari standar")
elif 18.5 <= bmi < 24.9:
    print("Berat badan Anda normal")
elif 25.0 <= bmi < 29.9:
    print("Berat badan anda Overweight")
else:
    print("Berat badan anda ideal")

print("=======================")

print("Rumus Konveksi dari Celcius ke Fahrenheit")
C = float(input("Masukkan angka Celcius     : "))
konveksi = (9 / 5 * C) + 32
print("Konveksi dari Celcius ke Fahrenheit", konveksi, "F")

print("=======================")
print("Rumus Luas dan Keliling Tabung")
phi = 3.14
r = float(input("Masukkan panjang jari-jari Tabung: "))
t = float(input("Masukkan panjang tinggi Tabung: "))
rumus_luas = 2 * phi * r**2 + 2 * phi * r * t
rumus_keliling = 2 * phi * r + 2 * phi * t
print("Luas Tabung", rumus_luas, "cm2", "dan Keliling Tabung", rumus_keliling, "cm2")
