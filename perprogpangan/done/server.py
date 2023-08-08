import socket
import threading
import os
import tqdm


store_message = []
List_ip = [
    ("192.168.43.67", 8008),
    ("192.168.43.121", 12345),
    # ("127.0.0.4", 9002),
]


# Create a DP socket
class sockConfig:
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_address = ("192.168.43.176", 8001)
    udp_socket.bind(local_address)


def showMessage():
    for conv in store_message:
        print(conv)


def multiCast(udp_socket):
    choose = []
    for i in range(len(List_ip)):
        print("Pilih IP:")
        for idx, address in enumerate(List_ip):
            print(f"{idx}. {address}")
        print("4. Exit")

        list_index = int(input("Masukan no : "))
        if list_index == 4:
            break
        choose.append(list_index)
        os.system("cls")
    # PENGIRIMAN
    mode = mode_pesan()
    if mode == 1:
        message = input("Masukan pesan : ")
        store_message.append(f"you : {message}")
        for i in choose:
            udp_socket.sendto(message.encode("utf-8"), List_ip[i])
    elif mode == 2:
        message = []
        print("input paragraf :")
        while True:
            message.append(input("Ketika (.) untuk berhenti : "))
            if message[-1] == ".":
                message = ". ".join(message)
                break
        print(message)
        store_message.append(f"you : {message}")
        for i in choose:
            udp_socket.sendto(message.encode("utf-8"), List_ip[i])
    elif mode == 3:
        for i in choose:
            send_file(udp_socket, List_ip[i], 3)
    elif mode == 4:
        for i in choose:
            send_file(udp_socket, List_ip[i], 4)
    elif mode == 5:
        for i in choose:
            send_file(udp_socket, List_ip[i], 5)
    elif mode == 6:
        for i in choose:
            send_file(udp_socket, List_ip[i], 6)


def broadcast(udp_socket):
    mode = mode_pesan()
    if mode == 1:
        message = input("Masukan pesan : ")
        store_message.append(f"you : {message}")
        for ip in List_ip:
            udp_socket.sendto(message.encode("utf-8"), ip)
    elif mode == 2:
        message = []
        print("input paragraf :")
        while True:
            message.append(input("Ketika (.) untuk berhenti : "))
            if message[-1] == ".":
                message = ". ".join(message)
                break
        for ip in List_ip:
            udp_socket.sendto(message.encode("utf-8"), ip)
    elif mode == 3:
        for ip in List_ip:
            send_file(udp_socket, ip, 3)
    elif mode == 4:
        for ip in List_ip:
            send_file(udp_socket, ip, 4)
    elif mode == 5:
        for ip in List_ip:
            send_file(udp_socket, ip, 5)
    elif mode == 6:
        for ip in List_ip:
            send_file(udp_socket, ip, 6)


def recvMessage(udp_socket):
    while True:
        data, address = udp_socket.recvfrom(1024)
        message = f"From: {address} : {data.decode('utf-8')}"

        formats = ["docx", "pdf", "jpg", "png", "mp3", "mp4"]
        if any(format in message for format in formats):
            recived_file(udp_socket, data.decode("utf-8"))
        else:
            store_message.append(message)


def sendMessage(udp_socket, address):
    response = input("masukan pesan : ")
    if response != "":
        store_message.append(f"you : {response}")
        udp_socket.sendto(response.encode("utf-8"), address)


def threading_slot():
    recv_thread = threading.Thread(target=recvMessage, args=(sockConfig.udp_socket,))
    recv_thread.daemon = True
    recv_thread.start()


def send_file(udp_socket, server_address, file_format):
    if file_format == 3:
        file_path = "dikirim_whisnu/whisnuPDF.pdf"
    elif file_format == 4:
        file_path = "dikirim_whisnu/whisnuJPG.jpg"
    elif file_format == 5:
        file_path = "dikirim_whisnu/whisnuMP3.mp3"
    elif file_format == 6:
        file_path = "dikirim_whisnu/whisnuMP4.mp4"

    file_name = os.path.basename(file_path)
    file_size = str(os.path.getsize(file_path))

    print(file_name)
    udp_socket.sendto(f"{file_name},{file_size}".encode(), server_address)

    with open(file_path, "rb") as file:
        # progress = tqdm.tqdm(unit="b", unit_scale=True, unit_divisor=1000, total=file_size)
        for data in iter(lambda: file.read(1024), b""):
            udp_socket.sendto(data, server_address)
            # progress.update(len(data))

    udp_socket.sendto(b"<END>", server_address)
    print("Data Send Succesfully")


def recived_file(udp_socket, file_info):
    file_info = file_info.split(",")
    file_name = file_info[0]
    file_size = int(file_info[1])
    
    destination_folder = "download_server"
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    file_path = os.path.join(destination_folder, file_name)

    with open(file_path, "wb") as file:
        received_bytes = 0
        progress = tqdm.tqdm(unit="b", unit_scale=True, unit_divisor=1000, total=file_size)
        while received_bytes < file_size:
            data, _ = udp_socket.recvfrom(1024)
            received_bytes += len(data)
            file.write(data)
            progress.update(len(data))

    print("File berhasil diterima: ", file_path)


def mode_pesan():
    print(
        """
            1. Kirim 1 kalimat
            2. Kirim 1 paragraph
            3. Kirim dokumen (docx/pdf)
            4. Kirim gambar (jpg/png)
            5. Kirim suara (mp3)
            6. Kirim video (mp4)
"""
    )
    return int(input("Pilih Mode Pesan : "))


def main():
    threading_slot()

    while True:
        showMessage()
        choose = input(
            "1. Unicast\n2. MultiCast\n3. Broadcast\n4. Lihat Pesan\ninsert number : "
        )

        if choose == "1":
            print("Pilih IP:")
            for idx, address in enumerate(List_ip):
                print(f"{idx}. {address}")
            dst = int(input("Masukkan IP Tujuan : "))
            showMessage()
            mode = mode_pesan()
            if mode == 1:
                sendMessage(sockConfig.udp_socket, List_ip[dst])
            elif mode == 2:
                message = []
                print("input paragraf :")
                while True:
                    message.append(input("Ketika (.) untuk berhenti : "))
                    if message[-1] == ".":
                        message = ". ".join(message)
                        break
            elif mode == 3:
                send_file(sockConfig.udp_socket, List_ip[dst], 3)
            elif mode == 4:
                send_file(sockConfig.udp_socket, List_ip[dst], 4)
            elif mode == 5:
                send_file(sockConfig.udp_socket, List_ip[dst], 5)
            elif mode == 6:
                send_file(sockConfig.udp_socket, List_ip[dst], 6)
        elif choose == "2":
            multiCast(sockConfig.udp_socket)
        elif choose == "3":
            broadcast(sockConfig.udp_socket)
        else:
            pass

        os.system("cls")


if __name__ == "__main__":
    main()
