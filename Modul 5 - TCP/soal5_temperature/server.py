import socket

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

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

    # Parse pesan dari klien
    parts = data.split()
    value = float(parts[0])
    unit_from = parts[1]
    unit_to = parts[3]

    # Konversi suhu
    if unit_from == 'C':
        if unit_to == 'F':
            result = celsius_to_fahrenheit(value)
            response = f"{value} Celsius = {result} Fahrenheit"
        elif unit_to == 'K':
            result = celsius_to_kelvin(value)
            response = f"{value} Celsius = {result} Kelvin"
        else:
            response = "Invalid input"
    elif unit_from == 'F':
        if unit_to == 'C':
            result = fahrenheit_to_celsius(value)
            response = f"{value} Fahrenheit = {result} Celsius"
        elif unit_to == 'K':
            result = fahrenheit_to_kelvin(value)
            response = f"{value} Fahrenheit = {result} Kelvin"
        else:
            response = "Invalid input"
    elif unit_from == 'K':
        if unit_to == 'C':
            result = kelvin_to_celsius(value)
            response = f"{value} Kelvin = {result} Celsius"
        elif unit_to == 'F':
            result = kelvin_to_fahrenheit(value)
            response = f"{value} Kelvin = {result} Fahrenheit"
        else:
            response = "Invalid input"
    else:
        response = "Invalid input"

    # Kirim balasan ke klien
    conn.sendall(response.encode())

# Tutup koneksi
conn.close()
