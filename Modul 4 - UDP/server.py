import socket


socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 4000)

socket_server.bind(server_address)

while True: 
    print("Menunggu Client")
    data, client_address = socket_server.recvfrom(4040)
    print(f'data: {len(data.decode())}')
    socket_server.sendto(str(len(data)).encode(), client_address)
    