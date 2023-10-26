kendaraan = ["B 370 EA", "Yamaha R15", "150cc", "Biru"]
kendaraan.append("36,08 Juta")
kendaraan.append("2 Roda")
kendaraan.insert(2, "Yamaha")
kendaraan.insert(3, "Motor")
print(kendaraan)

ket = """Selamat datang silahkan pilih rumus luas bangun datar
    1. Rumus Luas Persegi
    2. Rumus Luas Lingkaran
    3. Rumus Luas Segitiga
    Masukkan Angka : """
rumus = input(ket)
match rumus:
    case "1":
        print("Kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("Masukkan panjang sisi persegi: "))
        luas = sisi * sisi
        print("Luas persegi yang sisinya", sisi, "adalah", luas)
    case "2":
        print("Kamu memilih 2 untuk menghitung luas lingkaran")
        jari = float(input("Masukkan jari-jari: "))
        phi = 3.14
        lingkaran = phi * jari**2
        print("Luas lingkaran yang jari-jarinya", jari, "adalah", lingkaran)
    case "3":
        print("Kamu memilih 3 untuk menghitung luas segitiga")
        alas = int(input("Masukkan alas :"))
        tinggi = int(input("Masukkan tinggi :"))
        segitiga = alas * tinggi / 2
        print("Luas segitiga yang alas", alas, "dan tinggi", tinggi, "adalah", segitiga)
    case _:
        print("Salah memasukkan pilihan")
