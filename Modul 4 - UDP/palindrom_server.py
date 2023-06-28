import socket

def is_palindrome(string):
    return string == string[::-1]

# Inisialisasi socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 4000)
server_socket.bind(server_address)

print("Server berjalan...")

while True:
    data, client_address = server_socket.recvfrom(1024)
    input_string = data.decode()

    if is_palindrome(input_string):
        response = f"{input_string} adalah palindrom."
    else:
        response = f"{input_string} bukan palindrom."

    server_socket.sendto(response.encode(), client_address)
