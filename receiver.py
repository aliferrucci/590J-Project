import os
import sys
import socket

if __name__ == "__main__":
    try:
        # create a socket
        socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_connection.bind(("10.0.0.196", 59000))

        # listen for a client
        socket_connection.listen()
        client_request, r = socket_connection.accept()

        os.chdir('/home/kali/Desktop/files/')# put path of the directory you want the files to go)

        # naming title
        count = 1
        done = False
        data = b''
        while b'\x00\x01\x02END\x00\x01\x02' not in data:
            data += client_request.recv(1024)

        # Cut out the end bytes
        data = data[:len(data)-9]
        # Split the data by file
        datalist = data.split(b'\x00\x01\x02BEGIN\x00\x01\x02')
        datalist.pop(0)

        for filedata in datalist:
            # Split apart file name and file contents
            fileFormat = filedata.split(b'\x00\x01\x02FILENAME\x00\x01\x02')
            f = open(fileFormat[0], "wb")
            f.write(fileFormat[1])
            f.close()

    except KeyboardInterrupt:
        sys.exit()
