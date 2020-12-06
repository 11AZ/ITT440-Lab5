import socket
import tqdm
import os
import json
import sys

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 #send 4096 bytes each time step

#create client socket
s= socket.socket()
#the ip address of the server
host = "192.168.0.101"
#port use
port = 8888

#connect to server
print(f"[+] Connecting to {host}:{port}")
s.connect((host,port))
print("[+] COnnected")

#user input file name
filename = input("Enter file name")

#get the file size
file size = os.path.getsize(filename)

#send the filename and filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

progress = tqdm.tqdm(range(filesize),f"Sending{filename}", unit ="B", unit_scale=true, unit_divisor=1024)
with open(filename,"rb")as f:

	for _ in progress:
	#read the bytes from the file
	bytes_read= f.read(BUFFER_SIZE)
	if not bytes_read:
		#file transmitting is done
		break
	#use sendall to assure transimission in busy network
	s.sendall(bytes_read)
	#update the progress bar
	progess.update(len(bytes_read))

#close socket
s.close()


