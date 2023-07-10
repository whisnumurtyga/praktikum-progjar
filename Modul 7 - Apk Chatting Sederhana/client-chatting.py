from email import message
import socket
from threading import Thread 

# Konfigurasi Client dan Server
connectionSocket = socket.socket()
serverIp = "127.0.0.1"
serverPort = 2222

def kirimPesan(handlerSocket: socket.socket):
    while True:
        message = input()
        handlerSocket.send(message.encode())
        print(f"Client : {message}")
        if message.lower() == "exit":
            break

def terimaPesan(handlerSocket: socket.socket):
    while True:
        message = handlerSocket.recv(1024)
        print(f"Server : {message.decode('utf-8')}")
        if message.decode('utf-8').lower() == "exit":
            break
        
# Menhubungi Server
connectionSocket.connect((serverIp, serverPort))
print("Terhubung dengan Server")

t1 = Thread(target=terimaPesan, args=(connectionSocket,))
t2 = Thread(target=kirimPesan, args=(connectionSocket,))

t1.start()
t2.start()

t1.join()
t2.join()
