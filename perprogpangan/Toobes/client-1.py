import socket
import threading
import os




data_clients = {
    1: {
        'ip' : '127.0.0.2', 
        'port' : 12346 
    }, 
    2 : {
        'ip' : '127.0.0.3',
        'port' : 12347
    }
}




def main():
    server_ip = "127.0.0.1"
    server_port = 12345
    
    my_ip = '127.0.0.2'
    my_port = 12346

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind((my_ip, my_port))

    print("UDP client berjalan...")

    send_thread = threading.Thread(target=send_message, args=(client_socket, server_ip, server_port))
    send_thread.start()
    
    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
    receive_thread.daemon = True  # Menandai thread receive sebagai daemon, sehingga berhenti saat program utama berhenti.
    receive_thread.start()
    
    send_thread.join()




# TODO: -===  SEND  ===-  
def send_message(client_socket, server_ip, server_port):
    while True:
        show_menu_jenis_pesan()
        choice = int(input("Masukkan pilihan: "))
        if choice == 0:
            break
        elif choice == 1 and choice == 2:
            print('1')
            handle_msg_txt(choice, client_socket, server_ip, server_port)
            
    client_socket.close()


def handle_msg_txt(choice, client_socket, server_ip, server_port):
    show_clients()
    no_client = int(input("Masukkan client_id tujuan: "))
    destination_ip = data_clients[no_client]['ip']
    destination_port = data_clients[no_client]['port']
    
    if choice == 1:
        message = input("Masukkan pesan: ")
    elif choice == 2:
        print("Masukkan pesan (ketik '.' di baris baru untuk mengakhiri):")
        message_lines = []
        while True:
            line = input()
            if line == '.':
                break
            message_lines.append(line)
        message = '\n'.join(message_lines)
        
    # Format pesan: "<choice>|<destination_ip>|<destination_port>|<message>"
    formatted_message = f"{choice}|{destination_ip}|{destination_port}|{message}"
    client_socket.sendto(formatted_message.encode('utf-8'), (server_ip, server_port))
    print(f"Pesan terkirim ke {destination_ip}:{destination_port}")


def handle_msg_file(choice, client_socket, server_ip, server_port):
    show_clients()
    no_client = int(input("Masukkan client_id tujuan: "))
    destination_ip = data_clients[no_client]['ip']
    destination_port = data_clients[no_client]['port']
    
    path_file = input("Masukkan path file: ")
    file = open(path_file, "rb")
    file_size = os.path.getsize(path_file)

    with open(path_file, "rb") as f:
        data = f.read(2048)
        while data:
            client_socket.sendto(data, (server_ip, server_port))
            data = f.read(2048)
            formatted_message = f"{choice}|{destination_ip}|{destination_port}|{"
    print("File berhasil dikirim.")

# TODO: -===  RECIEVE  ===-  
def receive_message(client_socket):
    while True:
        data, server_address = client_socket.recvfrom(2084)
        choice = data.split(b'|')[0]
        
        if (choice == b'1' or choice == b'2'):
            data = data.decode('utf-8')
            choice, fromm, message = data.split('|')
            print(fromm, message)
        
        



# TODO: -===  SHOW  ===-
def show_menu_jenis_pesan():
    print("Pilih menu:")
    print("1. Kirim Pesan")
    print("2. Kirim Pesan Paragraph")  # Tambahkan pilihan ini
    print("3. Kirim Document (DOC/PDF)")
    print("4. Kirim Gambar (JPG/PNG)")
    print("5. Kirim Suara (MP3)")
    print("6. Kirim Video (MP4)")
    print("0. EXIT")


def show_clients():
     # Menggunakan loop for bersarang untuk mencetak semua key dan value
    for client_id, client_info in data_clients.items():
        print(f"Client ID: {client_id}\tIP: {client_info['ip']}\t Port:{client_info['port']}")
    
    
    
    
# TODO: -===  MAIN  ===-
if __name__ == "__main__":
    main()
