import ftplib
import os

def upload_file(hostname, username, password, filename):
    try:
        # Membuat objek FTP
        ftp = ftplib.FTP(hostname)

        # Login ke server FTP
        ftp.login(username, password)

        # Buka file untuk dibaca
        with open(filename, 'rb') as file:
            # Dapatkan nama file tanpa ekstensi
            base_filename = os.path.splitext(filename)[0]

            # Tambahkan awalan "new_" pada nama file
            new_filename = "new_" + base_filename + os.path.splitext(filename)[1]

            # Unggah file mp4 dengan nama baru
            ftp.storbinary('STOR ' + new_filename, file)

        # Tutup koneksi FTP
        ftp.quit()
        print("Gambar berhasil diunggah")
    except ftplib.all_errors as e:
        print("Terjadi kesalahan: ", e)

# Contoh penggunaan fungsi upload_file
hostname = '127.0.0.1'
username = 'whisnuu'
password = 'progjar123'

filename = '23.jpg'
upload_file(hostname, username, password, filename)
