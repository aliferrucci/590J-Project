import os
import sys
import socket

if __name__ == "__main__":
    try:
        # create a socket
        socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_connection.bind(("localhost", 59000))

        # listen for a client
        socket_connection.listen()
        client_request, r = socket_connection.accept()

        os.chdir(# put path of the directory you want the files to go)

        # naming title
        count = 1
        done = False

        while True:
            f = open("file" + str(count) + ".txt", "wb")
            data = client_request.recv(1024)
            while data:
                data = client_request.recv(1024)
                print("hello1")
                f.write(data)
                data = client_request.recv(1024)

            else:
                f.close()
                print("done")
                count += 1

    except KeyboardInterrupt:
        sys.exit()





