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
            #f = open("file" + str(count) + ".txt", "wb")
            data += client_request.recv(1024)
            #if data.find(b'\x00\x01END\x00\x01')
            #while data:
                #data += client_request.recv(1024)
                #print(data)
                #print("hello1")
                #f.write(data)
                #data += client_request.recv(1024)
                #print(data)

            #else:
                #f.close()
                #rint("done")
                #data = b''
                #count += 1
        data = data[:len(data)-9]
        datalist = data.split(b'\x00\x01\x02BEGIN\x00\x01\x02')
        datalist.pop(0)
        print(datalist)

        for filedata in datalist:
            fileFormat = filedata.split(b'\x00\x01\x02FILENAME\x00\x01\x02')
            f = open(fileFormat[0], "wb")
            f.write(fileFormat[1])
            f.close()

    except KeyboardInterrupt:
        sys.exit()
