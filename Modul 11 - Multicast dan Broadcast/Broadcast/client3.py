import socket
import threading

def receive_message():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(f'{message}')
        except ConnectionResetError:
            print('Server disconnected.')
            break

def send_message():
    while True:
        message = input('')
        client_socket.send(message.encode('utf-8'))
        if message == 'exit':
            client_socket.close()
            break

host = '127.0.0.1'
port = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

receive_thread = threading.Thread(target=receive_message)
send_thread = threading.Thread(target=send_message)

receive_thread.start()
send_thread.start()
