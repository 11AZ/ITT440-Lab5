import socket
import tqdm
import os
import json
import sys


SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 #send 4096 bytes each time step

#create client socket
s = socket.socket()
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
print("Filename:", filename)
#get the file size
filesize = os.path.getsize(filename)

#send the filename and filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

#start sending file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
        for _ in progress:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
#close socket
s.close()


