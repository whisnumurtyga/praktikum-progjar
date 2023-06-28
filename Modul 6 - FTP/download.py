import ftplib
import os


def download_file(hostname, username, password, filename):
    try:
        # Membuat objek
        ftp = ftplib.FTP(hostname)

        # Login ke server FTP
        ftp.login(username, password)

        # Ganti directory kerja
        ftp.cwd('')

        # Buka file untuk ditulis
        with open(filename, 'wb') as file:
            # Unduh file mp4
            ftp.retrbinary('RETR ' + filename, file.write)

        # Tutup koneksi FTP
        ftp.quit()
        print("File berhasil diunduh")

        # Rename file
        new_filename="result_" + filename
        os.rename(filename, new_filename)
        print("File berhasil direname menjadi", new_filename)

    except ftplib.all_errors as e:
        print("Terjadi kesalahan:", e)


# Contoh penggunaan fungsi download_file
hostname = '127.0.0.1'
username = 'whisnuu'
password = 'progjar123'

filename = 'whisnu.png'
download_file(hostname, username, password, filename)
