NPM = input("Masukkan NPM: ")
Nama = input("Masukkan Nama: ")
Umur = int(input("Masukkan Umur: "))
Prodi = input("Masukkan Prodi: ")

tugas = float(input("Masukkan Nilai Tugas: "))
uts = float(input("Masukkan Nilai UTS: "))
uas = float(input("Masukkan Nilai UAS: "))

nilai_akhir = (tugas + uts + uas) / 3

print("\n=== DATA MAHASISWA ===")
print("NPM:", NPM)
print("Nama:", Nama)
print("Umur:", Umur)
print("Prodi:", Prodi)
print("Nilai Akhir:", round(nilai_akhir, 2))

if nilai_akhir >= 75:
    print("Anda Lulus")
else:
    print("Anda Tidak Lulus")