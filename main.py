"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNGCTION
"""


def ekstraksi_data():
    """
    Tanggal : 28 Juli 2022
    Waktu : 02:17:36 WIB
    Magnitudo : 4.1
    Kedalaman : 10 km
    Lokasi : 8.20 LS - 115.50 BT
    Pusat Gempa : Pusat gempa berada di darat 16 km barat laut Karangasem
    Keterangan : Dirasakan (Skala MMI): II Karangasem
    """
    hasil = dict()
    hasil["tanggal"] = "28 Juli 2022"
    hasil["waktu"] = "02:17:36"
    hasil["magnitudo"] = 4.1
    hasil["lokasi"] = {"ls": 8.20, "bt": 115.50}
    hasil["pusat"] = "Pusat gempa berada di darat 16 km barat laut Karagasem"
    hasil["keterangan"] = "Dirasakan (Skala MMI) : II Karangasem"
    return hasil


def tampilkan_data(result):
    print ("Gempa Terakhir Berdasarkan situs BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Keterangan {result['keterangan']}")


if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)

