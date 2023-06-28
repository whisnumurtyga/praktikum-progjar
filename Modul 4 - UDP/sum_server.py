import socket

# Inisialisasi socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 4000)
server_socket.bind(server_address)

print("Server berjalan...")

while True:
    data, client_address = server_socket.recvfrom(1024)
    numbers = data.decode().split(',')  # Memisahkan angka-angka yang dikirim

    # Melakukan penjumlahan seluruh bilangan bulat
    total = sum(int(num) for num in numbers if num.isdigit())

    response = f"Hasil penjumlahan: {total}"

    server_socket.sendto(response.encode(), client_address)
