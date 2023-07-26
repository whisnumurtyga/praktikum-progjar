import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'exit':
                break
            print(f'{client_address}: {message}')
            broadcast_message(message, client_address)
        except ConnectionResetError:
            print(f'{client_address} disconnected.')
            break
    client_socket.close()

def broadcast_message(message, sender_address):
    for client_socket, client_address in clients:
        if client_address != sender_address:
            try:
                client_socket.send(message.encode('utf-8'))
            except ConnectionResetError:
                print(f'{client_address} disconnected.')
                clients.remove((client_socket, client_address))
                client_socket.close()

host = '127.0.0.1'
port = 8000
clients = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print('[SERVER STARTED] Waiting for connections...')

while True:
    client_socket, client_address = server_socket.accept()
    clients.append((client_socket, client_address))
    print(f'[NEW CONNECTION] Client {client_address} Connected')
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
