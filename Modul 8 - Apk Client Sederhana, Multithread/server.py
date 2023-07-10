import socket
import threading

def handleClient(clientSocket, clientAddress):
    print(f"[ NEW CONNECTION ] Client {clientAddress} connected.")

    try:
        while True:
            # Menerima pesan dari client
            message = clientSocket.recv(1024).decode('utf-8')
            if message == "exit":
                break

            # Menampilkan pesan dari client
            print(f"[ CLIENT {clientAddress} ] {message}")

            # Mengirim Balasan ke Client
            response = input("Your Response: ")
            clientSocket.send(response.encode('utf-8'))

    finally:
        # Menutup koneksi dengan client
        clientSocket.close()
        print(f"[ CONNECTION CLOSED ] Client {clientAddress} disconnected")


def startServer():
    # Konfigurasi Host dan Port
    host = "127.0.0.1"
    port = 8000

    # Membuat Socket Server
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((host, port))
    serverSocket.listen(5)
    print("[ SERVER STARTED ] Waiting for Connections")

    while True:
        # Menerima Koneksi dari Client
        clientSocket, clientAddress = serverSocket.accept()

        # Menangani koneksi client dalam thread baru
        clientThread = threading.Thread(target=handleClient, args=(clientSocket, clientAddress))
        clientThread.start()

startServer()
