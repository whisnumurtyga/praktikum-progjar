import socket


HOST = 'localhost' # alamat IP server
PORT = 12345 # port server

# buat socket client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# kirim data ke server
message = 'Hello, server!'
s.sendall(message.encode())

# terima balasan dari server
data = s.recv(1024)
print('Received from server:', data.decode())

# tutup koneksi
s.close()