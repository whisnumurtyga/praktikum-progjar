import socket
from threading import Thread

# Konfigurasi Server
listenerSocket = socket.socket()
serverIP = "0.0.0.0"
serverPort = 2222

def kirimPesan(handlerSocket: socket.socket) :
    while True:
        message = input()
        handlerSocket.send(message.encode())
        print(f"Server : {message}")
        if message.lower() == "exit":
            break
        
def terimaPesan(handlerSocket: socket.socket) :
    while True:
        message = handlerSocket.recv(1024)
        print(f"Client : {message.decode('utf-8')}")
        if message.decode('utf-8').lower() == "exit":
            break
        
# Binding socket dengan IP dan port
listenerSocket.bind((serverIP, serverPort))

# Listener socket siap menerima koneksi
listenerSocket.listen(0)
print("Server menunggu koneksi dari client")

# Listener socket mengunggu koneksi dari client, baris ini bersifat blocking, artinya program berhenti di sini sampai ada koneksi ke listenerSocket
handler, addr = listenerSocket.accept()
# Jika sudah ada koneksi dari client, maka program akan menjalankan baris ini
print(f"Sebuah client terkoneksi dengan alamat: {addr}")

t1 = Thread(target=kirimPesan, args=(handler,))
t2 = Thread(target=terimaPesan, args=(handler,))

t1.start()
t2.start()

t1.join()
t2.join()
