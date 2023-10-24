import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("10.0.0.0", 80))
print(f'Server IP address: {s.getsockname()[0]}')
