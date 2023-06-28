import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 4000)

while True:
    print("Connecting..")
    data = input("Masukkan Data: ")
    socket_client.sendto(data.encode(), server_address)

    feedback, _ = socket_client.recvfrom(4000)
    print(f"balasan dari server : {feedback.decode()}")