import socket

# Inisialisasi socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menghubungkan ke Server
server_address = ('localhost', 5000)
sock.connect(server_address)

# Meminta input dari pengguna
operator = input("Masukkan Operator(+,-,*,/,%): ")
operand1 = input("Masukkan operand1: ")
operand2 = input("Masukkan operand2: ")

# Mengirim pesan ke server
message = operator + " " + operand1 + " " + operand2

# Mengirim pesan ke server
sock.send(message.encode())

# Menerima pesan balasan dari server
response = sock.recv(1024).decode()
print("Hasil perhitungan: ", response)

# Menutup koneksi dengan server
sock.close()
