from socket import socket #??
from socket import AF_INET #??
from socket import SOCK_DGRAM #??
import os #Modul til oprette filer
from datetime import datetime, timedelta #Modul til dato og tid
import GetIP #Importere IP script

current_time = datetime.utcnow() #Opretter U-tid
formatted_time = current_time + timedelta(hours=2) #Lægger 2 timer oveni
dato = formatted_time.strftime('%Y-%m-%d') #Opretter dato variabel, tager kun year-month-date
tid = formatted_time.strftime('%H.%M.%S') #Oprette tid variabel, tager kun hour.minute.seconds
datotid = f'{dato} {tid}' #Opretter datotid variabel
folder_name = f'Observationer ({datotid})' #Opretter variabel med folder_name +datotid
os.mkdir(folder_name) #Opretter mappe med folder_name
file_path = f'./Observationer ({datotid})/' #Hvor den skal oprette .txt filer

server_port = 12000 #??
server_socket = socket(AF_INET, SOCK_DGRAM) #??
server_socket.bind(('', server_port)) #??
print('server is ready to recieve') #Viser at server er klar til at modtage dato
while True: #Loop starter
    try:
        message, client_address = server_socket.recvfrom(2048) #??
        modified_message = message.decode() #??
        server_socket.sendto(modified_message.encode(), client_address) #??
        if '##!, ' in modified_message: #Hvis modtaget besked har ##!, behandler vi denne besked
            messege = modified_message.split(',') #Opretter variabel til liste efter hvert ,
            if os.path.isfile(file_path + 'Spillernummer ' + messege[1] + '.txt') == False: #Tjekker om der er oprettet en fil for given spiller
                with open(file_path + 'Spillernummer ' + messege[1] + '.txt', "a") as file: #Hvis spilleren ikke findes, oprettes fil med spiller
                    file.write(f'Spiller observationer for spiller nummer{messege[1]}\nObservationerne er lavet d. {dato}\n\nObservationerne er formateret som:\nTidspunkt, Afsender, Observation\n\n') #Intro til spiller fil
            with open(file_path + 'Spillernummer ' + messege[1] + '.txt', "a") as file: #Åbner given spiller fil i "append mode"
                file.write(f'*{messege[4]} -{messege[3]}:{messege[2]}\n') #Skriver kommentar i fil +linje skift

        if modified_message != '': #Resetter besked
            print(modified_message)
            modified_message = ''
    except KeyboardInterrupt: #CTRL C lukker program
        print('CTRL-C pressed, closing down!')
        server_socket.close()
        exit()


