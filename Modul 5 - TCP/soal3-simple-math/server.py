import socket

HOST = ''  # Alamat IP server
PORT = 12345  # Port server

# Buat socket server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print('Server listening on', PORT)

# Tunggu koneksi dari klien
conn, addr = s.accept()
print('Connected by', addr)

while True:
    # Baca data dari klien
    data = conn.recv(1024).decode()
    if not data:
        # Jika data kosong, berarti koneksi ditutup oleh klien
        break

    # Parse pesan dari klien menjadi operasi dan angka
    operation, operand1, operand2 = data.split()
    operand1 = float(operand1)
    operand2 = float(operand2)

    # Lakukan operasi matematika sesuai permintaan klien
    if operation == '+':
        result = operand1 + operand2
    elif operation == '-':
        result = operand1 - operand2
    elif operation == '*':
        result = operand1 * operand2
    elif operation == '/':
        if operand2 != 0:
            result = operand1 / operand2
        else:
            result = "Error: Division by zero"
    else:
        result = "Error: Invalid operation"

    # Kirim balasan ke klien
    response = str(result)
    conn.sendall(response.encode())

# Tutup koneksi
conn.close()
