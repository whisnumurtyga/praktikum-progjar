import socket


HOST = '' # alamat IP server
PORT = 12345 # port server

# buat socket server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

# tunggu koneksi dari client
conn, addr = s.accept()
print('Connected by', addr)

# baca data dari client
data = conn.recv(1024)
print('Received from client:', data.decode())

# kirim balasan ke client
response = 'Hello, client!'
conn.sendall(response.encode())

# tutup koneksi
conn.close()