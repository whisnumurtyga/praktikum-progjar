import socket


HOST = 'localhost'  # Alamat IP server
PORT = 12345  # Port server

# Buat socket client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    # Input kalimat dari user
    message = input("Masukkan kata atau kalimat (atau 'q' untuk keluar): ")
    if message == 'q':
        break

    # Kirim data ke server
    s.sendall(message.encode())

    # Terima balasan dari server
    data = s.recv(1024).decode()
    print('Panjang karakter:', data)

# Tutup koneksi
s.close()
