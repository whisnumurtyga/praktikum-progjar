import socket

HOST = 'localhost'  # Alamat IP server
PORT = 12345  # Port server

# Buat socket klien
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    # Input suhu dari pengguna
    input_str = input("Masukkan suhu (contoh: 25 C to F): ")
    if input_str == 'q':
        break

    # Kirim data ke server
    s.sendall(input_str.encode())

    # Terima balasan dari server
    data = s.recv(1024).decode()
    print('Received from server:', data)

# Tutup koneksi
s.close()
