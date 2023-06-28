import socket

# Inisialisasi socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 4000)

while True:
    data = input("Masukkan kata: ")
    client_socket.sendto(data.encode(), server_address)

    response, _ = client_socket.recvfrom(1024)
    print(response.decode())
