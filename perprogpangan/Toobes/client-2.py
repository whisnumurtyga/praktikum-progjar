import socket
import threading
import os




data_clients = {
    1: {
        'ip' : '127.0.0.3', 
        'port' : 12353
    }, 
    2 : {
        'ip' : '127.0.0.5',
        'port' : 12355
    }
}





def main():
    server_ip_udp = "127.0.0.1"
    server_port_udp = 12345
    server_ip_tcp = "127.0.0.2"
    server_port_tcp = 12346
    
    my_ip_udp = '127.0.0.5'
    my_port_udp = 12355
    my_ip_tcp = '127.0.0.6'
    my_port_tcp = 12356

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind((my_ip_udp, my_port_udp))
    
    client_socket_file = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket_file.connect((my_ip_tcp, my_port_tcp))
    
    print('-== Pilih Jenis Pesan ==-')
    print('1. Text')
    print('2. File')
    choose = input("Pilih Jenis Pesan: ") 
    choose = int(choose)
    if choose == 1:
        # print('masuk 1')
        send_thread = threading.Thread(target=send_message, args=(client_socket, client_socket_file, server_ip_udp, server_port_udp))
        send_thread.start()
        send_thread.join()
    elif choose == 2:
        # print('masuk 2')
        send_thread_tcp = threading.Thread(target=send_message_file, args=(client_socket_file, server_ip_tcp, server_port_tcp))
        send_thread_tcp.start()
        send_thread_tcp.join()
   
    receive_thread.daemon = True  # Menandai thread receive sebagai daemon, sehingga berhenti saat program utama berhenti.
    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
    receive_thread.start()
    receive_thread.join()

    # Tutup socket setelah selesai
    client_socket.close()
    client_socket_file.close()






# TODO: -===  SEND  ===-  
def send_message(client_socket, client_socket_file, server_ip, server_port):
    while True:
        show_menu_jenis_pesan()
        choice = int(input("Masukkan pilihan: "))
        if choice == 0:
            break
        elif choice == 1 or choice == 2:
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
    print(message)


def send_message_file(client_socket_file, server_ip, server_port):
    show_clients()
    no_client = int(input("Masukkan client_id tujuan: "))
    destination_ip = data_clients[no_client]['ip']
    destination_port = data_clients[no_client]['port']
    
    file_path = input("Masukkan path file: ")
    file = open(file_path, "rb")
    file_size = os.path.getsize(file_path)

    with open(file_path, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            client_socket_file.sendall(data)
            
    # formatted_message = f"{choice}|{destination_ip}|{destination_port}|{file_size}|"
    # client_socket.sendto(formatted_message.encode('utf-8') + b'<END>', (server_ip, server_port))
    # print(f"File terkirim ke {destination_ip}:{destination_port}")
    
    
    
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
