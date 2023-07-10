import socket

def startClient():
    # Konfigurasi host dan port server
    host = "127.0.0.1"
    port = 8000
    
    # Membuat Socket Client
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((host,port))
    
    try:
        while True:
            # Mengirim pesan ke server
            message = input("Your message: ")
            clientSocket.send(message.encode('utf-8'))
            
            if message == "exit":
                break
            
            # Menerima balasan dari server
            response = clientSocket.recv(1024).decode('utf-8')
            print(f"[ SERVER RESPONSE ] {response}")   
        
    finally:
        # Menutup koneksi dengan server
        clientSocket.close()

startClient()