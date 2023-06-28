import socket

# Membuat Object Socket untuk server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# binding ke alamat ip dan port tertentu
server_socket.bind(('localhost', 8000))

# listen koneksi dari client
server_socket.listen()

# Menerima Konseksi dari Client
print('Waiting...')
client_socket, client_address = server_socket.accept()
print(f'Connected by {client_address}')

# Menerima data dari socket Client
data = client_socket.recv(1024)
print(f'Recieved: {data.decode()}')

# Mengirim response ke socket client
message = 'Hello babe!'
client_socket.sendall(message.encode())

# Konfigurasi Socket
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, (1,5))

# menutup koneksi
client_socket.close()
server_socket.close()