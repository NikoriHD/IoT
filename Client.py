from socket import socket
from socket import AF_INET
from socket import SOCK_DGRAM
from sys import exit
from datetime import datetime, timedelta

afsender = input('Instast dit navn: ')

server_name = input("Angiv server IP: ")
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    try:
        spillernummer = input('Indtast spillernummer: ')
        observation = input('Indtast observation: ')
        nu_tid = datetime.utcnow()
        nu_tid2 = nu_tid + timedelta(hours=2)
        tid = nu_tid2.strftime('%H:%M:%S')
        message = '##!, ' + spillernummer + ', ' + observation + ', ' + afsender + ', ' + tid
        client_socket.sendto(message.encode(), (server_name, server_port))
        modified_message, server_adress = client_socket.recvfrom(2048)
        print(modified_message.decode())
    except KeyboardInterrupt:
        client_socket.close()
        exit()