import os
import socket

socket_sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connection to server using given port
receiver_info = ("localhost", 59000)
socket_sender.connect(receiver_info)


pwd = os.getcwd()
os.chdir("C:\Users\Sam\Desktop")  # example
files = os.listdir("C:\Users\Sam\Desktop")


for file in files:
    if file.endswith(".txt"):
        print(file)

        f = open(file, "rb")
        content = f.read(1024)

        while content:
            socket_sender.send(content)
            content = f.read(1024)

        f.close()

#socket_sender.send(bytes("done"))

socket_sender.close()

