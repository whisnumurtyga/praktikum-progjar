import socket

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Inisialisasi socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 4000)
server_socket.bind(server_address)

print("Server berjalan...")

while True:
    data, client_address = server_socket.recvfrom(1024)
    number = int(data.decode())

    if is_prime(number):
        response = f"{number} adalah bilangan prima."
    else:
        response = f"{number} bukan bilangan prima."

    server_socket.sendto(response.encode(), client_address)
