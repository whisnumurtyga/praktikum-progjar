import socket
import threading
import os
import datetime
        
def main():
    server_ip = "127.0.0.1"
    server_port = 12345
    
    my_ip = '127.0.0.3'
    my_port = 12347

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind((my_ip, my_port))
    print("UDP client berjalan...")

    send_thread = threading.Thread(target=send_message, args=(client_socket, server_ip, server_port))
    send_thread.start()
    send_thread.join()
    
        

def send_message(client_socket, server_ip, server_port):
    while True:
        print("Pilih menu:")
        print("1. Kirim Pesan")
        print("2. Kirim Pesan Paragraph")  # Tambahkan pilihan ini
        print("3. Kirim File PDF/DOCX")
        print("0. Keluar")
        choice = input("Masukkan pilihan (0/1/2/3): ")
        
        if choice == '3':
            file_path = input("Masukkan path file PDF/DOCX: ")
            if os.path.exists(file_path):
                send_file(choice, client_socket, server_ip, server_port, file_path)
            else:
                print("File tidak ditemukan.")

    client_socket.close()
   
    
#     print("File berhasil dikirim ke server.")
def send_file(choice, client_socket, server_ip, server_port, file_path):
    file_size = os.path.getsize(file_path)
    init_msg = f'{choice}|{file_size}|{os.path.basename(file_path)}|'

    # Baca dan kirim file dalam bentuk chunk
    i = 0
    total = 0
    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(2084)
            if not chunk:
                break
            print(f'i:{i}\t{len(chunk)}\t{chunk}')
            i+=1
            total += len(chunk)
            client_socket.sendto(init_msg.encode('utf-8') + chunk , (server_ip, server_port))
            print(total)
    # print(f"{file_path} berhasil dikirim.")
    # print(f"{file_size}")


if __name__ == "__main__":
    main()
