import socket

def find_available_port(start_port, end_port):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', port))
        if result != 0:
            return port
    return None

start_port = 8000
end_port = 9000
available_port = find_available_port(start_port, end_port)
if available_port:
    print(f"Свободный порт: {available_port}")
else:
    print("В указанном диапазоне портов нет свободных портов.")
