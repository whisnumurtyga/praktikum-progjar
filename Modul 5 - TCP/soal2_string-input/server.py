import socket


HOST = ''  # Alamat IP server
PORT = 12345  # Port server

# Buat socket server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print('Server listening on', PORT)

# Tunggu koneksi dari client
conn, addr = s.accept()
print('Connected by', addr)

while True:
    # Baca data dari client
    data = conn.recv(1024).decode()
    if not data:
        # Jika data kosong, berarti koneksi ditutup oleh client
        break

    # Hitung panjang karakter kalimat
    length = len(data)

    # Kirim balasan ke client
    response = str(length)
    conn.sendall(response.encode())

# Tutup koneksi
conn.close()
