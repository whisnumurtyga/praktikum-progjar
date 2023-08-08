import socket
import threading
import os



# TODO: PER-SETUPAN
# Untuk MultiCast
data_groups = ['224.0.0.1', '224.0.0.2']

# Daftar data client
data_clients = {
    1: {'ip': '127.0.0.3', 'port': 12353, 'mcast': data_groups[0]},
    1: {'ip': '127.0.0.4', 'port': 12354, 'mcast': data_groups[0]},
    2: {'ip': '127.0.0.5', 'port': 12355, 'mcast': data_groups[1]}
}

def get_all_ips(data_clients):
    ip_clients = []
    for client_id, client_data in data_clients.items():
        ip_clients.append(client_data['ip'])
    return ip_clients

# Untuk Broadcast
ip_clients = get_all_ips(data_clients)




# TODO: -===  MAIN  ===-
def main():
    server_ip = "127.0.0.1"
    server_port = 12345
    


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.bind((my_ip, my_port))
    client_socket.connect((server_ip, server_port))
    print("Client berjalan...")

    send_thread = threading.Thread(target=send_message, args=(client_socket, server_ip, server_port))
    send_thread.start()
    
    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
    receive_thread.daemon = True  # Menandai thread receive sebagai daemon, sehingga berhenti saat program utama berhenti.
    receive_thread.start()
    
    send_thread.join()
    
    client_socket.close()
    



# TODO: -===  SEND  ===-
def send_message(client_socket, server_ip, server_port) :
    while True:
        msg = 'oioi'
        client_socket.sendall(msg.encode(), (server_ip, int(server_port)))
        choice, dest, msg_type = select_tujuan()
        return
        if msg_type == 0:
            break
        elif msg_type == 1 or msg_type == 2:
            handle_msg_txt(choice, dest, msg_type, client_socket)
            
    client_socket.close()
    
    
    

# TODO: -===  HANDLE MESSAGE  ===-
def handle_msg_txt(choice, dest, msg_type, client_socket):
    dest_ip = data_clients[dest]['ip']
    dest_port = data_clients[dest]['port']

    if msg_type == 1:
        msg = input("Masukkan pesan: ")
    elif msg_type == 2:
        print("Masukkan pesan (ketik '.' di baris baru untuk mengakhiri):")
        msg_lines = []
        while True:
            line = input()
            if line == '.':
                break
            msg_lines.append(line)
        msg = '\n'.join(msg_lines)

    # Format pesan: "<msg_type>|<dest_ip>|<dest_port>|<msg>"
    form_msg = f"{msg_type}|{dest_ip}|{dest_port}|{msg}"
    client_socket.sendto(form_msg.encode('utf-8'), (dest_ip, dest_port))
    print(f"Pesan terkirim ke {dest_ip}:{dest_port}")




# TODO: -===  RECIEVE  ===-
def receive_message(client_socket):
    while True:
        data, server_address = client_socket.recvfrom(2084)
        msg_type = data.split(b'|')[0]

        if msg_type == b'1' or msg_type == b'2':
            data = data.decode('utf-8')
            msg_type, fromm, message = data.split('|')
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
    print('\n')


def show_tujuan():
    print('Pilih Teknik Pengiriman Data')
    print("1. Unicast")
    print("2. Multicast")
    print("3. Broadcast")


def select_tujuan():
    show_tujuan()
    choice = input("Pilih Jenis Pengiriman Data: ")
    if choice == 1:
        show_clients()
        dest = input("Masukkan Client Id Tujuan: ")
        show_menu_jenis_pesan()
        msg_type = input("Masukkan Jenis Pesan: ")
        return int(choice), int(dest), int(msg_type)
    elif choice == 2:
        # show_mcast_group()
        print('sabar masih belum dibikin')
        return
    elif choice == 3:
        print('sabar masih belum dibikin')
        return
    
    
def show_clients():
    # Menggunakan loop for bersarang untuk mencetak semua key dan value
    for client_id, client_info in data_clients.items():
        print(f"Client ID: {client_id}\tIP: {client_info['ip']}\t Port:{client_info['port']}")


def show_mcast_group():
    for index, group in enumerate(data_groups):
        print(f'Group-{index+1}\t{group}')







# TODO: -===  MAIN  ===-
if __name__ == "__main__":
    main()
