import socket

HOST = 'localhost'  # Alamat IP server
PORT = 12345  # Port server

# Buat socket klien
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    # Input operasi dan angka dari pengguna
    operation = input("Masukkan operasi (+, -, *, /): ")
    if operation == 'q':
        break

    operand1 = float(input("Masukkan angka pertama: "))
    operand2 = float(input("Masukkan angka kedua: "))

    # Kirim data ke server
    message = operation + ' ' + str(operand1) + ' ' + str(operand2)
    s.sendall(message.encode())

    # Terima balasan dari server
    data = s.recv(1024).decode()
    print('Hasil:', data)

# Tutup koneksi
s.close()
