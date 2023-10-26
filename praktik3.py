x = input("Masukkan angka: ")
y = input("Masukkan angka: ")

x = int(x)
y = int(y)

if x > y:
    print(x, "lebih besar dari", y)
elif x == y:
    print(x, "sama dengan", y)
else:
    print(x, "lebih kecil dari", y)

print("====================================")


def menu_restaurant():
    print("Menu Restaurant:")
    print("1. Kwetiau")
    print("2. Bubur")
    print("3. Kacang Hijau")


def message_menu():
    message = int(input("Silahkan pilah salah satu menu yang di list: "))

    if message == 1:
        print("Anda memesan Kwetiau.")
    elif message == 2:
        print("Anda memesan Bubur.")
    elif message == 3:
        print("Anda memesan Kacang Hijau.")
    else:
        print(
            "Nomor yang anda pesan tidak ada, silahkan pilih nomor menu yang ada di list."
        )


if __name__ == "__main__":
    while True:
        menu_restaurant()
        message_menu()
        lanjutkan = input("Apakah Anda ingin memesan lagi? (y/n): ")
        if lanjutkan.lower() != "y":
            print("Terima kasih! Sampai jumpa.")
            break
print("===========================================")

mahasiswa = input("Masukkan Nama Mahasiswa: ")

if mahasiswa == "Hilmi":
    print("NIM Hilmi: 12345.")
elif mahasiswa == "Ilyas":
    print("NIM Ilyas: 67899.")
elif mahasiswa == "Elyas":
    print("NIM Ilyas: 699697.")
else:
    print("NIM tidak ditemukan.")

    print("==========================================")


x = int(input("Masukkan angka: "))
y = int(input("Masukkan angka: "))
z = int(input("Masukkan angka: "))

print(x > y and x < z)
print(x > y or x < z)
print(not (x > y and x < z))
