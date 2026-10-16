class Buku:
    def __init__(self, judul, penulis="Tidak diketahui", tahun_terbit=0):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def info(self):
        print(f"Judul       : {self.judul}")
        print(f"Penulis     : {self.penulis}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
        print("-" * 30)

# Membuat objek sesuai latihan sebelumnya
buku1 = Buku("Dasar Pemrograman Python", "Andi Pratama", 2021)
buku2 = Buku("Struktur Data", "Siti Aminah", 2022)
buku3 = Buku("Basis Data", "Budi Santoso", 2023)

# Membuat satu objek tanpa mengisi penulis (menggunakan nilai default)
buku4 = Buku("Pemrograman Web", tahun_terbit=2024)

# Menampilkan informasi buku
buku1.info()
buku2.info()
buku3.info()
buku4.info()