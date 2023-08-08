import os
import socket
import threading
import datetime

received_size = 0;
i = 0;
chunks = b''

def handle_client(server_socket, client_address, data):
    # TODO: FORMAT FILE [ choice | file_size | file_path/name | binary data file ]
    choice, *message_parts = data.split(b'|', maxsplit=3)    
    if choice == b'3':
        receive_file(server_socket, message_parts, client_address)


def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))
    print("UDP server berjalan...")

    while True:
        data, client_address = server_socket.recvfrom(4160)
        client_thread = threading.Thread(target=handle_client, args=(server_socket, client_address, data))
        client_thread.start()
            
def generate_path(message_parts, client_address):
    now = datetime.datetime.now()
    timedate = now.strftime("%Y%m%d%H%M%S")
    file_name = message_parts[1].decode('utf-8')
    save_path = f'./result/{client_address[1]}-{file_name}'
    
    return save_path


def receive_file(server_socket, message_parts, client_address):
    global received_size;
    global i;
    global chunks;
    
    file_size = int(message_parts[0].decode('utf-8'))
    save_path = generate_path(message_parts, client_address)
    chunk = message_parts[-1]
    chunks += chunk
    # print(len(chunk))
    # print(f'{i}\t{received_size}\t{file_size}\t{file_size-received_size}')
 
    # with open(save_path, 'wb') as file:
    #     if received_size <= file_size:
    #         print(f'i:{i}\t{len(chunk)}')
    #         file.write(chunk)
    #         received_size += len(chunk)    
    #         i+=1
    
    print(f'last: {chunks}')
            
    # print(f'{i}\t{received_size}\t{file_size}\t{file_size-received_size}')

    

if __name__ == "__main__":
    main()
