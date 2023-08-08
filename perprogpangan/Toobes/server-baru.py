import socket
import threading
import os

clients = []

# TODO: -===  MAIN  ===-
def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(100)
    print("Server berjalan...")

    while True:
        conn, addr = server_socket.accept()
        clients.append(addr)
        data = conn.recv(2048)
        print(f'clients: {clients}')
        # break
        # # return
        # choice = data.split(b'|', maxsplit=1)[0]

        # if choice == b'1' or choice == b'2':
        #     client_thread = threading.Thread(target=handle_client_txt, args=(server_socket, client_address, data, choice))
        #     client_thread.start()

        # if server_socket.accept() == True:
        #     client_thread = threading.Thread(target=handle_client, args=(server_socket, address, connection))
        #     client_thread.start()

    server_socket.close()

# TODO: -===  MAIN HANDLE  ===-
def handle_client_txt(server_socket, client_address, data, choice):
    if choice == b'1' or choice == b'2':
        # Format pesan: "<choice>|<destination_ip>|<destination_port>|<message>"
        message_parts = data.split(b'|', maxsplit=3)
        choice, destination_ip, destination_port, message = message_parts
        forward_message_text(choice, destination_ip, int(destination_port), message.decode('utf-8'), client_address[0], client_address[1])

# TODO: -===  FORWARD MSG TXT  ===-
def forward_message_text(choice, destination_ip, destination_port, message, client_ip, client_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    choice = int(choice.decode('utf-8'))

    if choice == 1 or choice == 2:
        res = f'{choice}|\nPesan dari {client_ip}:{client_port}|\n{message}'
        server_socket.sendto(res.encode('utf-8'), (destination_ip, destination_port))
        print(f"Pesan diteruskan ke {destination_ip}:{destination_port}")
        print('done')



# TODO: -===  RECIEVE  ===-
# TODO: -===  SEND  ===-

if __name__ == "__main__":
    main()
