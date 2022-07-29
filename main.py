"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNGCTION
"""
import gempaterkini
if __name__ == '__main__':
    print('Aplikasi Utama')
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)

