# toko.py

# 1. Buat list of dictionary bernama items
items = [
    {"nama": "mimic octopus", "stok": 20, "harga": 12000},
    {"nama": "redfox", "stok": 15, "harga": 13000},
    {"nama": "brontosaurus", "stok": 10, "harga": 14000},
    {"nama": "Telur dino", "stok": 30, "harga": 22000},
    {"nama": "Susu dino", "stok": 12, "harga": 18000}
]

# 2. Tampilkan isi dari list of dictionary menggunakan perulangan
print("Daftar Barang di Toko:")
for item in items:
    print(f"Nama: {item['nama']}, Stok: {item['stok']}, Harga: Rp{item['harga']}")

# 3. Buat function create untuk menambahkan item ke list of dictionary
def tambah_item(nama, stok, harga):
    item_baru = {
        "nama": nama,
        "stok": stok,
        "harga": harga
    }
    items.append(item_baru)
    print(f"Item '{nama}' berhasil ditambahkan.")

# Contoh penggunaan function tambah_item
tambah_item("mutasi" "", 25, 5000)

# Tampilkan ulang isi items
print("\nSetelah Penambahan:")
for item in items:
    print(f"Nama: {item['nama']}, Stok: {item['stok']}, Harga: Rp{item['harga']}")