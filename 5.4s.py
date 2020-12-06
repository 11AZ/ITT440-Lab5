import socket
import tqdm
import os
import json
import sys

#create server socket
s = socket.socket()
print(f"[+] socket succesffuly created")

#server port
port = 8888

#bind the socket
s.bind(('',port))
print(f"[+] socket binded to " + str(port))

#receive bytes
BUFFER_SIZE = 4096

SEPARATOR = "<SEPARATOR>"

#Enabling server to  accept connection
#5 is the number of unaccpeted connections
s.listen(5)
print(f"[+] Socket is listening ")

#accept conncetion if there is any
client_socket, address = s.accept()

#show the sender is connected
printf("[+] {address} is connected.")

#receive file infos
#receive use client socket
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)

#remove absolute path if there is
filename = os.path.basename(filename)

#convert to integer
filesize = int(filesize)

#start receive file from socket and write to the file stream
progress = tqdm.tqdm(range(filesize), f("Receiving {filename}", unit="B", unit_scale = TRUE, unit_divisor = 1024)

with open(filename, "wb") as f:
	for _ in progress:
	#read 1024 bytes from the socket(receive)
	bytes_read = client.socket.recv(BUFFER_SIZE)
	if not byte_read:
	break

	#write file the bytes just recived
	f.write(bytes_read)
	#update the progress bar
	progress.update(len(bytes_read))

#close teh client socket
client_socket.close()
#close the server socket
s.close()
