import socket

HOST = 'localhost'  # Alamat IP server
PORT = 12345  # Port server

# Buat socket klien
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    # Input jari-jari dari pengguna
    radius = input("Masukkan jari-jari lingkaran: ")
    if radius == 'q':
        break

    # Kirim data ke server
    s.sendall(radius.encode())

    # Terima balasan dari server
    data = s.recv(1024).decode()
    print('Hasil perhitungan:', data)

# Tutup koneksi
s.close()
