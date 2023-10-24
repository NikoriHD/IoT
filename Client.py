from socket import socket #??
from socket import AF_INET #??
from socket import SOCK_DGRAM #?
from sys import exit #??
from datetime import datetime, timedelta #Importere dato og tid moduler

afsender = input('Instast dit navn: ') #Opretter variabel "afsender", input fra shell

server_name = input("Angiv server IP: ") #Opretter variabel til server navn, input fra shell
server_port = 12000 #??
client_socket = socket(AF_INET, SOCK_DGRAM) #??

while True: #Starter Loop
    try:
        spillernummer = input('Indtast spillernummer: ') #Variabel til spiller nummer, input fra shell
        observation = input('Indtast observation: ') #Variabel til obs, input fra shell
        nu_tid = datetime.utcnow() #Variabel til Universel tid
        nu_tid2 = nu_tid + timedelta(hours=2) #Omregner til U-tid dansk tid
        tid = nu_tid2.strftime('%H:%M:%S') #Redigere tiden til ordenlig fremvisning af tid
        message = '##!, ' + spillernummer + ', ' + observation + ', ' + afsender + ', ' + tid #Message layout
        client_socket.sendto(message.encode(), (server_name, server_port)) #?? Sender besked til ønsket server_port
        modified_message, server_adress = client_socket.recvfrom(2048) #??
        print(modified_message.decode()) #Printer besked
    except KeyboardInterrupt: #Stopper program
        client_socket.close()
        exit()
