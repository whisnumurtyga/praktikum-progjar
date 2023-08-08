import socket
import threading
import os




# TODO: -===  MAIN  ===-
def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))
    print("UDP server berjalan...")

    while True:
        data, client_address = server_socket.recvfrom(2084)
        choice = data.split(b'|', maxsplit=1)[0]
        # print(choice)
        
        if (choice == b'1' or choice == b'2'):
            client_thread = threading.Thread(target=handle_client_txt, args=(server_socket, client_address, data, choice))
            client_thread.start()
        elif (choice == b'3'):
            client_thread = threading.Thread(target=handle_client_file, args=(server_socket, client_address, data, choice))
            client_thread.start()




# TODO: -===  MAIN HANDLE  ===-
def handle_client_txt(server_socket, client_address, data, choice):
    if(choice == b'1' or choice == b'2'):
        # Format pesan: "<choice>|<destination_ip>|<destination_port>|<message>"
        message_parts = data.split(b'|', maxsplit=3)
        choice, destination_ip, destination_port, message = message_parts

        forward_message_text(choice, destination_ip, int(destination_port), message.decode('utf-8'), client_address[0], client_address[1])
                

    
received_data = bytearray()
len_size = 0

def handle_client_file(server_socket, client_address, data, choice):
    global received_data, len_size
    message_parts = data.split(b'|')
    file_size = message_parts[3]
    print(message_parts)
    # file_size = int(file_size)

    if message_parts[-1][-5:] != b'<END>':
        data = message_parts[-1]    
        received_data += data
        len_size += len(received_data)

    if len_size == file_size:
        # Menyimpan data yang diterima ke dalam file
        with open("received_file.pdf", "wb") as f:
            f.write(received_data)
            
    # print('done')
    


# TODO: -===  FORWARD MSG TXT  ===-
def forward_message_text(choice, destination_ip, destination_port, message, client_ip, client_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    choice = int(choice.decode('utf-8'))
    
    if(choice == 1 or choice == 2):
        res = f'{choice}|\nPesan dari {client_ip}:{client_port}|\n{message}'
        server_socket.sendto(res.encode('utf-8'), (destination_ip, destination_port))
        print(f"Pesan diteruskan ke {destination_ip}:{destination_port}")




# TODO: -===  RECIEVE  ===-
# TODO: -===  SEND  ===-
    
if __name__ == "__main__":
    main()
