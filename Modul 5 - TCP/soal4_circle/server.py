import socket
import math

HOST = ''  # Alamat IP server
PORT = 12345  # Port server

# Buat socket server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print('Server listening on', PORT)

# Tunggu koneksi dari klien
conn, addr = s.accept()
print('Connected by', addr)

while True:
    # Baca data dari klien
    data = conn.recv(1024).decode()
    if not data:
        # Jika data kosong, berarti koneksi ditutup oleh klien
        break

    # Parse pesan dari klien menjadi jari-jari
    radius = float(data)

    # Hitung luas dan keliling lingkaran
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius

    # Buat pesan balasan
    response = "Luas: {:.2f}, Keliling: {:.2f}".format(area, circumference)

    # Kirim balasan ke klien
    conn.sendall(response.encode())

# Tutup koneksi
conn.close()
