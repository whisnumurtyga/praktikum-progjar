import socket

# Inisialisasi socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 4000)

# Meminta input bilangan bulat dari pengguna
numbers = input("Masukkan bilangan bulat (pisahkan dengan koma): ")

# Mengirim pesan ke server
client_socket.sendto(numbers.encode(), server_address)

# Menerima balasan dari server
response, _ = client_socket.recvfrom(1024)

print(response.decode())
