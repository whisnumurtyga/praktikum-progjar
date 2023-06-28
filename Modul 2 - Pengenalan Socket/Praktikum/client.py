import socket

# Membuat object socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menghubungkan Socket Client ke Server
client_socket.connect(('localhost', 8000))

# Mengirim data ke server
message = 'Hello, server!'
client_socket.sendall(message.encode())

# Menerima respons dari server
data = client_socket.recv(1024)
print(f'Received: {data.decode()}')

# Menutup Koneksi
client_socket.close()